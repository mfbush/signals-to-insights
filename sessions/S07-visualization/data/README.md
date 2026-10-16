# Data for session 7

Two datasets of SWIR band images. `apr22/` and `apr22_spectra.csv` are real: a crop of an aerial survey of plastics laid on grass, and mean spectra over the whole survey, for section 1. `batch/` and `band_pairs.csv` are simulated from those spectra: a test batch of known plastic flakes on a sorting belt and the band pairs assigned in class, for sections 2 and 3. Nothing is downloaded during the session.

## The April 2022 survey: `apr22/` and `apr22_spectra.csv`

### Source

M. Balsi, M. Moroni, and S. Bouchelaghem, "SWIR hyperspectral data cubes for plastics detection in the environment", Mendeley Data, version 1, 2025, [doi:10.17632/25hfz5c8dt.1](https://doi.org/10.17632/25hfz5c8dt.1), released under CC BY 4.0, accessed 2026-10-01. The files used are `cube_Apr22.zip` and `masks_Apr22.zip`. The survey and its camera are described in M. Balsi, M. Moroni, and S. Bouchelaghem, "Plastic Litter Detection in the Environment Using Hyperspectral Aerial Remote Sensing and Machine Learning", *Remote Sensing* 17 (2025) 938, [doi:10.3390/rs17050938](https://doi.org/10.3390/rs17050938), whose data statement cites a record of the same title, [doi:10.17632/y8cvcs8tt5.1](https://doi.org/10.17632/y8cvcs8tt5.1).

The files here are changed from the deposit, as the license asks us to say: the band images are cropped and saved as PNG, the PVC mask is cropped and thresholded, and `apr22_spectra.csv` is computed from the full bands and masks. The script that does this, `fetch_swir.py`, is kept by the instructors.

### The survey

A push-broom SWIR camera on a drone flew 7 to 15 m above small heaps of plastic objects laid on grass. The paper gives pixels 1 to 2 cm across the flight direction and no single value for this survey. The camera records 81 bands from 900 to 1700 nm in steps of 10 nm, and the deposit says that the bands from 900 to 930 nm are empty. Each band is one 8-bit JPEG of 7116 by 2050 pixels, a mosaic of flight lines stitched together, with three equal color channels. The values are the camera's digital numbers (DN), a raw signal that includes the sunlight's spectrum and the air between the drone and the ground. They are not reflectance.

### The crop, `apr22/`

`sequence_1_SWIR_fl01500_1659_0900.png` to `sequence_1_SWIR_fl01500_1659_1700.png` are the 81 bands, named as in the deposit, each 400 by 1085 pixels: rows 650 to 1049 and columns 965 to 2049 of the mosaic. The crop holds one PVC object, grass, and the edge of the mosaic. Each PNG has one channel and is lossless, so it holds exactly the values the deposit's JPEG decodes to, including the smoothing of fine detail that JPEG compression causes. `matplotlib.image.imread` returns an 8-bit PNG as fractions of 255, so multiply by 255 to get digital numbers. Four quirks matter for the session:

- 900 and 910 nm are zero everywhere, 920 nm reaches 2 DN and 930 nm reaches 4 DN.
- 16.9% of the pixels are 0 at 1250 nm: they lie outside the mosaic and were never measured.
- A few pixels at the mosaic's edge give band ratios far from the rest, up to 19.0 for 1200 nm over 1250 nm.
- Faint stripes run down the crop, along the flight lines the mosaic was stitched from.

`03_PVC.png` is the deposit's PVC mask over the same crop, 255 inside and 0 outside, thresholded at 127 of 255 because the deposit's masks are JPEGs with soft edges. The mask was drawn loosely around the object and holds 78,436 pixels, many of them grass.

### The spectra, `apr22_spectra.csv`

One row per band, 900 to 1700 nm. `wavelength_nm` is the band, and `grass`, `PET`, `PE`, `PVC`, `PP`, and `PS` are each material's mean signal in DN over its object pixels in the whole survey. Grass is the deposit's background mask outside its all-materials mask, 8,055,853 pixels. A polymer's object pixels are the pixels of its mask that are brighter at 1100 nm than the 99th percentile of grass, 135 DN, which keeps the object and drops the grass the mask was drawn around: 1,573 for PET, 40,412 for PE, 9,179 for PVC, 2,019 for PP, and 30,537 for PS. PET and PP keep few pixels because their objects are barely brighter than grass at 1100 nm, so their spectra may carry more grass than the others do. Every spectrum dips near 1130 nm and from 1350 to 1450 nm, where water vapor in the air absorbs.

## The test batch: `batch/` and `band_pairs.csv`

### What it is

A sorting plant checks its display by running known flakes past the camera. The test batch is such a check, simulated by the generator `make_batch.py`, which the instructors keep, with seed 427; a rerun rewrites every file byte for byte. It holds 72 flakes, 40 PET, 8 PVC, 12 PE, and 12 PP, from 23.3 to 48.0 mm long, on a belt 400 mm along and 800 mm across, imaged at 2.0 mm per pixel.

What is measured and what is modeled:

- Each flake's spectrum is its polymer's spectrum in `apr22_spectra.csv`, measured in the survey.
- Each flake has its own brightness, for how it lies and the light it catches, and a band ratio cancels it. Each flake also has its own thickness, which deepens its absorption bands as the Beer-Lambert law does, and a band ratio does not cancel it. Both are modeled.
- The belt is modeled, not measured: flat and dark, a tenth of the brightest survey signal at each band, because sorting belts are usually black rubber that reflects little SWIR. Its median at 1100 nm is 15.0 DN.
- 32 of the flakes catch a glint, a spot where the lamp reflects off the surface. A glint carries the lamp's spectrum and is clipped at 255 DN wherever the lamp is bright. Its brightness is modeled.
- Pixels at a flake's edge mix the flake and the belt, every pixel carries a little noise, and values are rounded to 8 bits.
- The flakes inherit the survey's water-vapor dips near 1130 nm and from 1350 to 1450 nm, which would be much weaker for a camera a meter above a belt.

### The files

`test_batch_0950.png` to `test_batch_1700.png` are the 76 bands, 950 to 1700 nm in steps of 10 nm, each 200 by 400 pixels, read the same way as the crop. `PET.png`, `PVC.png`, `PE.png`, and `PP.png` are the masks, one per polymer, 255 inside and 0 outside. They are drawn generously, as the survey's masks are: a pixel is in a polymer's mask if any part of a flake of that polymer covers it, so the masks include the flakes' edges and their glints.

`band_pairs.csv` has the columns `pair`, `numerator_nm`, and `denominator_nm`: 36 band pairs, `pair_01` to `pair_36`, one assigned to each student in class and the rest spares. The generator `make_band_pairs.py`, which the instructors keep, chose them from the bands outside the water-vapor dips so that every pair separates PET from PVC in this batch.
