# Data for session 13

Real X-ray powder diffraction patterns of a certified standard, all in the repository, so nothing is downloaded in class. The five `.cif` files are the patterns; `certificate.csv` is the certificate's table of certified sizes; `windows.csv` says where each reflection's window begins and ends on each pattern; `reflections.csv` says which pattern and reflection are yours. Dataset A, the worked example of section 1, is reflection 032 of pattern 5857.

## Source and licence

National Institute of Standards and Technology (NIST), "SRM 1979 certification data: synchrotron powder diffraction patterns of nano-crystalline zinc oxide", NIST Public Data Repository, record mds2-2269, [doi:10.18434/M32269](https://doi.org/10.18434/M32269), file `srm_1979_cifs_20201110a.zip`, accessed 2026-10-23. The data are NIST data, free of copyright in the United States under the [NIST licence](https://www.nist.gov/open/license). The course copied the five patterns of the 15 nm powder unchanged; the zip also holds four patterns of the 60 nm powder, which the session does not use.

The standard and its certification are described in the [certificate of analysis](https://tsapps.nist.gov/srmext/certificates/1979.pdf) (NIST, 2021) and in J. P. Cline et al., "The certification of Standard Reference Material 1979: powder diffraction line profile standard for crystallite size analysis", *Journal of Research of NIST* 125, 125020 (2020), [doi:10.6028/jres.125.020](https://doi.org/10.6028/jres.125.020).

## The patterns

Each file is one pattern of one specimen of the 15 nm zinc oxide powder, measured on beamline 11-BM of the Advanced Photon Source at a wavelength of 0.41419 Å, from 2.0° to 47.5° 2θ in steps of 0.001°, 45,504 points. The files are named by NIST's scan number and bottle: `5857_15_nm_174.cif` is scan 5857 of the powder from bottle 174, and the notebook calls that pattern `5857`.

A file is text in the crystallographic information file (CIF) format, with three data blocks of the same 45,504 points: the pattern as measured, the same pattern with its angle scale corrected against the NIST line-position standard SRM 660c, and NIST's fitted model of it. The notebook's `read_cif` reads the second block, whose loop is headed `_pd_proc_2theta_corrected`, `_pd_proc_intensity_total` and `_pd_proc_ls_weight`: the corrected angle in degrees 2θ, the counts, and the least-squares weight, from which the notebook takes σ = 1 / √weight in counts.

## The certificate: `certificate.csv`

Table 1 of the certificate, one row per reflection of the 15 nm powder. Columns: `hkl`, the reflection's indices as text (read it with `dtype={"hkl": str}`, so that `010` keeps its zero); `two_theta_deg`, its position at 0.41419 Å, computed from the certified lattice parameters a = 3.249664 Å and c = 5.208330 Å; `L_vol_nm`, the certified volume-weighted mean column length ⟨L⟩vol in nm; `U_nm`, its expanded uncertainty in nm at k = 2, Type A and B combined; `unaffected_by_stacking_faults`, `True` for the ten reflections the certificate marks "breadth unaffected by stacking faults".

## The windows: `windows.csv`

One row per pattern and reflection, 110 rows. Columns: `pattern`, `hkl`, and `lo_deg` and `hi_deg`, the window's edges in degrees 2θ. A window runs halfway to the nearest zinc oxide line on each side, certified or not, or eight breadths of a 15 nm crystallite from the reflection, whichever is narrower. The edges were computed by the instructors' script `select_reflections.py` from the certified lattice.

## Who has which reflection: `reflections.csv`

Columns: `student`, your student number from session 4, two digits; `pattern` and `hkl`, your pattern and reflection. Student 22 sets `PATTERN = "5858"` and `REFLECTION = "014"`. Numbers 27 to 29 are spares, and number 30 is the pair the instructors' solution uses. The pairs and the order were chosen by `select_reflections.py` with a fixed random seed, so that the room holds reflections with and without stacking faults, and with and without a neighbouring line in the window.
