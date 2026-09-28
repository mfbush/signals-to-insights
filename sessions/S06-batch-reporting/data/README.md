# Data for session 6

Two folders of spectra: `flarelab/`, real ferrocyanide spectra for section 1, and `runs/`, one simulated run of iron in water per student for sections 2 and 3. Nothing is downloaded during the session.

## `flarelab/`: ferrocyanide standards on two days

### Source

P. Rimmer, "Supplementary data for "Measuring Nitroprussside and Ferrocyanide with Quantitative UV-Vis using FlareLab"", Harvard Dataverse, version 1, 2025, [doi:10.7910/DVN/QAZ9B6](https://doi.org/10.7910/DVN/QAZ9B6), released under CC0 1.0, accessed 2026-09-28. The title's spelling is the record's. The data belong to the preprint L. Rossmanith, S. K. Platymesi, S. J. Thompson and P. B. Rimmer, "Measuring Nitroprussside and Ferrocyanide with Quantitative UV-Vis using FlareLab", ChemRxiv, 2025, [doi:10.26434/chemrxiv-2025-d3ltb](https://doi.org/10.26434/chemrxiv-2025-d3ltb), which reports the molar attenuation coefficient of ferrocyanide at 340 nm as (2.2 ± 0.4) × 10^3 dm^2/mol, i.e., 220 L/mol/cm. The record holds 392 files for ferrocyanide, nitroprusside and their mixtures; this folder is three of them, from `Supplementary Data/Raw Data/Ferrocyanide/`, copied byte for byte:

- `Ferrocyanide Standard 240409/`, 39 spectra measured on April 9, 2024
- `Ferrocyanide Standard 240410/`, 39 spectra measured on April 10, 2024
- `Ferrocyanide Standard File Parameters.csv`, the laboratory's list of the ferrocyanide files, 213 rows for four days, of which 78 are the two days here

### The spectra

Each file is one spectrum from an Ocean Insight Flame spectrometer (serial FLMS018081): a header of instrument settings, the line `>>>>>Begin Spectral Data<<<<<`, and 2,048 rows of two tab-separated columns, wavelength in nm, 178 to 879 nm, and detector counts, dark-corrected by the spectrometer. The files mix line endings as the spectrometer wrote them (LF in the header, CRLF in the data, one stray carriage return after the first line); the repository keeps them unchanged, and reading the text with Python's `splitlines()` handles all three.

The file name carries the facts, separated by underscores: `LE_240409_d_50_mm_ferrocyanide_counts_v5_FLMS018081_17-18-03-634.txt` is day 240409, distance setting 50 mm, role `ferrocyanide`, standard `v5`, spectrometer serial, and the time of the measurement. The distance setting is a setting of the FlareLab instrument, recorded in millimeters; each day was measured at 50, 200 and 550 mm. The role is one of three:

| Role in the name | Parameter table `Experiment type` | What it is | Files per day |
|---|---|---|---|
| `Background` | `Background` | the dark spectrum, counts with no light | 3, one per setting |
| `initial` | `initial counts` | the reference, the cuvette of water | 3, one per setting |
| `ferrocyanide` | `Ferrocyanide counts` | a standard, `v1` to `v11` | 33, eleven per setting |

### The parameter table

One row per file: `dateID` (yymmdd), `Version ID`, `Distance Setting` (mm), `Experiment type`, `standard type`, `Filename`, and `concentration (M)`, the standard's concentration in mol/L, `NA` for the dark and reference. The eleven standards are 0.000001, 0.000005, 0.00001, 0.00005, 0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05 and 0.1 M. The concentration is in the table only, not in the file name.

## `runs/`: iron in water, one run per student

Simulated by the generator `make_iron_runs.py`, which the instructors keep, with seed 427; a rerun rewrites every file byte for byte. Iron is determined as the tris(1,10-phenanthroline)iron(II) complex at 510 nm, 0.199 AU per mg/L at 1 cm (molar absorptivity 11,100 L/mol/cm), with 0.002 AU of noise. There are 36 runs, `run_01` to `run_36`, one assigned to each student in class and the rest spares. Each has the same layout, 16 spectra and a sequence table:

- `standards/std_0p00.csv` to `standards/std_4p00.csv`: the reagent blank and six standards at 0.10, 0.25, 0.50, 1.00, 2.00 and 4.00 mg/L, the level written with `p` for the decimal point
- `samples/<water>_rep<k>.csv`: three waters, each in triplicate, drawn from tap, spring, river, cistern and well; the names differ between runs
- `sequence.csv`: the instrument's sequence table, one row per measurement in the order it was made

A spectrum is a CSV with the columns `wavelength_nm`, 400 to 700 nm at 1 nm, and `absorbance_AU`, blanked by the instrument. The sequence table has the columns `position`, `file` (the path below the run folder, for example `samples/tap_rep1.csv`), `kind` (`standard` or `sample`), `level_mg_L` (standards only), `sample` and `replicate` (samples only), `instrument` (`UV-1` or `UV-2`) and `note`.
