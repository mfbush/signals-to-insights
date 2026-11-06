# Data for session 14

Two real sets of PM2.5 measurements, each made by PurpleAir sensors placed beside regulatory reference monitors, and one table of who has which sensors. The two sets are downloaded in class by `fetch_barkjohn.py`, the first code cell of section 1, and are not in the repository; `sensors.csv` is. Dataset A, the worked example of section 1, is the 24 hour set, with Washington's sensors as the example. Dataset B is your two sensors in the hourly smoke set.

## Downloading the two sets: `fetch_barkjohn.py`

The notebook runs `%run data/fetch_barkjohn.py`. For each set, the script downloads the zip from EPA ScienceHub if the CSV the notebook reads is not already here, checks the zip's SHA-256 against the value recorded on 2026-09-30, takes that one CSV out of the zip into its folder here, and deletes the zip. On every run it checks each CSV's SHA-256, so every student and every grader reads the same bytes. The downloads are 4 MB and 72 MB, about a minute on campus Wi-Fi, and the two CSVs take 268 MB of disk. If a download fails or a file differs, the script stops with a `RuntimeError` that says what to do. We will post the files on Canvas, in the Session 14 module, if the source refuses.

The CSVs land in `data/Data_DevelopmentUSPAcorrection_210408/` and `data/Dataset_PurpleAirSmoke_Barkjohn_1_18_23/`, the folders the Parameters cell's paths name. If you download a zip by hand from its DOI page, put it in `data/` unopened and run the cell: the script takes the CSV out of it. The repository's `.gitignore` keeps the zips and both folders out of git, so `git pull` keeps working.

## Source and terms

**Dataset A.** K. Barkjohn (2021), "Dataset Development and Application of a United States wide correction for PM2.5 data collected with the PurpleAir sensor", U.S. EPA Office of Research and Development, EPA ScienceHub, [doi:10.23719/1522388](https://doi.org/10.23719/1522388), file `Data_DevelopmentUSPAcorrection_210408.zip`, accessed 2026-11-05. The paper is K. K. Barkjohn, B. Gantt and A. L. Clements, *Atmospheric Measurement Techniques* 14, 4617 (2021), [doi:10.5194/amt-14-4617-2021](https://doi.org/10.5194/amt-14-4617-2021).

**Dataset B.** K. Barkjohn (2023), "Dataset Correction and Accuracy of PurpleAir PM2.5 Measurements for Extreme Wildfire Smoke", U.S. EPA Office of Research and Development, EPA ScienceHub, [doi:10.23719/1528138](https://doi.org/10.23719/1528138), file `Dataset_PurpleAirSmoke_Barkjohn_3_15_23.zip`, accessed 2026-11-05. The paper is K. K. Barkjohn, A. L. Holder, S. G. Frederick and A. L. Clements, *Sensors* 22, 9669 (2022), [doi:10.3390/s22249669](https://doi.org/10.3390/s22249669).

EPA ScienceHub states that data produced by EPA are in the public domain in the United States, without warranty. The sensor readings in both sets originate from PurpleAir sensors and are used here as EPA published them; the course does not copy or redistribute them.

## Dataset A: `Full24hrdataset.csv`

12,413 rows from 49 sensors in 15 states, 2017-09-30 to 2020-01-13. Each row is one day at one sensor beside one reference monitor. At some sites two reference monitors stood together, a filter-based Federal Reference Method sampler and a continuous Federal Equivalent Method monitor, so 2,197 sensor-days have two rows, one for each. The file has 31 columns; the notebook reads six.

| Column | What it is |
|---|---|
| `Date` | the day, `YYYY-MM-DD` |
| `ID` | the sensor: the state's two letters and a number, for example `WA2`; the notebook takes the state from the letters |
| `PM25FM` | the reference monitor's 24 hour mean PM2.5, µg/m³ |
| `PM25cf1` | the sensor's raw 24 hour mean PM2.5, µg/m³, by its CF=1 setting |
| `RH` | the sensor's relative humidity, daily mean, % |
| `PM25PARHcor` | the paper's corrected value, µg/m³, from the raw reading and RH |

The other columns are particle counts in six size bins, temperature, dew point, other corrections, and ratios and differences against the reference. A data dictionary, a Word file in the zip, describes them all; the script does not take it out.

## Dataset B: `Finaldataset_correcteddatasetwholding_10_26_22.csv`

1,513,776 rows from 27 sensors between 2018 and 2020, many through the 2020 fire season, when the reference reached hundreds of µg/m³. Each row is one hour at one sensor beside one reference monitor. The file is 262 MB; reading the seven columns the notebook uses takes about 3 seconds and 220 MB of memory.

| Column | What it is |
|---|---|
| `hr` | the hour, as text, `YYYY-MM-DD HH:MM:SS`; its first ten characters are the date |
| `city` | the sensor's site, the name `sensors.csv` uses, for example `Bend_S` |
| `RH` | the sensor's relative humidity for the hour, % |
| `PA` | the sensor's raw PM2.5 for the hour, µg/m³ |
| `ref` | the reference monitor's PM2.5 for the hour, µg/m³ |
| `wholdtype`, `adjtype` | the paper's bookkeeping: how its correction was refitted for the row, described in the 2022 paper |

The notebook does not read `id`, the sensor's identifier, `monitortype`, the reference monitor's make and method, `week`, `adj`, the paper's corrected value for the row, or `State`, which is mostly empty and makes `read_csv` warn about mixed types when it is read.

## Who has which sensors: `sensors.csv`

Columns: `student`, your student number from session 4, two digits; `sensor_1` and `sensor_2`, your two sensors' `city` names, in alphabetical order. Student 27 sets `SENSORS = ["Keeler_S", "RTP"]`. Numbers 27 to 29 are spares, and number 30 is the pair the instructors' solution uses. The pairs were chosen by the instructors' script `select_sensors.py` with a fixed random seed, so that every pair holds days near a breakpoint and no two pairs give the same counts in section 3.
