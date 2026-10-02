# Data for session 2

All three files are simulated from a fixed seed, so every copy is identical. The instructors keep the generator scripts.

## uvvis_calibration.csv

The same file as in session 1: absorbance at 520 nm for six standards of a dye at 0, 5, 10, 15, 20 and 25 µM in a 1 cm cuvette, one row per standard.

| Column | Unit | Meaning |
|---|---|---|
| `concentration_uM` | µM | concentration of the standard |
| `absorbance_AU` | AU | absorbance at 520 nm, reported to 0.001 AU |

The values follow Beer-Lambert behavior with a slope of 0.0597 AU/µM, a response that flattens above 1.2 AU, and read noise with a standard deviation of 0.0015 AU.

## ms_peaks.csv

A centroided peak list, i.e., one row per peak as an instrument's peak-picking step exports it, from a positive-mode electrospray mass spectrum of a caffeine standard, 28 peaks from <i>m</i>/<i>z</i> 130 to 446, sorted by <i>m</i>/<i>z</i>.

| Column | Unit | Meaning |
|---|---|---|
| `mz` | <i>m</i>/<i>z</i> | mass-to-charge ratio of the peak, to 0.0001 |
| `intensity_counts` | counts | peak intensity |

The peaks are protonated caffeine at <i>m</i>/<i>z</i> 195.088 with its isotope peaks, the sodium adduct, a fragment at <i>m</i>/<i>z</i> 138.066, the proton- and sodium-bound dimers, four plasticizer ions of the kind found in electrospray backgrounds, and 16 low-intensity noise peaks. Each <i>m</i>/<i>z</i> carries a mass error with a standard deviation of 1.5 ppm and each intensity a 3% scatter.

## arrhenius_rates.csv

First-order rate constants for one reaction at seven temperatures from 283 to 343 K, one row per temperature.

| Column | Unit | Meaning |
|---|---|---|
| `temperature_K` | K | temperature of the measurement |
| `rate_constant_per_s` | 1/s | measured first-order rate constant, to four significant figures |

The values follow the Arrhenius equation with a prefactor of 2.0 × 10¹¹ per second and an activation energy of 80.0 kJ/mol, with a 3% relative scatter on each rate constant.
