# Data for session 17

Two real files of near-infrared (NIR) spectra and fuel properties, measured on the same diesel fuels, and two tables of labels. The two data files are downloaded in class by `fetch_diesel.py`, the first code cell of section 1, and are not in the repository; `split.csv` and `assignments.csv` are, and hold fuel labels only, no spectra and no cetane numbers. Dataset A, the worked example of section 1, is the 133 calibration fuels and 82 validation fuels in `split.csv`. Dataset B is your one fuel, a record kept out of both.

## Downloading the files: `fetch_diesel.py`

The notebook runs `%run data/fetch_diesel.py`. The script downloads `SWRI_Diesel_NIR_CSV.zip` from Eigenvector Research if the two CSVs the notebook reads are not already here, checks the zip's SHA-256 against the value recorded on 2026-11-10, takes `diesel_spec.csv` and `diesel_prop.csv` out of it into this folder, and deletes the zip. On every run it checks each CSV's SHA-256, so every student and every grader reads the same bytes. The download is 1.0 MB, about a second on campus Wi-Fi, and the two CSVs take 2.8 MB of disk. If the download fails or a file differs, the script stops with a `RuntimeError` that says what to do. We will post the files on Canvas, in the Session 17 module, if the source refuses. If you download the zip by hand, put it in `data/` unopened and run the cell: the script takes the CSVs out of it. The repository's `.gitignore` keeps the zip and both CSVs out of git, so `git pull` keeps working.

## Source and terms

S. Hutzler, Southwest Research Institute (2004), "NIR Spectra of Diesel Fuels" and "Properties of Diesel Fuels", distributed by Eigenvector Research as `SWRI_Diesel_NIR_CSV.zip` on its [data sets page](https://eigenvector.com/resources/data-sets/), accessed 2026-11-10. The page says the data were obtained at Southwest Research Institute on a project sponsored by the U.S. Army, that outliers were removed, and that all the fuels are summer fuels. It states no licence or terms of use, so the course does not copy the files or any value from them into the repository.

## The spectra: `diesel_spec.csv`

784 fuels by 401 channels, 750 to 1550 nm every 2 nm, with no missing values. The file does not state the unit of the spectra; the notebook reads them as absorbance. Counted from 0, as pandas counts rows read with `header=None`, rows 0 to 8 hold the file's name, author and date and two rows of labels, row 9 is labelled `Axisscale` and holds the wavelengths in nm from the third column on, and each later row is one fuel: an empty first column, the fuel's label in the second, then its 401 values. A comma at the end of every row makes an empty last column, which the notebook drops.

The negative second derivative of the calibration fuels' mean spectrum puts its bands at 998, 1042 and 1064 nm and at 1240, 1264 and 1288 nm. [Ma and colleagues (2019)](https://doi.org/10.1038/s41598-019-45945-y), *Scientific Reports* 9, 9503, place the second overtone of aromatic C-H stretching near 1140 nm, of methyl C-H near 1190 nm and of methylene C-H near 1210 nm, and a combination band near 1400 nm, about 150 nm above the file's bands. The course uses the axis as the file gives it, as published work on these data does, and reads the first three bands as aromatic, methyl and methylene C-H from their order and from the signs of their coefficients in section 1, not from their positions.

## The properties: `diesel_prop.csv`

The same 784 fuels in the same order. Counted from 0, rows 0 to 7 hold the file's name, author and date and a row of labels, row 8 holds the column names, and each later row is one fuel: an empty first column, the label in the second, then seven properties. A property not measured on a fuel is `NaN`. The units are those Eigenvector's page gives; the page does not describe `FLASH`.

| Column | What it is | Fuels with a value |
|---|---|---|
| `BP50` | boiling point at 50% recovered, °C, ASTM D86 | 395 |
| `CN` | cetane number, ASTM D613, the engine test; the only property the notebook reads | 381 |
| `D4052` | density at 15 °C, g/mL, ASTM D4052 | 395 |
| `FLASH` | flash point, °C, by the values; not on Eigenvector's page | 395 |
| `FREEZE` | freezing temperature, °C | 395 |
| `TOTAL` | total aromatics, mass %, ASTM D5186 | 395 |
| `VISC` | viscosity at 40 °C, cSt (mm²/s) | 395 |

## The sets: `split.csv`

Columns: `label`, a fuel's label as both data files give it, and `set`, one of `calibration` (133 fuels), `validation` (82) or `record` (30). Every fuel listed has a cetane number. Eigenvector also distributes the fuels with a cetane number in a MATLAB file, `CNGATEST.mat`, divided by the depositors into 20 high-leverage fuels and two random groups of 113 and 112. The course matched each of those 245 fuels to its row in the CSV files by its spectrum and cetane number. The 20 high-leverage fuels and the group of 113 are the calibration set. The group of 112 is divided into the 82 validation fuels, which choose the number of latent variables and measure each model's error, and the 30 records, which no model is fitted to and no choice is made on. The other 136 fuels with a cetane number are in no set.

## Who has which fuel: `assignments.csv`

Columns: `student`, your student number from session 4, two digits; `label`, your fuel. Student 27 sets `FUEL = "21663"`. Numbers 27 to 29 are spares, and number 30 is the fuel the instructors' solution uses. The fuels were chosen by the instructors' script `select_fuels.py` with a fixed random seed, so that every record's calls at 51 are worth arguing over: the three-band model and PLS disagree, or both disagree with the engine value, or the PLS prediction is within one validation error of 51. No two records give the same pair of predictions to 0.1.
