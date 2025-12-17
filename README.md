# travlr.explore

Agentic environment for TRAVLR's explore section. Datasets are organized by folder to keep marker data and metadata together for the explore experience.

## Structure
- `AGENTS.md` — working instructions for maintaining the explore datasets.
- `datasets/<dataset-id>/data.json` — dataset markers or geometries.
- `datasets/<dataset-id>/description.json` — dataset metadata (`id`, `name`, `index`, `title`, `description`, `markercount`).
- `tools/` — helper scripts for dataset maintenance and asset management.

## Current datasets
### Point datasets
1. **Lord of the Rings Filming Locations** (`lotr-locations`) — 131 markers (Category: Film & TV).
2. **Reddit Travel Locations** (`reddit-travel-locations`) — 26,479 markers (Category: Travel).
3. **UNESCO World Heritage Sites - Natural** (`unesco-nature`) — 203 markers (Category: Heritage).
4. **UNESCO World Heritage Sites - Human** (`unesco-human`) — 849 markers (Category: Heritage).
5. **Meteorite Landings** (`meteorites`) — 45,716 markers (Category: Science).
6. **Star Wars Filming & Story Locations** (`star-wars-locations`) — 62 markers (Category: Film & TV).
7. **Harry Potter Filming Locations** (`harry-potter-locations`) — 74 markers with per-entry confidence ratings (Category: Film & TV).
8. **Game of Thrones Filming Locations** (`game-of-thrones-locations`) — 300 markers with cFactor confidence scores for each site (Category: Film & TV).
9. **James Bond Filming & Story Locations** (`james-bond-locations`) — 62 markers mixing filming sites and in-universe anchors with confidence factors (Category: Film & TV).
10. **World Pyramids** (`pyramids`) — 122 markers spanning ancient through modern pyramids (Category: Architecture).
11. **Iconic Waterfalls** (`waterfalls`) — 1100 markers with heights and confidence factors (Category: Nature).
12. **Traditional Dishes and Origins** (`traditional_food`) — 800 markers tying iconic recipes to the precise venues where they originated, each with a cFactor confidence note (Category: Food & Culture).
9. **World Pyramids** (`pyramids`) — 122 markers spanning ancient through modern pyramids (Category: Architecture).
10. **Iconic Waterfalls** (`waterfalls`) — 1100 markers with heights and confidence factors (Category: Nature).
11. **Traditional Dishes and Origins** (`traditional_food`) — 800 markers tying iconic recipes to the precise venues where they originated, each with a cFactor confidence note (Category: Food & Culture).
12. **Assassin's Creed Real-World Locations** (`assassins-creed-locations`) — 263 markers mapping historical sites and analogs from the franchise (Category: Games).
12. **Fallout Explorable Locations** (`fallout-explore`) — 350 markers mapping Fallout's Mojave, Capital Wasteland, Commonwealth, and New California locales to real-world coordinates with confidence ratings (Category: Film & TV).

### Polygon datasets
13. **Country and US Bounding Boxes** (`country-bounds`) — 254 entries (Category: Boundaries).
14. **United States Feature Collection** (`us-states`) — 52 features (Category: Boundaries).

## Adding a dataset
1. Create `datasets/<dataset-id>/` and place the source JSON in `data.json` without altering its structure unless necessary.
2. Add a `description.json` with the required metadata fields and updated `markercount`.
3. Update this README to include the new dataset summary.

## Tools
- `tools/download_images.py` — download images from an `images.txt` manifest. Use `--dataset <id>` to drop images into `datasets/<id>/assets/images` (or override with `--out`). The script commits changes by default and only pushes when `--push` is provided. Requires the `requests` package.
