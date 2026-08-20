# Citation, DOI, and license

## Zenodo DOI model

Use two DOI levels:

- **Concept DOI:** resolves to the software project and always points to its
  newest archived release.
- **Version DOI:** resolves to one immutable archived release.

For reproducible research, cite the **version DOI** that matches the software
actually used. The project page may also display the concept DOI.

| Record | Published value |
|---|---|
| Concept DOI | |
| Concept record | |
| Current version DOI | |
| Current version record | |

These fields remain empty until Zenodo has minted the records. Do not
preconstruct or guess DOI values.

## Suggested software citation

Until the archival metadata is published:

```text
Nima Masoudvaziri, Fernando Szasdi Bardales, Utkarsh Kumar, and Negar
Elhami-Khorasani. (YEAR). SWUIFT: Streamlined Wildland–Urban Interface Fire
Tracing (Version VERSION) [Computer software].
```

The current citation metadata identifies version `1.0.0`; confirm the version,
year, creator list, and DOI against the release's `CITATION.cff` or Zenodo
record. Also report the full commit SHA, input-bundle identifier, simulation
window, and seeds in the methods or data-availability statement.

## BibTeX template

```bibtex
@software{swuift_VERSION,
  author    = {Masoudvaziri, Nima and Szasdi Bardales, Fernando and
               Kumar, Utkarsh and Elhami-Khorasani, Negar},
  title     = {SWUIFT: Streamlined Wildland--Urban Interface Fire Tracing},
  year      = {<YEAR>},
  version   = {<VERSION>},
  publisher = {},
  doi       = {},
  url       = {}
}
```

## Research and academic source-available license

SWUIFT is source-available, not open source. It is offered under the
restrictive **SWUIFT Research and Academic Use License** distributed with the
release.

- Source and binary use, modification, and redistribution are permitted solely
  for research and/or academic use, subject to retaining the required
  copyright, conditions, and disclaimer.
- Commercial use—including commercial redistribution, paid consulting,
  commercial contract research, and operational decision support—is prohibited
  unless separately licensed in writing.
- Specified institutional and contributor names may not be used for
  endorsement without prior written permission.
- The license includes a limited patent non-assert covenant that terminates
  upon use outside the permitted purpose.
- The signed or packaged license text controls if this summary differs from it.

Before using or sharing SWUIFT, read the
[complete license text](license.md). The same authoritative `LICENSE` file is
included in the repository root and in every packaged application.

For commercial licensing, contact `techtransfer@buffalo.edu`. For scientific
questions, contact Prof. Negar Elhami-Khorasani at `negarkho@buffalo.edu`.
