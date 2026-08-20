# Citation, DOI, and license

## Zenodo DOI model

Use two DOI levels:

- **Concept DOI:** resolves to the software project and always points to its
  newest archived release.
- **Version DOI:** resolves to one immutable archived release.

For reproducible research, cite the **version DOI** that matches the software
actually used. The project page may also display the concept DOI.

| Record | FUTURE PUBLICATION VALUE |
|---|---|
| Concept DOI | `<FUTURE_ZENODO_CONCEPT_DOI>` |
| Concept record | `<FUTURE_ZENODO_CONCEPT_RECORD_URL>` |
| Current version DOI | `<FUTURE_ZENODO_VERSION_DOI>` |
| Current version record | `<FUTURE_ZENODO_VERSION_RECORD_URL>` |

These placeholders must be replaced only after Zenodo has minted the records.
Do not preconstruct or guess DOI values.

## Suggested software citation

Until the archival metadata is published:

```text
Elhami-Khorasani, N. (YEAR). SWUIFT: Simulating Wildfire–Urban Interface
Fire Transmission (Version VERSION) [Computer software].
Zenodo. https://doi.org/<FUTURE_ZENODO_VERSION_DOI>
```

The current citation metadata identifies version `1.0.0`; confirm the version,
year, creator list, and DOI against the release's `CITATION.cff` or Zenodo
record. Also report the full commit SHA, input-bundle identifier, simulation
window, and seeds in the methods or data-availability statement.

## BibTeX template

```bibtex
@software{swuift_VERSION,
  author    = {Elhami-Khorasani, Negar},
  title     = {SWUIFT: Simulating Wildfire--Urban Interface Fire Transmission},
  year      = {<YEAR>},
  version   = {<VERSION>},
  publisher = {Zenodo},
  doi       = {<FUTURE_ZENODO_VERSION_DOI>},
  url       = {https://doi.org/<FUTURE_ZENODO_VERSION_DOI>}
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

Before using or sharing SWUIFT, read the complete release license:
`<FUTURE_IMMUTABLE_LICENSE_URL>`.

For commercial licensing, contact `techtransfer@buffalo.edu`. For scientific
questions, contact Prof. Negar Elhami-Khorasani at `negarkho@buffalo.edu`.
