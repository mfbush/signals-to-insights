# Data for session 12

Real gas chromatograms of commercial lavender oils, all in the repository, so nothing is downloaded in class. `L13A.cdf` is Dataset A, the worked example of section 1. The other 90 files are three replicate runs, A, B and C, of each of 30 oils, one oil per student for sections 2 and 3. `samples.csv` says which oil is yours.

## Source and licence

K. Pokajewicz (2024), "Lavandula angustifolia essential oil adulteration dataset", Mendeley Data, version 1, [doi:10.17632/pgkrc7wyj4.1](https://doi.org/10.17632/pgkrc7wyj4.1), folder "GC-FID analyses on wax column", accessed 2026-10-22. Licence: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The dataset holds 55 commercial oils sold as *Lavandula angustifolia*; the findings on them are in K. Pokajewicz, *Farmacja Polska* 81(2), 95 (2025), [doi:10.32383/farmpol/211704](https://doi.org/10.32383/farmpol/211704), in Polish. The course copied runs of 31 of the oils and renamed some of them, as the next section says; the files are otherwise unchanged.

## The runs

Each oil was run by gas chromatography with flame ionization detection (GC-FID) on a polar wax (macrogol) column, by the depositor's account according to the European Pharmacopoeia's monograph on lavender oil, which sets the chromatographic profile the session's limits come from. Each run is 73 min long (`L55A.cdf`, 70 min) at 10 points per second, with the solvent near 4.4 min and the oil's components from about 6 min on. In every run the three components the session reports elute in this order: camphor near 40.37 min, linalool near 42.88 min and linalyl acetate near 43.29 min.

The files are named `L<oil><run>.cdf`, such as `L19A.cdf`, `L19B.cdf` and `L19C.cdf` for the three runs of oil 19. In the deposit, run A of 18 oils has no letter, and the course added the `A`: `L19.cdf` became `L19A.cdf`, and the same for oils 23, 25, 28, 29, 31, 34, 36, 37, 38, 39, 43, 44, 47, 49, 50, 51 and 53. Every other file has its deposited name.

## What each file holds

Each run is an AIA netCDF file, the chromatography data exchange format (ASTM E1947), which `scipy.io.netcdf_file` reads. The notebook's `read_run` uses four of its variables:

| Variable | What it is |
|---|---|
| `ordinate_values` | the detector signal, one value per point, in mV (the file's `detector_unit` is `mVolts`) |
| `actual_sampling_interval` | the time between points, in minutes (0.0016667 min, 0.1 s); a single number, a 0-dimensional variable, read with `float(...data)`. The first point is at time 0 |
| `peak_retention_time` | the data system's peak table: each peak's retention time, in minutes |
| `peak_area_percent` | the data system's peak table: each peak's area as a percentage of the total of the peaks it lists |

The data system's table lists 19 to 54 peaks per run. The files also hold that table's start and end times, areas, heights and baseline points (`peak_start_time`, `peak_area`, `baseline_start_value` and others), the run length (`actual_run_time_length`), and global attributes such as `sample_name` and `injection_date_time_stamp`.

## Who has which oil: `samples.csv`

Columns: `student`, your student number from session 4, two digits; `sample`, your oil. Student 7 sets `SAMPLE = "L39"` and reads `L39A.cdf`, `L39B.cdf` and `L39C.cdf`. Numbers 27 to 29 are spares, and number 30 is the oil the instructors' solution uses. The oils and the order were chosen by the instructors' script `select_samples.py`, with a fixed random seed, so that every student holds a different oil and the calls differ across the class.
