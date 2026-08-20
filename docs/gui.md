# Desktop GUI

The desktop application combines six configuration tabs, a live simulation
log, and a sequential job queue.

## Standard workflow

1. Select all inputs.
2. Set the simulation window and model parameters.
3. Choose output options.
4. Click **Add to Queue** to snapshot the current settings.
5. Add more parameter variants if needed.
6. Click **Run All** and monitor the queue.

## Configuration tabs

### Data Inputs

Select the ten required `.mat` or `.csv` inputs. The GUI validates that every
path exists before a job can be queued. See [Input schema](input-schema.md).

### Grid & Time

Start and end are inclusive. Both must align to the fixed five-minute timestep.
The panel reports the duration and calculated number of states.

### Radiation

- **Ignition Threshold (W/m²):** radiant-energy threshold for ignition.
- **Radiation Reduction Factor:** multiplier applied before the ignition check;
  `1.0` means no reduction.

### Firebrands

The wind coefficient and longitudinal/transverse standard deviations control
wind-driven transport and stochastic scatter.

### Hardening & Seeds

Radiation and spotting hardening are percentages. Random-number seeds make a
configuration reproducible when software, inputs, and platform are also held
constant. Record both seeds in publications.

### Output Settings

- **Output Folder:** base folder for timestamped run directories.
- **Generate Video / GIF:** creates animations after simulation.
- **Frame DPI:** resolution of rendered frames.
- **Dump Interval:** saves full state every N steps; `0` disables dumps.
- **Dump as CSV:** human-readable dumps, typically larger and slower.
- **Lazy Wind:** lowers memory use by reading wind slices on demand.
- **Radiation/spotting CSV:** optional per-step diagnostic exports.

## Queue controls

| Control | Effect |
|---|---|
| **Add to Queue** | Validate and snapshot the current configuration |
| **Run All** | Run pending jobs sequentially |
| **Cancel** | Stop the current job or queue after confirmation |
| **Remove Selected** | Remove a pending job |
| **Duplicate Selected** | Copy a job for a parameter variant |
| **Clear Queue** | Remove jobs when no simulation is active |

The queue reports status, phase, elapsed time, estimated remaining time, and
the run output directory. A failed row can be opened to view its error.

## Save and restore settings

Use **File → Save Settings as JSON…** (`Ctrl+S`) and **File → Load Settings
from JSON…** (`Ctrl+O`). Saved settings contain paths and model parameters, but
not the input files themselves. Review paths after moving a settings file to
another computer.

## Reproducibility checklist

- Keep the released software version and full commit SHA.
- Keep the input-bundle identifier and checksums.
- Save the settings JSON.
- Preserve `run_params.json` and `run_log.txt`.
- Record platform, seed values, and whether lazy wind was enabled.
