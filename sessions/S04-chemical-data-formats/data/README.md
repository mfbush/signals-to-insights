# Data for session 4

One committed file, the acetone spectrum that section 1 of the activity reads, and one file you download yourself in class.

## acetone_ir.jdx

Gas-phase infrared spectrum of acetone, CAS registry number 67-64-1, from the NIST Chemistry WebBook. The record comes from the NIST/EPA Gas-Phase Infrared Database, measured by Sadtler Research Laboratories under contract to the US EPA, as the file's `ORIGIN` and `$NIST SOURCE` fields say. It was downloaded on 2026-09-27 from the [WebBook's JCAMP-DX download link for the acetone IR spectrum](https://webbook.nist.gov/cgi/cbook.cgi?JCAMP=C67641&Index=0&Type=IR) and is unchanged apart from its line endings.

The file is JCAMP-DX, plain text: 24 header fields of the form `##NAME=value`, then a data block of 88 lines in the `(X++(Y..Y))` form, one wavenumber followed by ten stored integers per line. The header fields that fix what the numbers mean:

| Field | Value | Meaning |
|---|---|---|
| `XUNITS` | `1/CM` | wavenumber in per cm |
| `YUNITS` | `ABSORBANCE` | absorbance, unitless (AU) |
| `DELTAX` | `4.0` | spacing of the points within a line, per cm |
| `YFACTOR` | `0.000078659` | the stored integer times this is the absorbance |
| `NPOINTS` | `880` | number of points, 450 to 3966 per cm |
| `MAXY` | `0.78659` | largest absorbance, at 1738 per cm |

Cite the source as: Linstrom, P. J.; Mallard, W. G., Eds. *NIST Chemistry WebBook, NIST Standard Reference Database Number 69*; National Institute of Standards and Technology: Gaithersburg, MD; [doi:10.18434/T4D303](https://doi.org/10.18434/T4D303). The file carries the notice "Collection (C) 2018 copyright by the U.S. Secretary of Commerce on behalf of the United States of America. All rights reserved."; copyright in NIST Standard Reference Data is held under the Standard Reference Data Act, 15 U.S.C. 290e. This one record is redistributed here for teaching with that attribution. For any other use, take the file from the WebBook.

## Your own record, `<CAS number>-IR.jdx`

Section 2 of the activity has you download the gas-phase IR record of your assigned molecule from the same WebBook, which names the file after the CAS number. Keep it in this folder under that name. The repository ignores `*-IR.jdx` files here, so your download is never committed and `git pull` never touches it. The instructors hold copies of every assigned record under the same names, which is how your notebook runs when it is graded.
