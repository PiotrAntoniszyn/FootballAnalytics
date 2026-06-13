# FootballAnalytics

A collection of football analytics notebooks built while completing David Sumpter's **[Mathematical Modelling of Football](https://www.uu.se/en/study/syllabus?query=44017)** course (Uppsala University). The repo is a historical snapshot — it hasn't been actively maintained since the course ended, but the notebooks run end-to-end as written.

---

## Contents

| File | What it does |
|---|---|
| `Pass Flow map.ipynb` | Aggregates a team's passes into a directional flow map overlaid on a pitch — shows dominant passing corridors and build-up structure |
| `Player Passes.ipynb` | Filters and plots an individual player's passing network for a single match |
| `Progressive passes.ipynb` | Identifies and visualises progressive passes (carrying the ball significantly closer to goal) from FBref data |
| `Radar chart.ipynb` | Builds a radar/spider chart comparing a player's percentile stats across multiple metrics |
| `radarChartCreator.py` | Reusable module that extracts the radar chart logic from the notebook into a callable script |
| `PlayerDatabaseChartCreator.ipynb` | Loads player data from the FBref export and generates radar charts in batch for a squad |
| `Dashboard/` | Prototype dashboard combining the visualisations above |
| `web/` | Web wrapper for sharing outputs |

---

## Data

Player and match data sourced from **[FBref](https://fbref.com)** (Football Reference) — the `.xls` files in the root are raw FBref exports. The pass-level notebooks use **StatsBomb open data** via the `mplsoccer` loader.

---

## Libraries

```
mplsoccer
pandas
matplotlib
numpy
```

---

## Context

The course, taught by David Sumpter (author of [Soccermatics](https://www.bloomsbury.com/uk/soccermatics-9781472924148/)), covers the mathematical foundations behind modern football analytics — pass networks, player similarity, spatial analysis and statistical modelling. The notebooks here are my implementations of the course exercises, with some extensions to the visualisation layer.
