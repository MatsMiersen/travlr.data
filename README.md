# travlr.explore

Agentic environment for TRAVLR's explore section. Datasets are organized by folder to keep marker data and metadata together for the explore experience.

## Structure
- `AGENTS.md` — working instructions for maintaining the explore datasets.
- `datasets/<dataset-id>/data.json` — dataset markers or geometries.
- `datasets/<dataset-id>/description.json` — dataset metadata (`id`, `name`, `index`, `title`, `description`, `markercount`).
- `tools/` — helper scripts for dataset maintenance and asset management.

## Explore functions
Explore-ready datasets grouped by theme.

| Theme | Dataset | ID | Markers | Notes |
| --- | --- | --- | --- | --- |
| Culture | Traditional Dishes and Origins | `traditional_food` | 800 | Iconic recipes mapped to the venues where they originated with confidence notes. |
| Culture | UNESCO World Heritage Sites – Human | `unesco-human` | 849 | Human-made heritage sites with marker confidence values. |
| Culture | World Pyramids | `pyramids` | 122 | Ancient through modern pyramids. |
| Culture | Reddit Travel Locations | `reddit-travel-locations` | 26,479 | Crowd-sourced travel tips and places to visit. |
| Nature | UNESCO World Heritage Sites – Natural | `unesco-nature` | 203 | Natural heritage sites. |
| Nature | Meteorite Landings | `meteorites` | 45,716 | Global meteorite strike records. |
| Nature | Iconic Waterfalls | `waterfalls` | 1,100 | Waterfalls with height and confidence factors. |
| Nature | Volcanoes | `vulcanoes` | 425 | Volcano locations with supporting details. |
| Fiction | Lord of the Rings Filming Locations | `lotr-locations` | 131 | Filming locations for Peter Jackson's trilogy. |
| Fiction | Star Wars Filming & Story Locations | `star-wars-locations` | 62 | Filming sites and in-universe anchors. |
| Fiction | Harry Potter Filming Locations | `harry-potter-locations` | 74 | Locations used across the film series. |
| Fiction | Game of Thrones Filming Locations | `game-of-thrones-locations` | 300 | Filming sites with confidence scores. |
| Fiction | James Bond Filming & Story Locations | `james-bond-locations` | 62 | Mix of filming sites and in-universe anchors with confidence factors. |
| Fiction | Assassin's Creed Real-World Locations | `assassins-creed-locations` | 263 | Historical sites and analogs from the franchise. |
| Fiction | Fallout Explorable Locations | `fallout-explore` | 350 | Fallout locales mapped to real-world coordinates with confidence ratings. |

## Polygon sets
Boundary and region geometries for polygon-based exploration.

| Dataset | ID/Source | Features | Notes |
| --- | --- | --- | --- |
| Country and US Bounding Boxes | `country-bounds` | 254 | Bounding boxes for global countries and U.S. regions. |
| United States Feature Collection | `us-states` | 52 | U.S. state and territory polygons. |
| Time Zones | `ne_10m_time_zones.shp` | Shapefile | Natural Earth 1:10m time zone polygons (feature count depends on importer). |
| Tectonic Plates | `PB2002_plates.json` | 54 | PB2002 tectonic plate boundaries in GeoJSON format. |

## Adding a dataset
1. Create `datasets/<dataset-id>/` and place the source JSON in `data.json` without altering its structure unless necessary.
2. Add a `description.json` with the required metadata fields and updated `markercount`.
3. Update this README to include the new dataset summary.

## Tools
- `tools/download_images.py` — download images from an `images.txt` manifest. Use `--dataset <id>` to drop images into `datasets/<id>/assets/images` (or override with `--out`). The script commits changes by default and only pushes when `--push` is provided. Requires the `requests` package.
