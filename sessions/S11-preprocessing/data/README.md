# Data for session 11

Two simulated chromatogram files, both in the repository, so nothing is downloaded in class. `chromatogram_a.csv` is Dataset A, the worked example of section 1. `records.csv` holds every student's record for sections 2 and 3, one column each.

## The method

Both files simulate the same quality-control method: a drug substance run on a gradient HPLC with UV detection, 30 minutes at 5 points per second, the detector signal in milli-absorbance units (mAU). The method's known peaks, which the notebook's Parameters cell lists:

| Peak | Retention time (min) | Relative retention |
|---|---|---|
| impurity 1 | 7.4 | 0.62 |
| main peak | 12.0 | 1.00 |
| impurity 2 | 18.6 | 1.55 |
| impurity 3 | 25.2 | 2.10 |

The main peak is about 1,200 mAU tall; the impurities are under 1 mAU. Every peak is 8 to 13 s wide at half height. The baseline rises with the gradient's organic fraction, about 30 mAU over the run, with a small curvature, and carries detector noise of about 0.03 mAU rms. The retention times drift by a few hundredths of a minute from run to run.

## Dataset A: `chromatogram_a.csv`

Columns: `time_min`, the retention time in minutes, 0 to 30 in steps of 0.2 s (9,001 rows); `absorbance_mAU`, the detector signal. One run of the method with the three known impurities at levels the instructors chose so that the session's decision depends on the baseline.

## The records: `records.csv`

Columns: `time_min`, as above, then `record_01` to `record_30`, each one run of the method in mAU. Your record is your student number from session 4: student 7 reads `record_07`. Records 25 to 29 are spare and record 30 is the solution's. Each record's impurity levels, baseline and noise differ, and a batch is not obliged to match the method's table.

## How the files were made

Both were written by the generator `make_chromatograms.py`, which the instructors keep, from `np.random.default_rng` seeds tried from 427 upward; a record's seed was kept only if the session's decision is clear on it. Each true peak area is known to the instructors and is not in the repository. A rerun of the generator rewrites both files byte for byte.
