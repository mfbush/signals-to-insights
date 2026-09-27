# Data for session 1

## uvvis_calibration.csv

Simulated. Absorbance at 520 nm for six standards of a dye at 0, 5, 10, 15, 20 and 25 µM in a 1 cm cuvette, one row per standard.

| Column | Unit | Meaning |
|---|---|---|
| `concentration_uM` | µM | concentration of the standard |
| `absorbance_AU` | AU | absorbance at 520 nm, reported to 0.001 AU |

The values were generated from Beer-Lambert behavior with a slope of 0.0597 AU/µM, a response that flattens above 1.2 AU, and random read noise with a standard deviation of 0.0015 AU, from a fixed seed so every copy of the file is identical. The instructors keep the generator script. `ai-practices.md` uses the same series for its worked judgment entry.
