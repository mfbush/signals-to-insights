# Data for session 8

Two kinds of data. `ag_trace_1ms.csv` is real: one ICP-MS count trace of dissolved silver, for the first half of section 1. `method_study.csv` and `labs/` are simulated: lead method detection limit studies by ICP-MS, one for the second half of section 1 and one per lab for sections 2 and 3. Nothing is downloaded during the session.

## The silver count trace: `ag_trace_1ms.csv`

### Source

I. Abad Álvaro, E. Bolea Morales and F. Laborda García, "SP-ICP-MS Raw Data - Towards the harmonization of raw data processing in single particle inductively coupled plasma mass spectrometry", Zenodo, 2026, [doi:10.5281/zenodo.18745872](https://doi.org/10.5281/zenodo.18745872), released under CC BY 4.0, accessed 2026-10-02. The data are described in *Talanta* (2026) 129575, [doi:10.1016/j.talanta.2026.129575](https://doi.org/10.1016/j.talanta.2026.129575).

The file is `Table 1_raw data/Tabla1_ Ag 0.1 ppb_1000us_1.csv` from the deposit's zip, copied byte for byte and renamed, as the license asks us to say. The script that does this, `fetch_ag_trace.py`, is kept by the instructors.

### The trace

A solution of dissolved silver at 0.1 µg/L flowed into an ICP-MS that counted <sup>107</sup>Ag ions in consecutive 1 ms windows, the dwell time, for 60.0 s. The file has a one-line header, `107Ag, counts`, which names the isotope and the unit, then 59,999 whole numbers, one count per window, with Windows line endings. The mean is 2.800 counts per window, 2800 counts per second. The deposit's authors recorded it to study single-particle ICP-MS, where nanoparticles show up as brief bursts of counts; this solution held dissolved silver only, so the trace shows the instrument's counting noise and the slower noise of the plasma and the sample introduction.

## The lead studies: `method_study.csv` and `labs/`

### What they are

Each file is one laboratory's method detection limit (MDL) study for lead in drinking water by ICP-MS, done the way 40 CFR 136 Appendix B asks: seven method blanks and seven spikes at 2 µg/L, prepared through the whole method and read on three days. The files in `labs/`, `lab_01.csv` to `lab_36.csv`, also hold 40 first-draw tap-water samples from homes, read in the same run. Every solution is read at four integration times, 0.025, 0.1, 0.4 and 1.6 s. None of it is measured. The studies are simulated by the generator `make_lead_runs.py`, which the instructors keep, with seed 427; a rerun rewrites every file byte for byte.

### The counting model

- Counts at <sup>208</sup>Pb are Poisson, with a mean equal to the count rate times the integration time. The rate, in counts per second, is the background plus the sensitivity times the lead in µg/L.
- The sensitivity is 500 counts per second per µg/L, a teaching value chosen so that counting noise matters at these integration times. A modern instrument is 20 to 200 times more sensitive; the silver trace above gives about 28,000 counts per second per µg/L. It changes a little from day to day, which each day's calibration removes.
- Each reading's rate also varies by 2% at random, a proportional noise that a longer count does not reduce, standing in for the noise the silver trace shows past about 16 ms.
- The background starts each day at 30 counts per second and rises through the run at each lab's own drift rate, between 15 and 90 counts per second per hour. That is more drift than a lab would carry without rinsing or recalibrating; it is set so that section 3 has a drift to correct.
- Every solution prepared through the method, blanks, spikes and homes, picks up lead from its reagents, a different amount in each solution around each lab's own mean and spread. Calibration standards and calibration blanks are made in clean acid and carry none.
- A home's lead is drawn from a lognormal distribution with a median of 1.0 µg/L.

Each lab was kept only if its data show what sections 2 and 3 ask about, and only if its MDL never rises from one integration time to the next: a standard deviation from seven replicates is uncertain by about a factor of two, enough to make a rise by chance. It was also kept only if the drift raises its homes' mean under the opening background at every integration time, since at short times the noise of the calibration blanks can hide it. Thermal (Johnson) noise is left out: a pulse-counting detector has none worth modelling.

### The run

Each day opens with five calibration standards at 0, 1, 2, 5 and 10 µg/L, the 0 being the opening calibration blank. The day's samples follow in a shuffled order, with a calibration blank before the first sample, after every fourth and at the end. Each position in the run takes 4 minutes.

### The columns

One row per reading, in run order:

- `day`: 1, 2 or 3.
- `position`: the solution's place in that day's run, from 1.
- `minute`: minutes from the start of that day's run.
- `solution`: `std_0` to `std_10`, `cal_blank`, `blank_1` to `blank_7`, `spike_1` to `spike_7`, or `home_01` to `home_40`.
- `kind`: `standard`, `cal_blank`, `blank`, `spike` or `home`.
- `nominal_ug_L`: the lead added, in µg/L, for standards, blanks and spikes; empty for homes.
- `integration_s`: the integration time of this reading, in s.
- `counts`: the counts recorded in that time.

`method_study.csv` has the same columns and no homes.
