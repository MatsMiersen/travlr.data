# Agent Guidelines

This repository is organized as a collection of explore-ready datasets for Travlr.

- Keep datasets inside `datasets/<dataset-id>/` with a `data.json` file for the markers and a companion `description.json` containing `id`, `name`, `index`, `title`, `description`, and `markercount` fields.
- Update `README.md` when adding or restructuring datasets so other agents understand the layout.
- Preserve existing JSON structures; prefer non-destructive edits and document any format changes in the dataset description.
- Run lightweight checks (formatting, counts) relevant to any dataset you touch and record them in your final summary.
