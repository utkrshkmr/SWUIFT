# SWUIFT

**Streamlined Wildland-Urban Interface Fire Tracing**

SWUIFT is research software for studying vegetation fire, wind-driven
firebrands, radiant heat, and structure hardening on a gridded
wildland–urban interface. It provides a desktop application and a command-line
interface for reproducible batch runs.

> SWUIFT is not an operational forecasting, evacuation, emergency-response, or
> life-safety system. Results require expert interpretation.

## Documentation

The polished user guide is built with MkDocs Material:

- [Overview](docs/index.md)
- [Downloads and immutable release placeholders](docs/downloads.md)
- [Windows/macOS desktop and cross-platform CLI installation](docs/installation.md)
- [Quick Start](docs/quick-start.md)
- [Desktop GUI](docs/gui.md)
- [CLI](docs/cli.md)
- [Input schema](docs/input-schema.md)
- [Marshall 121-state tutorial](docs/marshall-tutorial.md)
- [Expected outputs](docs/outputs.md)
- [SHA-256 and signature verification](docs/verification.md)
- [Citation, Zenodo DOI model, and license](docs/citation-license.md)
- [Complete license text](docs/license.md)
- [Troubleshooting and contact](docs/troubleshooting.md)

Repository, release, DOI, checksum, and signing-key values marked **FUTURE
PUBLICATION VALUE** are intentional placeholders and must be replaced by the
maintainers before public release.

## Install from source

Python 3.10 or newer is required.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
swuift --help
```

Launch the desktop application:

```bash
cd apps/desktop
python swuift_app.py
```

## Build the documentation

```bash
python -m pip install -r docs/requirements.txt
mkdocs serve
```

For a strict production build:

```bash
mkdocs build --strict
```

## License and citation

SWUIFT is source-available under a restrictive research and academic use
license supplied with each release; it is not open source. See
[the complete license](LICENSE) and
[citation and license guidance](docs/citation-license.md). Commercial licensing:
`techtransfer@buffalo.edu`. Scientific questions: Prof. Negar
Elhami-Khorasani, `negarkho@buffalo.edu`.
