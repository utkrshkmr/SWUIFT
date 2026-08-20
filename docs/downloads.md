# Downloads

Official releases will be published as immutable, versioned assets. Do not use
temporary workflow artifacts for archival or cited research.

!!! danger "Links not yet published"
    Every value in angle brackets below is a **FUTURE PUBLICATION VALUE**.
    Maintainers must replace it with a real repository, tag, filename, and
    digest before announcing a release.

## Desktop packages

| Platform | Package | Immutable download |
|---|---|---|
| Windows x64 | Signed installer (`.exe`) | `<FUTURE_GITHUB_RELEASE_URL>/download/<VERSION>/<WINDOWS_X64_INSTALLER>` |
| Windows ARM64 | Application bundle (`.zip`) | `<FUTURE_GITHUB_RELEASE_URL>/download/<VERSION>/<WINDOWS_ARM64_ARCHIVE>` |
| macOS Apple silicon | Disk image (`.dmg`) | `<FUTURE_GITHUB_RELEASE_URL>/download/<VERSION>/<MACOS_ARM64_DMG>` |

Desktop packages are published only for Windows and macOS. Linux users can use
the CLI from a versioned source release; no Linux desktop application is built
or supported.

## Release records

- Release page: `<FUTURE_IMMUTABLE_RELEASE_URL>`
- Source at release tag: `<FUTURE_REPOSITORY_URL>/tree/<VERSION_TAG>`
- Source at exact commit: `<FUTURE_REPOSITORY_URL>/tree/<FULL_COMMIT_SHA>`
- Checksums: `<FUTURE_GITHUB_RELEASE_URL>/download/<VERSION>/SHA256SUMS`
- Detached checksum signature:
  `<FUTURE_GITHUB_RELEASE_URL>/download/<VERSION>/SHA256SUMS.asc`
- Signing key: `<FUTURE_SIGNING_KEY_URL>`
- Archived release record:

An immutable link must contain a release tag, exact commit, or version DOI.
Links to a moving branch such as `main`, to “latest,” or to a workflow run are
not suitable for reproducibility.

## Before running

1. Download the package and both verification files.
2. Follow [SHA-256 and signature verification](verification.md).
3. Record the version, full commit SHA, input bundle version, and version DOI
   with your research notes.
4. Continue to [installation](installation.md).
