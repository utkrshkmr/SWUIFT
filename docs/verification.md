# Verify a release

Release verification has two independent parts:

1. a SHA-256 digest detects a changed or incomplete download;
2. a signature authenticates the checksum manifest against a trusted
   maintainer key.

!!! danger "Future values"
    `<EXPECTED_SHA256>`, `<RELEASE_FILE>`, `<SIGNING_KEY_FINGERPRINT>`, and all
    release URLs are **FUTURE PUBLICATION VALUES**. Obtain them from the
    official immutable release record. Never substitute a value from an
    untrusted mirror.

## Linux

```bash
sha256sum <RELEASE_FILE>
```

Compare the complete output to `<EXPECTED_SHA256>`, or verify the manifest:

```bash
sha256sum --check SHA256SUMS
```

## macOS

```bash
shasum -a 256 <RELEASE_FILE>
```

Compare all 64 hexadecimal characters to `<EXPECTED_SHA256>`.

## Windows PowerShell

```powershell
Get-FileHash .\<RELEASE_FILE> -Algorithm SHA256
```

Compare the full `Hash` value to `<EXPECTED_SHA256>`.

## Verify the signed checksum manifest

Import the public key only after confirming its fingerprint through an
independent official channel:

```bash
gpg --import <SWUIFT_SIGNING_KEY.asc>
gpg --fingerprint <SIGNING_KEY_ID>
```

The fingerprint must exactly match:

```text
<SIGNING_KEY_FINGERPRINT>
```

Then verify the detached signature and checksums:

```bash
gpg --verify SHA256SUMS.asc SHA256SUMS
sha256sum --check SHA256SUMS
```

On macOS, verify the signature with `gpg`, then compare the relevant digest
using `shasum -a 256`. On Windows, GnuPG can verify the signature and
PowerShell can calculate the file digest.

## Failure policy

Do not install or run the package if:

- the calculated digest differs by even one character;
- the signature is bad, missing when the release promises one, or made by an
  unexpected key;
- the key fingerprint cannot be confirmed independently;
- the filename or version differs from the checksum manifest.

Delete the suspect files, download again from the immutable official release,
and contact the maintainers if the mismatch persists. A checksum proves file
identity, not that the software is safe or suitable for a particular use.
