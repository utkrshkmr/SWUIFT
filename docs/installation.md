# Installation

Verify downloaded files before opening them. See [Verify a release](verification.md).
Read the [complete SWUIFT license](license.md) before running the software.

## Windows

### x64 installer

1. Download the versioned Windows x64 installer from [Downloads](downloads.md).
2. Verify its SHA-256 digest and the signed checksum manifest.
3. Double-click the installer and follow the prompts.
4. Launch **SWUIFT** from the Start menu.

### ARM64 archive

1. Download and verify the Windows ARM64 archive.
2. Extract the complete archive to a user-writable folder.
3. Run `SWUIFT.exe` inside the extracted `SWUIFT` folder. Keep the bundled
   files together.

Windows may display a reputation warning before a newly published application
has established reputation. Confirm the filename and verified digest; do not
bypass a signature or digest mismatch.

## macOS

The packaged build targets Apple silicon (arm64).

1. Download and verify the versioned `.dmg`.
2. Open it and drag **SWUIFT.app** to **Applications**.
3. Open **SWUIFT** from Applications.

If macOS blocks first launch, open **System Settings → Privacy & Security** and
review the message. Proceed only if the package digest and publisher identity
match the release record. Intel Macs do not have a promised packaged build.

## Linux CLI and source installation

Python 3.10 or newer is required. From a versioned source archive or an exact
release checkout:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
swuift --help
```

Linux is supported through the command-line interface. SWUIFT does not publish
or support a Linux desktop application; desktop releases are limited to macOS
and Windows.

## Source installation on PowerShell

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
swuift --help
```

## Source installation on macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
swuift --help
```

Use a fresh environment for each released SWUIFT version. Do not mix packages
from different checkouts.

## Local license file

- Source checkouts keep the authoritative file at `<SWUIFT_ROOT>/LICENSE`.
- Installed Python wheels keep it under the distribution metadata
  `swuift-<version>.dist-info/licenses/LICENSE`.
- Desktop bundles include `LICENSE` in their internal resource directory.

The desktop startup dialog and CLI prompt display the exact absolute path used
on the current machine. SWUIFT fails closed if that file is missing or unreadable.
