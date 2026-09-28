# Data for session 5

Two files per state, derived from the EPA's UCMR 5 occurrence data. The instructors keep the derivation script; every file here can be rebuilt from the EPA release.

## Source

US Environmental Protection Agency, Fifth Unregulated Contaminant Monitoring Rule (UCMR 5) occurrence data, 2023 to 2025, the file `ucmr5-occurrence-data.zip` on the EPA page [Occurrence Data for the Unregulated Contaminant Monitoring Rule](https://www.epa.gov/dwucmr/occurrence-data-unregulated-contaminant-monitoring-rule). The release used is the one on the server on 2026-09-27, dated August 28, 2026 by the server and August 27 by the files inside the zip; the July 2026 data summary inside the zip describes it. The results file, `UCMR5_All.txt`, holds 1,992,002 analytical results, one per row, for 29 PFAS and lithium from every public water system serving more than 3,300 people and a sample of the smaller ones. It is a US government work in the public domain. Cite it as: US EPA, *UCMR 5 Occurrence Data*, accessed 2026-09-27, from the page linked above.

## What was derived

For each of the 57 states and territories with a two-letter code (the EPA Region tribal programs, coded 01 to 10, are left out), the first sampling event (`SE1`) and six of the PFAS: PFBS, PFHxA and PFHxS with a method reporting limit of 0.003 µg/L, PFOA and PFOS at 0.004 µg/L, and PFPeA at 0.003 µg/L. They are the six the archived version of this activity used, among the seven PFAS with the most detections nationally.

### The results file, `states/<ST>_results.csv`

One row per sample, i.e., one sample point on one collection date, in the shape of a laboratory report. The EPA release is already one measurement per row; this wide layout, and the composite identifier, were built from it so that the activity has a table to tidy, which is what a laboratory's export usually needs.

| Column | Meaning |
|---|---|
| `sample_id` | four facts joined by underscores: the public water system id (PWSID), the sample point id, the collection date as YYYY-MM-DD, and the sampling event, `SE1` |
| `PFBS`, `PFHxA`, `PFHxS`, `PFOA`, `PFOS`, `PFPeA` | the result in µg/L as the laboratory reported it, for example `0.0040`, or `< 0.004` for a result below the reporting limit |

Two rules were applied. A sample point that appears under two facility ids on the same date is kept once, with the later row's results: 3,066 samples nationally, about 4% of the first-event results for these six PFAS, and in 393 of them the two rows' results differ. A sample with fewer than six results in the event, which happens when a point was sampled on two dates with the compounds split between them, is left out: 45 samples nationally, in 13 states. So every cell of a results file is a value or a below-limit code.

### The sample table, `states/<ST>_samples.csv`

The sample table: one row per sample point.

| Column | Meaning |
|---|---|
| `pwsid` | public water system id, the key shared with `sample_id` |
| `system_name` | the system's name as the EPA lists it |
| `size_category` | `L` for a system serving more than 10,000 people, `S` for a smaller one |
| `facility_id` | the EPA id of the treatment facility the sample point belongs to; for a point reported under two facilities, the later one |
| `facility_water_type` | `GW` groundwater, `SW` surface water, `MX` mixed, `GU` groundwater under the influence of surface water; a sample point reported under two types (64 of 25,000 nationally) carries the more common one |
| `sample_point_id` | the sample point id, the second key; read it as text, since some are all digits with leading zeros |
| `epa_region` | the EPA region number |
| `state` | the two-letter code |

Every sample point in UCMR 5 is an entry point to the distribution system, so the sample table has no sample point type column.

## Washington and your state

Section 1 of the activity uses `WA_results.csv` and `WA_samples.csv`. Section 2 uses the state assigned to you in class, whose two files are here under its code. Nothing is downloaded during the session.
