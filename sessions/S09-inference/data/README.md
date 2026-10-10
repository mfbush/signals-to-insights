# Data for session 9

One real file and one table of draws from it. `Flint-Samples-FINAL.xlsx` holds the lead results of Virginia Tech's 2015 tap-water survey in Flint, Michigan; it is downloaded in class by `fetch_flint.py`, the first code cell of section 1, and is not in the repository. `draws.csv` says which samples of that file make up each student's draw for sections 2 and 3. It holds row numbers only, no lead values.

## The Flint lead results: `Flint-Samples-FINAL.xlsx`

### Source

FlintWaterStudy.org (2015), "Lead Results from Tap Water Sampling in Flint, MI during the Flint Water Crisis", Virginia Tech, file `Flint-Samples-FINAL.xlsx` ([download link on FlintWaterStudy.org](https://flintwaterstudy.org/wp-content/uploads/2015/12/Flint-Samples-FINAL.xlsx)), accessed 2026-10-10. The site gives that citation and states no licence, so the course does not copy the file into the repository. Each student downloads it once, and the repository's `.gitignore` keeps the download out of git.

### Downloading it

`fetch_flint.py` downloads the file into this folder if it is not already here, then checks its SHA-256 against the value recorded on 2026-10-10, for a file of 33,202 bytes, so every student and every grader reads the same bytes. The site refuses Python's default user agent, so the script names itself in the request. If the download fails or the file differs, the script stops with a `RuntimeError` that says what to do. We will post the file on Canvas, in the Session 9 module, if the source refuses.

### The file

Three sheets. Sheet 1, "Samples from Flint Water homes", holds 271 samples from 269 homes, one row per sample under a one-line header, with credits in the rows below the samples; homes 31 and 79 were sampled twice, and both of their samples count, as in Virginia Tech's summary. Sheet 2 holds 5 samples the study did not use, with the reason for each. Sheet 3 compares Virginia Tech's first draws with the Michigan Department of Environmental Quality's results at 21 homes; the notebook does not use it.

Each home took three bottles: the first draw after at least 6 hours without use, then the water after 45 s and after 2 min of running the tap. Lead was measured by ICP-MS, with a stated detection limit of 1 µg/L, and every result in sheet 1 is a number, including the 40 first draws below 1 µg/L. Results are in ppb, which for lead in water is µg/L.

### The columns of sheet 1, and their names in the notebook

| Column in the file | Name in the notebook | What it is |
|---|---|---|
| `SampleID` | `sample_id` | the study's number for the home |
| `Zip Code`, `Ward` | not kept | where the home is |
| `Pb Bottle 1 (ppb) - First Draw` | `first_draw_ug_L` | lead in the first draw, µg/L |
| `Pb Bottle 2 (ppb) - 45 secs flushing` | `flushed_45s_ug_L` | lead after 45 s of flushing, µg/L |
| `Pb Bottle 3 (ppb) - 2 mins flushing` | `flushed_2min_ug_L` | lead after 2 min of flushing, µg/L |
| `Notes` | not kept | "house sampled twice" for homes 31 and 79 |
| (the row number) | `sheet_row` | the sample's row in the spreadsheet, row 1 being the header |

`load_homes` in section 1 reads sheet 1, keeps the rows with a `SampleID`, adds `sheet_row` and renames the columns.

## The draws: `draws.csv`

Each draw is 60 of the 271 samples in sheet 1, chosen at random without replacement, the size of a sampling campaign a utility might run. There are 36 draws, `draw_01` to `draw_36`. The file has two columns, `draw` and `sheet_row`, one row per sample in a draw, so it holds the row numbers of the samples and none of their values; the notebook applies it to the file you download.

The draws were made by the generator `make_draws.py`, which the instructors keep, with seed 427. A draw was kept only if every call the notebook asks about is clear of its threshold: its 90th percentile and its lower bound are each at least 0.5 µg/L from 10 and from 15 µg/L, the values at ranks 54 and 55 differ, and the p values of the paired and the two-sample t-tests are each at least 0.01 from 0.05. A rerun rewrites the file byte for byte.
