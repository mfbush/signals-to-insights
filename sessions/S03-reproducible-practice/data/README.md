# Data for session 3

The one file is simulated from a fixed seed, so every copy is identical. The instructors keep the generator script.

## fe_phen_calibration.csv

Six standards of the iron(II) 1,10-phenanthroline complex, the colorimetric iron method from quantitative analysis, at 0, 10, 20, 40, 60 and 80 µM in a 1 cm cuvette, measured at 510 nm. One row per standard. The spectrophotometer exported percent transmittance, not absorbance.

| Column | Unit | Meaning |
|---|---|---|
| `concentration_uM` | µM | iron concentration of the standard |
| `transmittance_pct` | %T | percent transmittance at 510 nm, reported to 0.1 %T |

The values follow Beer-Lambert behavior in absorbance with a slope of 0.0111 AU/µM, from a molar absorptivity of 11,100 per molar per cm, a reagent blank of 0.004 AU, and read noise with a standard deviation of 0.002 AU, converted to percent transmittance. Every standard is below 0.9 AU, inside the linear range.
