# travlr.explore

Agentic environment for TRAVLR's explore section. Datasets are organized by folder to keep marker data and metadata together for the explore experience.

## Structure
- `AGENTS.md` — working instructions for maintaining the explore datasets.
- `datasets/<dataset-id>/data.json` — dataset markers or geometries.
- `datasets/<dataset-id>/description.json` — dataset metadata (`id`, `name`, `index`, `title`, `description`, `markercount`).
- `tools/` — helper scripts for dataset maintenance and asset management.

## Current datasets
1. **Lord of the Rings Filming Locations** (`lotr-locations`) — 131 markers.
2. **Reddit Travel Locations** (`reddit-travel-locations`) — 26,479 markers.
3. **UNESCO World Heritage Sites - Natural** (`unesco-nature`) — 203 markers.
4. **UNESCO World Heritage Sites - Human** (`unesco-human`) — 849 markers.
5. **Country and US Bounding Boxes** (`country-bounds`) — 254 entries.
6. **Meteorite Landings** (`meteorites`) — 45,716 entries.
7. **Star Wars Filming & Story Locations** (`star-wars-locations`) — 62 markers.
8. **United States Feature Collection** (`us-states`) — 52 features.
9. **Harry Potter Filming Locations** (`harry-potter-locations`) — 74 markers with per-entry confidence ratings.

## Adding a dataset
1. Create `datasets/<dataset-id>/` and place the source JSON in `data.json` without altering its structure unless necessary.
2. Add a `description.json` with the required metadata fields and updated `markercount`.
3. Update this README to include the new dataset summary.

## Tools
- `tools/download_images.py` — download images from an `images.txt` manifest. Use `--dataset <id>` to drop images into `datasets/<id>/assets/images` (or override with `--out`). The script commits changes by default and only pushes when `--push` is provided. Requires the `requests` package.
