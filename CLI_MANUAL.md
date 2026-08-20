# SWUIFT CLI Manual

The `swuift` command runs one explicit simulation or a sequential JSON batch.

## Install

Python 3.10 or newer is required:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
swuift --help
```

## Run

Single-run mode requires a job name, ten input paths, model parameters, seeds,
wind-loading choice, and output controls:

```bash
swuift \
  --job-name <NAME> \
  --fire-prog <PATH> --domains <PATH> --landcover <PATH> \
  --homes <PATH> --lat <PATH> --lon <PATH> \
  --harden-rad-map <PATH> --harden-spo-map <PATH> \
  --water <PATH> --wind <PATH> \
  --grid-size 10 \
  --t-start "2021-12-30 18:00" \
  --t-end "2021-12-31 04:00" \
  --harden-rad 70 --harden-spo 70 \
  --rad-ig-thresh 14000 --rad-decay 1.0 \
  --brand-wind-coef 30 --brand-wind-sd 0.3 \
  --brand-wind-sd-lat 4.85 \
  --seed-harden 123456 --seed-spread 10 \
  --lazy-wind \
  --output-dir <OUTPUT_DIR> \
  --frame-dpi 150 --dump-every 0 --no-dump-csv
```

Replace all angle-bracket placeholders. The CLI accepts
`YYYY-MM-DD HH:MM`, `YYYY-MM-DDTHH:MM`, or `YYYY-MM-DD HH:MM:SS`; it does not
accept timezone suffixes. Both endpoints must align to five-minute boundaries.

Batch mode reads a non-empty top-level `jobs` array:

```bash
swuift --batch jobs.json
```

The output directory must be writable and outside the installed CLI package
tree. Every run writes `run_log.txt` and `run_params.json`; maps, tables,
frames, animations, and per-step diagnostics depend on output switches.

## Complete documentation

- [CLI options and JSON schema](docs/cli.md)
- [Input schema](docs/input-schema.md)
- [Marshall 121-state tutorial](docs/marshall-tutorial.md)
- [Expected outputs](docs/outputs.md)
- [Troubleshooting and contact](docs/troubleshooting.md)

SWUIFT is source-available under a restrictive research and academic use
license. See [citation and license guidance](docs/citation-license.md).
