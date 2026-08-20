# Marshall tutorial

This walkthrough configures the requested Marshall window:

- **UTC convention:** `2021-12-30T18:00Z` through `2021-12-31T04:00Z`
- **Mountain Standard Time (UTC−07:00):** 11:00 through 21:00 on
  December 30, 2021
- **Timestep:** 5 minutes
- **Duration:** 10 hours = 600 minutes
- **Inclusive states:** `600 / 5 + 1 = 121`

!!! note "Timezone entry"
    Enter local wall times `2021-12-30 11:00` and `2021-12-30 21:00` with
    `America/Denver`. SWUIFT converts this interval to the validated UTC window
    internally and displays results in Mountain Standard Time. See
    [Timezone codes](timezones.md).

## 1. Prepare the input directory

Obtain the authorized Marshall input bundle from its official distributor.
The extracted interface needs these ten logical inputs:

```text
<MARSHALL_INPUT_DIR>/
├── wildland_fire_matrix.mat
├── domain_matrix.mat
├── binary_cover_landcover.mat
├── homes_matrix.mat
├── latitude.mat
├── longitude.mat
├── radiation_matrix.mat
├── spotting_matrix.mat
├── water_matrix.mat
└── wind.mat
```

Names here describe the tutorial layout; the required variables and shapes are
authoritative and listed in [Input schema](input-schema.md). Verify the bundle
checksums supplied by its distributor before use.

## 2. Choose an external output directory

Create a writable location with enough space for frames and animations:

```bash
mkdir -p "$HOME/swuift-results"
```

The CLI rejects output inside its installed package tree.

## 3. Run with the CLI

Replace `<MARSHALL_INPUT_DIR>` and `<OUTPUT_DIR>` with absolute paths:

```bash
swuift \
  --job-name marshall_20211230_121_steps \
  --fire-prog <MARSHALL_INPUT_DIR>/wildland_fire_matrix.mat \
  --domains <MARSHALL_INPUT_DIR>/domain_matrix.mat \
  --landcover <MARSHALL_INPUT_DIR>/binary_cover_landcover.mat \
  --homes <MARSHALL_INPUT_DIR>/homes_matrix.mat \
  --lat <MARSHALL_INPUT_DIR>/latitude.mat \
  --lon <MARSHALL_INPUT_DIR>/longitude.mat \
  --harden-rad-map <MARSHALL_INPUT_DIR>/radiation_matrix.mat \
  --harden-spo-map <MARSHALL_INPUT_DIR>/spotting_matrix.mat \
  --water <MARSHALL_INPUT_DIR>/water_matrix.mat \
  --wind <MARSHALL_INPUT_DIR>/wind.mat \
  --grid-size 10 \
  --t-start "2021-12-30 11:00" \
  --t-end "2021-12-30 21:00" \
  --timezone America/Denver \
  --harden-rad 70 \
  --harden-spo 70 \
  --rad-ig-thresh 14000 \
  --rad-decay 1.0 \
  --brand-wind-coef 30 \
  --brand-wind-sd 0.3 \
  --brand-wind-sd-lat 4.85 \
  --seed-harden 123456 \
  --seed-spread 10 \
  --lazy-wind \
  --output-dir <OUTPUT_DIR> \
  --frame-dpi 150 \
  --dump-every 0 \
  --no-dump-csv
```

The numeric settings above are an explicit tutorial configuration, not a
claim that they are universally appropriate. Cite and justify settings used
for research conclusions.

## 4. Configure the desktop GUI

1. Select the same ten files on **Data Inputs**.
2. On **Grid & Time**, choose `America/Denver`, set the start to
   `2021-12-30 11:00`, and set the end to `2021-12-30 21:00`.
3. Confirm the interface reports **121** inclusive states at five-minute
   spacing.
4. Enter the same radiation, firebrand, hardening, and seed values.
5. Select the output folder and enable **Lazy Wind** if memory is constrained.
6. Click **Add to Queue**, then **Run All**.

## 5. Confirm the run

Open the newly created `marshall_20211230_121_steps_<timestamp>/` directory.
Check `run_params.json` before interpreting results:

- `timezone` is `America/Denver`;
- local 11:00–21:00 corresponds to `2021-12-30T18:00:00Z` through
  `2021-12-31T04:00:00Z`;
- `max_steps` is `121`;
- the grid shape matches the Marshall bundle;
- input paths, seeds, and requested output switches are correct.

Then review `run_log.txt` for completion or warnings. Preserve those two files
with any reported figures or derived datasets.
