# Quick Start

You need a complete, licensed SWUIFT input bundle before beginning. The
software distribution does not imply redistribution rights for third-party
geospatial or wind data.

## Desktop in five steps

1. Open **SWUIFT – Wildfire Spread Simulation**.
2. On **Data Inputs**, select all ten files described in the
   [input schema](input-schema.md).
3. On **Grid & Time**, select the required [IANA timezone](timezones.md), then
   enter local start and end values aligned to five-minute boundaries.
4. On **Output Settings**, choose a writable output folder. Enable **Lazy
   Wind** when memory is limited.
5. Click **Add to Queue**, then **Run All**.

The queue progresses through loading, configuration, simulation, and optional
video generation. When the status is **Done**, use the output directory shown
in the queue.

## CLI in five steps

Activate the environment and confirm the command is available:

```bash
source .venv/bin/activate
swuift --help
```

Create a batch file containing a top-level `jobs` array. Each job needs ten
input paths, explicit model settings, and an output directory:

```json
{
  "jobs": [
    {
      "name": "research_run",
      "fire_prog": "<INPUT_DIR>/wildland_fire_matrix.mat",
      "domains": "<INPUT_DIR>/domain_matrix.mat",
      "landcover": "<INPUT_DIR>/binary_cover_landcover.mat",
      "homes": "<INPUT_DIR>/homes_matrix.mat",
      "lat": "<INPUT_DIR>/latitude.mat",
      "lon": "<INPUT_DIR>/longitude.mat",
      "harden_rad_map": "<INPUT_DIR>/radiation_matrix.mat",
      "harden_spo_map": "<INPUT_DIR>/spotting_matrix.mat",
      "water": "<INPUT_DIR>/water_matrix.mat",
      "wind": "<INPUT_DIR>/wind.mat",
      "grid_size": 10,
      "t_start": "2021-12-30 11:00",
      "t_end": "2021-12-30 21:00",
      "timezone": "America/Denver",
      "harden_rad": 70,
      "harden_spo": 70,
      "rad_ig_thresh": 14000,
      "rad_decay": 1.0,
      "brand_wind_coef": 30,
      "brand_wind_sd": 0.3,
      "brand_wind_sd_lat": 4.85,
      "seed_harden": 123456,
      "seed_spread": 10,
      "lazy_wind": true,
      "output_dir": "<OUTPUT_DIR>",
      "frame_dpi": 150,
      "dump_every": 0,
      "dump_csv": false
    }
  ]
}
```

Replace all angle-bracket placeholders, then run:

```bash
swuift --batch jobs.json
```

Review `run_log.txt` and `run_params.json` first. See [Expected outputs](outputs.md)
for the remaining artifacts and the [Marshall tutorial](marshall-tutorial.md)
for the complete time-window walkthrough.
