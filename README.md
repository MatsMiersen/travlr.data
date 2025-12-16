# travlr.explore

Agentic environment for TRAVLR's explore section. Datasets are organized by folder to keep marker data and metadata together for the explore experience.

## Structure
- `AGENTS.md` — working instructions for maintaining the explore datasets.
- `datasets/<dataset-id>/data.json` — dataset markers or geometries.
- `datasets/<dataset-id>/description.json` — dataset metadata (`id`, `name`, `index`, `title`, `description`, `markercount`).

## Current datasets
1. **Lord of the Rings Filming Locations** (`lotr-locations`) — 131 markers.
2. **Reddit Travel Locations** (`reddit-travel-locations`) — 26,479 markers.
3. **UNESCO World Heritage Sites** (`unesco-sites`) — 1,052 markers.
4. **Country Bounding Boxes** (`country-bounds`) — 202 entries.
5. **Meteorite Landings** (`meteorites`) — 45,716 entries.
6. **Star Wars Filming & Story Locations** (`star-wars-locations`) — 62 markers.
7. **United States Feature Collection** (`us-states`) — 52 features.

## Adding a dataset
1. Create `datasets/<dataset-id>/` and place the source JSON in `data.json` without altering its structure unless necessary.
2. Add a `description.json` with the required metadata fields and updated `markercount`.
3. Update this README to include the new dataset summary.
