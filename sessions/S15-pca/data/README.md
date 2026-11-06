# Data for session 15

One real file of X-ray fluorescence analyses of obsidian, in the repository as its authors deposited it, so nothing is downloaded in class, and one table of who has which artefact. `obsidian_data.xlsx` holds the analyses; the notebook reads its sheet `data` with `pd.read_excel`. `assignments.csv` names your artefact. Dataset A, the worked example of section 1, is the reference analyses of the geological sources. Dataset B is your artefact's one or three analyses in the same sheet.

## Source and licence

J. Petřík and L. Prokeš, "Chemical compositions of grinded obsidian artefacts from Early Eneolithic site in Nitra-Selenec (Slovakia) and reference samples of carpathian obsidians", Zenodo (2025), [doi:10.5281/zenodo.14771241](https://doi.org/10.5281/zenodo.14771241), file `obsidian_data.xlsx`, accessed 2026-11-05, licence [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The file is the deposit byte for byte, 360,635 bytes, SHA-256 `85df4a24b2ad971443a019e97dc6db2c7a232d3a7b7bd3bf8fbc5a1fd9e9ac15`, put here and checked by the instructors' script `fetch_obsidian.py`. The same record holds the authors' own analysis as an R Quarto document, `Obsidian_Nitra2mLPpwl.qmd`, which the course does not copy.

The measurements are energy-dispersive X-ray fluorescence (ED-XRF): a flake is irradiated with X-rays, each element emits X-rays at its own energies, and the counts at those energies give the element's concentration. The deposit does not name the instrument or its calibration, so its concentrations are for comparison within the sheet, against its own reference analyses, not with published obsidian compositions.

## The workbook: `obsidian_data.xlsx`

Five sheets. The notebook reads `data`; the others are described so that you know what you are not using.

| Sheet | Rows | What it holds |
|---|---|---|
| `List1` | 243 | the authors' working table, with Czech column headings (`Vzorek` sample, `Lokalita` site, `Zdroj` source) and 134 columns, most of them empty |
| `data` | 246 | one row per ED-XRF analysis of a reference sample or an artefact, 22 columns: the sheet the notebook reads |
| `data2` | 107 | the subset the authors' Quarto document analyses: the source references and 17 Nitra artefacts, with the non-detects and the second measurement campaign treated as the document describes |
| `data2orig` | 108 | `data2` before the authors' last edit |
| `List2` | 53 | the authors' confusion matrix and predicted source probabilities, from their random-forest model |

### Sheet `data`

Columns: `Sample`, the specimen's name as the authors wrote it, repeated when a specimen was analysed more than once; `Source`, a code for where the specimen came from; `Datation`, the archaeological period of an artefact, empty for the references; then 19 elements, twelve as the element in parts per million (`Rb`, `Sr`, `Y`, `Zr`, `Th`, `As`, `V`, `Zn`, `Ba`, `U`, `Yb`, `Nb`) and seven as the oxide in weight per cent (`Al2O3`, `SiO2`, `K2O`, `CaO`, `Fe2O3`, `TiO2`, `MnO`).

The `Source` codes:

| Code | Rows | Meaning |
|---|---|---|
| `CIB`, `CIV` | 26, 18 | Slovak sources, the Carpathian 1 group (CI), in the Zemplín hills: the sample names are Brehov, Cejkov and Kašov under `CIB`, Viničky and Malá Bara under `CIV` |
| `CIIE`, `CIIEM`, `CIIT` | 19, 15, 10 | Hungarian sources, the Carpathian 2 group (CII), in the Tokaj mountains: Erdőbénye, Mád and Tolcsva under `CIIE`, Mád and Olaszliszka under `CIIEM`, Tolcsva under `CIIT` |
| `CIII` | 3 | the Ukrainian source, Carpathian 3: Rokosovo |
| `P` | 118 | artefacts from Palaeolithic and Mesolithic sites in Slovakia, Moravia and Hungary, with the period in `Datation` |
| `N` | 30 | artefacts the sheet dates Neolithic: the Nitra site of the deposit's title, Košice sites and others |
| `ref` | 4 | laboratory reference glasses, among them NIST SRM 610 |
| `B` | 3 | three Bronze Age artefacts |

The notebook's `SOURCES` maps the first six codes to CI, CII and CIII and `P` and `N` to artefacts, and leaves `ref` and `B` out.

**Non-detects are coded 0.** A value of 0 means the element was not detected, not that it was measured as zero. The elements with many zeros are `As` (123 of 246 rows), `Nb` (105), `Zn` (86), `Yb` (84), `Y` (76), `Zr` (56) and `Th` (18); `Ba` has 15, `Sr` and `TiO2` 3 each, `SiO2` 1, and the rest none. The notebook keeps an analysis only when none of its ten elements is zero.

**Two measurement campaigns.** Rows 0 to 102 of the sheet (campaign A) and rows 103 to 245 (campaign B) were measured at different times, and three elements do not agree between them. Two Slovak references, Viničky2 and Viničky3, were measured in both campaigns and pass the notebook's filters: their `U` reads 16 to 20 times lower in campaign B than in A, `TiO2` 11 to 15 times lower and `MnO` 157 to 202 times lower, whereas the other ten elements read within a factor of two (A over B from 0.75 to 1.84). Campaign A's uranium and manganese oxide are not obsidian values. The notebook leaves `U`, `TiO2` and `MnO` out and keeps the ten elements that agree: `Rb`, `Sr`, `Th`, `Ba`, `V`, `Al2O3`, `SiO2`, `K2O`, `CaO`, `Fe2O3`. Campaign B is also not normalised to 100%: 19 of its rows report `SiO2` above 100 wt%, and 12 rows of the sheet report it below 50 wt%. The notebook keeps an analysis only when its `SiO2` is 50 to 100 wt%. The notebook also leaves out the 19 rows whose name contains "red", the red obsidians, as the authors did.

After the three filters, 53 reference analyses remain (CI 30, CII 20, CIII 3) and 122 artefact analyses of 92 distinct names, 15 of them measured three times.

## Who has which artefact: `assignments.csv`

Columns: `student`, your student number from session 4, two digits; `artefact`, the `Sample` name of your artefact in sheet `data`, exactly as written there. Student 08 sets `ARTEFACT = "Moravany4"`. Numbers 27 to 29 are spares, and number 30 is the artefact the instructors' solution uses. The artefacts were chosen by the instructors' script `select_artefacts.py` with a fixed random seed, from the names whose section 2 result does not hang on the last digit, so that the room holds every outcome of section 3.
