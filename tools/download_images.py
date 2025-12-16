#!/usr/bin/env python3
"""
Download images and commit them into the current git repo, optionally targeting a dataset.

Input file format (images.txt), one per line:
  URL
  URL <whitespace> filename
  URL <whitespace> filename <whitespace> referer

Examples:
  https://example.com/a.jpg
  https://example.com/a.jpg datasets/lotr-locations/assets/images/a.jpg
  https://cdn.site.com/img/123.png datasets/lotr-locations/assets/images/123.png https://site.com/gallery

Notes:
- If filename is omitted, the script will derive one from the URL.
- If referer is omitted, it will derive referer from the URL origin.
- When `--dataset` is provided, the default output becomes `datasets/<id>/assets/images`.
- Use `--push` if you really need to push to the remote; by default the script keeps changes local.
"""

from __future__ import annotations

import hashlib
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse, unquote

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


DEFAULT_ASSETS_DIR = Path("assets/images")
DEFAULT_LIST_FILE = Path("images.txt")
DATASETS_DIR = Path("datasets")


@dataclass
class Item:
    url: str
    out_path: Path
    referer: str


def die(msg: str, code: int = 1) -> None:
    print(f"[error] {msg}", file=sys.stderr)
    sys.exit(code)


def run(cmd: list[str]) -> str:
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{p.stdout}")
    return p.stdout.strip()


def sanitize_filename(name: str) -> str:
    name = name.strip().replace("\\", "/").split("/")[-1]
    name = re.sub(r"[^A-Za-z0-9._-]+", "_", name)
    return name or "image"


def ext_from_content_type(ct: str) -> str | None:
    ct = (ct or "").split(";")[0].strip().lower()
    return {
        "image/jpeg": ".jpg",
        "image/jpg": ".jpg",
        "image/png": ".png",
        "image/webp": ".webp",
        "image/gif": ".gif",
        "image/svg+xml": ".svg",
        "image/avif": ".avif",
        "image/heic": ".heic",
        "image/heif": ".heif",
        "image/bmp": ".bmp",
        "image/tiff": ".tiff",
    }.get(ct)


def derive_filename_from_url(url: str) -> str:
    p = urlparse(url)
    base = unquote(Path(p.path).name)
    base = sanitize_filename(base)
    if "." not in base:  # no extension in URL path
        h = hashlib.sha256(url.encode("utf-8")).hexdigest()[:12]
        base = f"{base}_{h}"
    return base


def derive_referer(url: str) -> str:
    p = urlparse(url)
    if not p.scheme or not p.netloc:
        return ""
    return f"{p.scheme}://{p.netloc}/"


def compute_default_out_dir(dataset_id: str | None) -> Path:
    if dataset_id:
        return DATASETS_DIR / dataset_id / "assets/images"
    return DEFAULT_ASSETS_DIR


def parse_list(path: Path, out_dir: Path) -> list[Item]:
    if not path.exists():
        die(f"List file not found: {path}")

    items: list[Item] = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        parts = line.split()
        url = parts[0]

        filename = None
        referer = None
        if len(parts) >= 2:
            filename = parts[1]
        if len(parts) >= 3:
            referer = parts[2]

        if filename:
            out_path = Path(filename)
        else:
            out_path = out_dir / derive_filename_from_url(url)

        if not referer:
            referer = derive_referer(url)

        items.append(Item(url=url, out_path=out_path, referer=referer))

    return items


def make_session() -> requests.Session:
    s = requests.Session()

    retries = Retry(
        total=5,
        backoff_factor=0.6,
        status_forcelist=[403, 408, 429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD"],
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retries, pool_connections=10, pool_maxsize=10)
    s.mount("http://", adapter)
    s.mount("https://", adapter)
    return s


def download_one(session: requests.Session, item: Item, sleep_s: float = 0.3) -> bool:
    item.out_path.parent.mkdir(parents=True, exist_ok=True)

    headers = {
        "User-Agent": os.environ.get("IMG_UA", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"),
        "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": item.referer or "",
    }

    try:
        h = session.head(item.url, headers=headers, timeout=20, allow_redirects=True)
        _ = h.status_code
    except Exception:
        pass

    r = session.get(item.url, headers=headers, timeout=40, allow_redirects=True)
    if r.status_code != 200:
        print(f"[fail] {item.url} -> HTTP {r.status_code}")
        return False

    ct = r.headers.get("Content-Type", "")
    if not ct.lower().startswith("image/"):
        snippet = r.text[:200].replace("\n", " ")
        print(f"[fail] {item.url} -> not an image (Content-Type={ct}); starts: {snippet!r}")
        return False

    if item.out_path.suffix == "":
        ext = ext_from_content_type(ct) or ".img"
        item.out_path = item.out_path.with_suffix(ext)

    if item.out_path.exists():
        old = item.out_path.read_bytes()
        if hashlib.sha256(old).digest() == hashlib.sha256(r.content).digest():
            print(f"[skip] unchanged: {item.out_path}")
            time.sleep(sleep_s)
            return True

    item.out_path.write_bytes(r.content)
    print(f"[ok] {item.url} -> {item.out_path} ({len(r.content)} bytes)")
    time.sleep(sleep_s)
    return True


def ensure_git_repo() -> None:
    try:
        run(["git", "rev-parse", "--is-inside-work-tree"])
    except Exception as e:
        die(f"Not a git repository (or git not available). Details:\n{e}")


def ensure_dataset(dataset_id: str | None) -> None:
    if not dataset_id:
        return
    dataset_root = DATASETS_DIR / dataset_id
    if not dataset_root.exists():
        die(f"Dataset directory not found: {dataset_root}")
    if not dataset_root.is_dir():
        die(f"Dataset path is not a directory: {dataset_root}")


def git_commit_and_push(message: str, push: bool) -> None:
    run(["git", "add", "-A"])
    status = run(["git", "status", "--porcelain"])
    if not status.strip():
        print("[git] no changes to commit")
        return

    run(["git", "commit", "-m", message])
    print("[git] committed")

    if not push:
        print("[git] push skipped (use --push to enable)")
        return

    run(["git", "push"])
    print("[git] pushed ✅")


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--list", default=str(DEFAULT_LIST_FILE), help="Path to images list file")
    parser.add_argument(
        "--dataset", help="Dataset id under datasets/; sets default output to datasets/<id>/assets/images"
    )
    parser.add_argument("--out", help="Default output directory; overrides --dataset")
    parser.add_argument("--commit-message", default="Add downloaded images", help="Git commit message")
    parser.add_argument("--no-commit", action="store_true", help="Download but do not commit changes")
    parser.add_argument("--push", action="store_true", help="Push after committing changes")
    args = parser.parse_args()

    ensure_git_repo()
    ensure_dataset(args.dataset)

    out_dir = Path(args.out) if args.out else compute_default_out_dir(args.dataset)

    list_file = Path(args.list)

    items = parse_list(list_file, out_dir)
    if not items:
        die("No images found in list file (empty or only comments).")

    session = make_session()

    ok = 0
    for item in items:
        if download_one(session, item):
            ok += 1

    print(f"[done] {ok}/{len(items)} downloaded")

    if args.no_commit:
        print("[git] --no-commit set; skipping commit/push")
        return

    git_commit_and_push(args.commit_message, push=args.push)


if __name__ == "__main__":
    main()
