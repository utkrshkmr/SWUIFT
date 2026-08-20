# Contributing to SWUIFT

Contributions for research and academic use are welcome.

## Development setup

Use Python 3.10 or newer in an isolated environment:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

Before submitting a change, run:

```bash
ruff check .
ruff format --check .
mypy
python scripts/check_public_boundary.py
python -m build packages/core
python -m build packages/cli
```

Add tests for changed behavior and explain any test that cannot be run.

## Contributions and licensing

By submitting a contribution, you represent that you have the right to submit
it and agree that it may be distributed under the license in `LICENSE`. Do not
submit confidential, export-controlled, personal, proprietary, or
third-party-restricted material.

Use focused commits and include a clear description, validation steps, and any
licensing implications in the pull request. Report security issues privately as
described in `SECURITY.md`.
