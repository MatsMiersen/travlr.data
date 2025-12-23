# travlr.data

Agentic environment for TRAVLR's explore section. Datasets are organized by folder to keep marker data and metadata together for the explore experience.

## Structure
- `AGENTS.md` — working instructions for maintaining the explore datasets.
- `datasets/<dataset-id>/data.json` — dataset markers or geometries.
- `datasets/<dataset-id>/description.json` — dataset metadata (`id`, `name`, `index`, `title`, `description`, `markercount`).
- `tools/` — helper scripts for dataset maintenance and asset management.

## Explore functions
Explore-ready datasets grouped by theme.

| Theme | Dataset | ID | Markers | Image | Icon | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Culture | Traditional Dishes and Origins | `traditional_food` | 800 | ![Traditional Food](datasets/traditional_food/assets/images/traditional_food.webp) | <div style="display:flex; gap:4px; align-items:center;"><img src="datasets/traditional_food/assets/icons/traditional_food_blk.png" alt="Traditional Food Icon" width="24" height="24"></div> | Iconic recipes mapped to the venues where they originated with confidence notes. |
| Culture | UNESCO World Heritage Sites – Human | `unesco-human` | 849 | ![UNESCO Human Sites](datasets/unesco-human/assets/images/unesco-human.webp) | <div style="display:flex; gap:4px; align-items:center;"><img src="datasets/unesco-human/assets/icons/unesco-human_blk.png" alt="UNESCO Human Icon" width="24" height="24"></div> | Human-made heritage sites with marker confidence values. |
| Culture | World Pyramids | `pyramids` | 122 | ![Pyramids](datasets/pyramids/assets/images/pyramids.webp) | <div style="display:flex; gap:4px; align-items:center;"><img src="datasets/pyramids/assets/icons/pyramids_blk.png" alt="Pyramids Icon" width="24" height="24"></div> | Ancient through modern pyramids. |
| Culture | Alien & UFO Landmarks | `alien_world` | 15 | — | — | UFO sightings, memorials, and alien-themed landmarks rooted in enthusiast subculture. |
| Culture | Reddit Travel Locations | `reddit-travel-locations` | 26,479 | ![Reddit Travel Locations](datasets/reddit-travel-locations/assets/images/reddit-travel-locations.webp) | <div style="display:flex; gap:4px; align-items:center;"><img src="datasets/reddit-travel-locations/assets/icons/reddit-travel-locations_blk.png" alt="Reddit Travel Icon" width="24" height="24"></div> | Crowd-sourced travel tips and places to visit. |
| Nature | UNESCO World Heritage Sites – Natural | `unesco-nature` | 203 | ![UNESCO Natural Sites](datasets/unesco-nature/assets/images/unesco-nature.webp) | <div style="display:flex; gap:4px; align-items:center;"><img src="datasets/unesco-nature/assets/icons/unesco-nature_blk.png" alt="UNESCO Natural Icon" width="24" height="24"></div> | Natural heritage sites. |
| Nature | Meteorite Landings | `meteorites` | 45,716 | ![Meteorites](datasets/meteorites/assets/images/meteorites.webp) | <div style="display:flex; gap:4px; align-items:center;"><img src="datasets/meteorites/assets/icons/meteor_glo.png" alt="Meteorites Globe Icon" width="24" height="24"><img src="datasets/meteorites/assets/icons/meteor_mono.png" alt="Meteorites Mono Icon" width="24" height="24"><img src="datasets/meteorites/assets/icons/meteor_sat.png" alt="Meteorites Satellite Icon" width="24" height="24"><img src="datasets/meteorites/assets/icons/meteor_streets.png" alt="Meteorites Streets Icon" width="24" height="24"></div> | Global meteorite strike records. |
| Nature | Earthquakes | `earthquakes` | 6,107 | ![Earthquakes](datasets/earthquakes/assets/images/earthquakes.webp) | <div style="display:flex; gap:4px; align-items:center;"><img src="datasets/earthquakes/assets/icons/earthquakes_blk.png" alt="Earthquakes Icon" width="24" height="24"></div> | Worldwide earthquake events with magnitudes, felt reports, timestamps, and tsunami flags. |
| Nature | Iconic Waterfalls | `waterfalls` | 1,100 | ![Waterfalls](datasets/waterfalls/assets/images/waterfalls.webp) | <div style="display:flex; gap:4px; align-items:center;"><img src="datasets/waterfalls/assets/icons/waterfalls_blk.png" alt="Waterfalls Icon" width="24" height="24"></div> | Waterfalls with height and confidence factors. |
| Nature | Volcanoes | `vulcanoes` | 425 | ![Volcanoes](datasets/vulcanoes/assets/images/vulcanoes.webp) | <div style="display:flex; gap:4px; align-items:center;"><img src="datasets/vulcanoes/assets/icons/vulcanoes_blk.png" alt="Volcanoes Icon" width="24" height="24"></div> | Volcano locations with supporting details. |
| Transport | Global Airports | `airports` | 10,352 | — | — | Worldwide airports and heliports with codes, time zones, and flightability flags. |
| Transport | Global Cities | `cities` | 9,639 | — | — | City points with translations, time zones, and airport readiness flags. |
| Fiction | Lord of the Rings Filming Locations | `lotr-locations` | 131 | ![LOTR Locations](datasets/lotr-locations/assets/images/lotr-locations.webp) | <div style="display:flex; gap:4px; align-items:center;"><img src="datasets/lotr-locations/assets/icons/lotr-locations_blk.png" alt="LOTR Icon" width="24" height="24"></div> | Filming locations for Peter Jackson's trilogy. |
| Fiction | Star Wars Filming & Story Locations | `star-wars-locations` | 62 | ![Star Wars Locations](datasets/star-wars-locations/assets/images/star-wars-locations.webp) | <div style="display:flex; gap:4px; align-items:center;"><img src="datasets/star-wars-locations/assets/icons/star-wars-locations_blk.png" alt="Star Wars Icon" width="24" height="24"></div> | Filming sites and in-universe anchors. |
| Fiction | Dune Filming Locations | `dune-locations` | 106 | — | — | Real deserts, city-scale backlots, and interior soundstages explicitly shown in *Dune* (2021). |
| Fiction | Harry Potter Filming Locations | `harry-potter-locations` | 74 | ![Harry Potter Locations](datasets/harry-potter-locations/assets/images/harry-potter-locations.webp) | <div style="display:flex; gap:4px; align-items:center;"><img src="datasets/harry-potter-locations/assets/icons/harry-potter-locations_blk.png" alt="Harry Potter Icon" width="24" height="24"></div> | Locations used across the film series. |
| Fiction | Game of Thrones Filming Locations | `game-of-thrones-locations` | 300 | ![Game of Thrones Locations](datasets/game-of-thrones-locations/assets/images/game-of-thrones-locations.webp) | <div style="display:flex; gap:4px; align-items:center;"><img src="datasets/game-of-thrones-locations/assets/icons/game-of-thrones-locations_blk.png" alt="Game of Thrones Icon" width="24" height="24"></div> | Filming sites with confidence scores. |
| Fiction | The Last of Us Filming Locations | `last-of-us-locations` | 100 | — | — | Alberta filming sites for the HBO series with per-location notes. |
| Fiction | Breaking Bad Filming Locations | `breaking-bad-locations` | 222 | — | — | Albuquerque and New Mexico shoots with per-location notes. |
| Fiction | James Bond Filming & Story Locations | `james-bond-locations` | 62 | ![James Bond Locations](datasets/james-bond-locations/assets/images/james-bond-locations.webp) | <div style="display:flex; gap:4px; align-items:center;"><img src="datasets/james-bond-locations/assets/icons/james-bond-locations_blk.png" alt="James Bond Icon" width="24" height="24"></div> | Mix of filming sites and in-universe anchors with confidence factors. |
| Fiction | Pirates of the Caribbean Ports & Coastlines | `pirates-caribbean-coasts` | 108 | — | — | Real-world ports, islands, and coastal vistas seen across the film series. |
| Fiction | Indiana Jones Filming Locations | `indiana-jones-locations` | 58 | — | — | Key filming locations spanning the adventure series. |
| Fiction | Assassin's Creed Real-World Locations | `assassins-creed-locations` | 263 | ![Assassin's Creed Locations](datasets/assassins-creed-locations/assets/images/assassins-creed-locations.webp) | <div style="display:flex; gap:4px; align-items:center;"><img src="datasets/assassins-creed-locations/assets/icons/assassins-creed-locations_blk.png" alt="Assassin's Creed Icon" width="24" height="24"></div> | Historical sites and analogs from the franchise. |
| Fiction | Fallout Explorable Locations | `fallout-explore` | 350 | ![Fallout Locations](datasets/fallout-explore/assets/images/fallout-explore.webp) | <div style="display:flex; gap:4px; align-items:center;"><img src="datasets/fallout-explore/assets/icons/fallout-explore_blk.png" alt="Fallout Icon" width="24" height="24"></div> | Fallout locales mapped to real-world coordinates with confidence ratings. |

## Polygon sets
Boundary and region geometries for polygon-based exploration.

| Dataset | ID/Source | Features | Notes |
| --- | --- | --- | --- |
| Ancient Empires Peak Extents | `ancient-empires` | 14 | MultiPolygon outlines for major empires at their peak reach. |
| Country and US Bounding Boxes | `country-bounds` | 254 | Bounding boxes for global countries and U.S. regions. |
| Indigenous & Community Conserved Areas | `indigenous_people` | 24 | ICCA Registry polygons highlighting Indigenous and community stewarded territories. |
| United States Feature Collection | `us-states` | 52 | U.S. state and territory polygons. |
| Time Zones | `time-zones` | Shapefile | Natural Earth 1:10m time zone polygons (feature count depends on importer). |
| Tectonic Plates | `tectonic-plates` | 54 | PB2002 tectonic plate boundaries in GeoJSON format. |

## Adding a dataset
1. Create `datasets/<dataset-id>/` and place the source JSON in `data.json` without altering its structure unless necessary.
2. Add a `description.json` with the required metadata fields and updated `markercount`.
3. Update this README to include the new dataset summary.

## Tools
- `tools/download_images.py` — download images from an `images.txt` manifest. Use `--dataset <id>` to drop images into `datasets/<id>/assets/images` (or override with `--out`). The script commits changes by default and only pushes when `--push` is provided. Requires the `requests` package.

## Coming Soon: New Explore Datasets

| Pillar | Dataset | Dataset ID | Core concept | Probable scale (features) |
|---|---|---|---|---|
| Nature | Unique Geological Formations | `unique-geology` | Rare / visually striking formations shaped by deep time | ≈ 500–2,000 |
| Nature | Extreme Geography Points | `geographic-extremes` | The physical limits of habitation & natural conditions | ≈ 300–1,200 |
| History | Famous Journeys & Expeditions | `historic-expeditions` | Routes of influential journeys that changed understanding | ≈ 100–800 |
| Nature | Seasonal Nature Phenomena | `seasonal-phenomena` | “When-to-go” locations: blooms, foliage, fireflies, bioluminescence, migrations | ≈ 1,000–10,000 |
| Urbanism / Design | Urban Revolution | `urban-revolution` | Post-industrial transformations and urban reinvention | ≈ 1,000–12,000 |
| Culture | Pilgrimage Trails | `pilgrimage-trails` | Living pilgrimage networks (routes + rest nodes), still walked today | ≈ 500–8,000 |
| Culture | Craft Terroirs | `craft-terroirs` | Regions where material + tradition create “only-here” crafts | ≈ 3,000–25,000 |
| Fiction | The Witcher (Netflix) | `witcher-locations` | Real-world filming locations as depicted on screen across seasons | ≈ 120–400 |
| Fiction | Jurassic Park / World | `jurassic-locations` | Real islands, coasts, forests used and depicted in the franchise | ≈ 50–180 |
| Fiction | The Matrix | `matrix-locations` | Real urban locations and infrastructures shown as themselves or unnamed cities | ≈ 70–200 |
| Fiction | Blade Runner (1982 / 2049) | `blade-runner-locations` | Real city locations and structures visible in-film | ≈ 40–120 |
| Fiction | Star Trek (Earth-based scenes) | `star-trek-earth-locations` | Real Earth locations depicted on screen (films + series) | ≈ 80–300 |
| Fiction | Mission: Impossible | `mission-impossible-locations` | On-location set pieces depicted directly in the films | ≈ 120–400 |
| Fiction | Narcos (Netflix) | `narcos-locations` | Real cities, neighborhoods, and landscapes depicted on screen | ≈ 120–300 |
| Fiction | Peaky Blinders | `peaky-blinders-locations` | Industrial-era locations depicted in the series | ≈ 80–200 |
| Fiction | Sherlock (BBC) | `sherlock-locations` | Real London locations depicted as themselves or story settings | ≈ 70–180 |
| Fiction | The Dark Knight Trilogy | `dark-knight-locations` | Real urban locations depicted on screen across the trilogy | ≈ 90–220 |
| Fiction | The Bourne Series | `bourne-locations` | Real European & global city locations depicted on screen | ≈ 120–350 |
| Fiction | The Crown | `the-crown-locations` | Real palaces, estates, cities, and interiors depicted on screen | ≈ 150–400 |
| Fiction | Vikings | `vikings-locations` | Real-world locations depicted across the series | ≈ 120–300 |
| Fiction | The Last of Us | `last-of-us-locations` | Real urban and rural locations depicted on screen | ≈ 80–200 |
| Fiction | Call of Duty (Real-World Campaign Maps) | `call-of-duty-locations` | Real cities and regions depicted in campaign missions | ≈ 80–200 |
| Fiction | Watch Dogs | `watch-dogs-locations` | Real cities recreated and depicted as themselves | ≈ 60–150 |
| Fiction | Grand Theft Auto (Real-World References Only) | `gta-real-locations` | Real locations explicitly named or depicted (limited, verified only) | ≈ 30–80 |
| Fiction | Tomb Raider (Reboot Trilogy) | `tomb-raider-locations` | Real archaeological and urban locations depicted on screen | ≈ 60–150 |
