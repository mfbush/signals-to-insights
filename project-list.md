# CHEM 427 project list

Each project below is a question, a public dataset and enough chemistry to start. Every dataset has been downloaded and loaded by the instructional team, and the first analysis named for each project has been run on it, so each one is feasible by the working draft on November 22. The answers are not given here: the question is yours to settle from the data. This list is a draft until Thursday, October 15, when the preferences survey opens on Canvas; a project may still change or be added before then.

Each project goes to one student. Rank your three preferred projects on the Canvas survey "CHEM 427 project preferences" by Sunday, November 1, and Matt assigns each of you one project by Tuesday, November 3, from your three wherever the choices allow. Each student works and submits alone. Your topic declaration, due Sunday, November 8, names the project you were assigned, loads the data from a relative path, and prints the number of rows, the column names and the units of the measured variable, as set out on the [final project page](final-project.md). Record the date you download the data, because you cite it with that access date.

## The projects at a glance

| # | Project | Measurement | Course methods | Download |
|---|---|---|---|---|
| 1 | Retention time from molecular structure | Liquid chromatography | Sessions 14, 15, 17, 18 | 6 MB |
| 2 | An HPLC calibration across gradient lengths | HPLC with diode-array detection | Sessions 8, 11, 12, 13, 14 | 53 MB |
| 3 | Collision cross section and chemical class | Ion mobility mass spectrometry | Sessions 9, 13, 14, 18 | 4 MB |
| 4 | How much signal a sugar calibration needs | Raman spectroscopy | Sessions 8, 11, 14, 17, 18 | 120 MB |
| 5 | Finding the varnish on a painting | Near-infrared hyperspectral imaging | Sessions 8, 9, 11, 15 | 145 MB |
| 6 | Identifying plastics pixel by pixel | Raman imaging | Sessions 8, 11, 15, 18 | 140 MB |
| 7 | Counting carbons from isotope patterns | High-resolution mass spectrometry | Sessions 9, 12, 13, 14 | 13 MB |
| 8 | Other vegetable oils in olive oil | ¹H NMR spectroscopy | Sessions 12, 13, 17, 18 | 4 MB |
| 9 | Perovskite nanocrystal synthesis read by absorbance | UV-Vis spectroscopy | Sessions 12, 13, 15, 18 | 3 MB |
| 10 | Phase transitions of potassium niobate | Powder X-ray diffraction | Sessions 12, 13, 14 | 1 MB |
| 11 | Nanoparticle size by three techniques | Atomic force and electron microscopy, SAXS | Sessions 9, 11, 12, 13, 14 | 95 MB |
| 12 | Hydrogen on platinum | Cyclic voltammetry | Sessions 9, 11, 12, 13, 14 | 17 MB |

The course methods column names the sessions whose methods the question needs. Session 4, on file formats, is needed by every project.

## 1. Retention time from molecular structure

**Question.** A Ridge or PLS model built on 10 to 20 molecular descriptors predicts reversed-phase retention time on one C18 method; after a straight-line recalibration, how much of that accuracy survives a change of organic modifier and gradient, and how does that compare with changing only the column?

**Data.** [RepoRT, the repository of retention times](https://github.com/michaelwitting/RepoRT), datasets 0252 (Waters BEH C18, water and acetonitrile), 0236 (the same method on an HSS T3 column) and 0262 (BEH C18, water and methanol, a 15 minute gradient). Each dataset folder holds a table of compounds with retention time in minutes and a table of 286 computed descriptors for the same compounds. Dataset 0252 has about 570 compounds. Kretschmer, F. et al., *Nat. Methods* **21**, 153 (2024), doi:10.1038/s41592-023-02143-z. License CC BY-SA 4.0.

**What you meet on loading.** The retention table and the descriptor table join on a compound ID. More than a third of the descriptors are empty or constant for every compound. Two compounds are stored as salts, and their descriptor values are off by orders of magnitude. Some compounds appear more than once.

**A first analysis for the draft.** The cross-validated error of a Ridge model on 0252, in minutes, against a straight line on one descriptor, the calculated logP.

**Chemical context.** In reversed phase a compound is retained by partitioning into the nonpolar stationary phase, so retention time rises with hydrophobicity, and logP is the single best predictor. Compounds that elute near the column dead time barely interact with the stationary phase, and descriptor models do worst on them. Methanol is a weaker eluent than acetonitrile, so the same compound elutes later in 0262.

## 2. An HPLC calibration across gradient lengths

**Question.** Does the calibration slope of each analyte depend on the length of the solvent gradient, beyond the uncertainty from replicate injections, and does the scatter about each calibration line come from the injections or from the standards?

**Data.** The Knoevenagel example set of [MOCCA, an open-source chromatography package](https://github.com/bayer-group/MOCCA) (branch `example-data`, file `knoevenagel.tar.bz2`). It holds standards of benzaldehyde, 4-methoxybenzaldehyde and 4-(dimethylamino)benzaldehyde at 4 concentrations, run on 5 gradient lengths from 0.5 to 2.5 minutes in two replicate series, with blanks for each. Each run is a matrix of absorbance in mAU against time and wavelength, 200 to 550 nm. Haas, C. P. et al., *ACS Cent. Sci.* **9**, 307 (2023), doi:10.1021/acscentsci.2c01042. License MIT.

**What you meet on loading.** The archive unpacks to about 1 GB, so extract only the calibration and blank runs. The CSV files are UTF-16 text, which a default `read_csv` call cannot read. The concentrations are not in the file names, which carry only a nominal code; the weighed concentrations are in the package's loader source, `src/mocca2/example_data/loaders.py`. The time axes differ slightly between runs, and the blank baseline drifts with the gradient.

**A first analysis for the draft.** For one analyte on one gradient: subtract the blank, integrate the peak, and fit a calibration line with the uncertainty on its slope.

**Chemical context.** The three aldehydes are the starting materials of the Knoevenagel condensations studied in the paper, and each absorbs in the UV at a different wavelength, so choose each analyte's wavelength from its spectrum where the blank is flat. The peaks are less than a second wide at 10 points per second, so where you place the integration limits changes the area. A longer gradient elutes the same compound later and in a different solvent composition.

## 3. Collision cross section and chemical class

**Question.** Does collision cross section scale with <i>m</i>/<i>z</i> by a different power law for nucleotides than for lipids and organic acids, and is the offset between traveling-wave and drift-tube instruments larger than the scatter about that power law?

**Data.** The [Unified CCS Compendium](https://zenodo.org/records/6860818), 1,983 ions with <i>m</i>/<i>z</i>, adduct, chemical class and a cross section in Å² measured by drift tube in nitrogen. Picache, J. A. et al., *Chem. Sci.* **10**, 983 (2019), doi:10.1039/C8SC04396E. License CC BY 4.0. For the instrument comparison, the source files of [C3SDB](https://github.com/dylanhross/c3sdb), 18,237 cross sections from 26 published sets, each labelled drift tube, traveling wave or trapped ion mobility. Ross, D. H., Cho, J. H., Xu, L., *Anal. Chem.* **92**, 4548 (2020), doi:10.1021/acs.analchem.9b05772. License MIT.

**What you meet on loading.** The two databases write adducts differently. One C3SDB file stores its numbers as text. The "organic acids" class includes peptides with charges up to +24. Matching a compound between the databases has to use <i>m</i>/<i>z</i>, adduct and name, and some <i>m</i>/<i>z</i> values match more than one compound. Some C3SDB sets may re-report the Compendium's own measurements.

**A first analysis for the draft.** A power-law fit of cross section against <i>m</i>/<i>z</i> for singly protonated ions in each class, with the uncertainty on each exponent.

**Chemical context.** The collision cross section is the orientation-averaged area an ion presents in collisions with the drift gas. For singly charged ions it grows more slowly than the 2/3 power of mass expected for spheres of constant density, and the exponent differs between classes because shape and packing change with size differently in each. Drift-tube values follow from the measured drift time, field and pressure, whereas traveling-wave values depend on a calibration against ions of known cross section.

## 4. How much signal a sugar calibration needs

**Question.** How does the PLS prediction error for each of four sugars scale with total integration time, from single 0.5 s spectra averaged 1 to 32 times to single 5 s spectra, does it follow the 1/√t expected for shot-noise-limited spectra, and where does it stop improving?

**Data.** [Raman_Sugars](https://github.com/Alvaro-FG/Raman_Sugars), Raman spectra of 245 aqueous mixtures of sucrose, fructose, maltose and glucose at 0 to 0.32 mol/L each, excited at 785 nm, 142 to 3685 cm⁻¹ in raw counts. Each mixture has 8 spectra at 5 s and 32 at 0.5 s. Fernandez Galiana, A., Raman_Sugars, GitHub repository, commit 2f68c20 (2024). License MIT. There is no paper, so cite the repository and the commit.

**What you meet on loading.** Each file has one column per spectrum, and the columns are not in the order of the metadata table. The metadata give each sugar as a volume of 1 M stock in µL, which you convert to concentration. Cosmic rays leave single-pixel spikes. The detector is weak above about 2500 cm⁻¹.

**A first analysis for the draft.** A PLS model for one sugar on the 5 s spectra, with its cross-validated error in mmol/L, where all the spectra of one mixture stay in the same fold.

**Chemical context.** Aqueous sugars have their Raman bands between about 400 and 1500 cm⁻¹, from C–O and C–C stretches and ring and skeletal bends, and the four sugars overlap heavily there, which is why a multivariate model is needed. For shot-noise-limited spectra the signal to noise ratio grows as the square root of the counts collected, i.e., of integration time. Repeat spectra of one mixture are not independent samples, so a model tested on a repeat of a training mixture looks better than it is.

## 5. Finding the varnish on a painting

**Question.** Where is the dammar varnish on a mock-up painting, located from its C–H absorption, is the difference in band area across the boundary larger than the variation between neighbouring regions, and does the band area map the varnish thickness?

**Data.** A [near-infrared hyperspectral image of a mock-up after Botticelli](https://zenodo.org/records/8143550): 384 × 410 pixels, 288 bands from 896 to 2502 nm, raw detector counts, with white and dark reference images for converting to reflectance. The panel is egg tempera on a gypsum ground, and dammar varnish covers part of the surface. Rocha de Oliveira, R., Malegori, C., Sciutto, G., Oliveri, P., *Chemom. Intell. Lab. Syst.* **240**, 104918 (2023), doi:10.1016/j.chemolab.2023.104918. License CC BY 4.0.

**What you meet on loading.** Each image is an ENVI pair: a text header that gives the dimensions, byte order, band interleave and wavelengths, and a binary file of 16-bit integers that `np.fromfile` reads once you know the layout. Reflectance is the sample minus the dark reference, divided by the white minus the dark. The first bands carry almost no light. The image includes the scan stage, bare wood and a gypsum strip besides the painting. No file says which part is varnished.

**A first analysis for the draft.** Calibrate to reflectance, report the noise in each band from the dark frames, and make a PCA score image of the painted area.

**Chemical context.** Dammar is a triterpenoid resin rich in C–H bonds, and it absorbs at the first overtone of C–H stretching near 1700 nm and at C–H combination bands near 2300 nm. The egg binder and the gypsum absorb in the near infrared as well, so the varnish shows as extra absorbance on a spectrum shared with the paint, not as a new band. Neighbouring pixels are not independent measurements, which matters for any test that counts pixels.

## 6. Identifying plastics pixel by pixel

**Question.** Trained on Raman maps of single polymers and tested on maps of mixtures it has never seen, how accurately does a classifier on PCA scores label each pixel, and at what signal to noise ratio does its accuracy fall below 90%?

**Data.** [RaMPI, Raman maps of plastics](https://borealisdata.ca/dataset.xhtml?persistentId=doi:10.5683/SP3/8UQQQN): 34 maps of 14 plastics, 32,897 pixel spectra, each labelled by hand as a polymer or as blank. Each map is a tab-separated file with the label in the first column and CCD counts at 1,017 Raman shifts from 710 to 1827 cm⁻¹. About 13 maps, including 9 single polymers and 4 mixtures, make a working set of 140 MB. Hogan, U. E. et al., *Sci. Data* (2026), doi:10.1038/s41597-026-07103-8. License CC BY 4.0.

**What you meet on loading.** The files carry no pixel coordinates. The rows are in raster order, so rebuilding the image means finding the map's width. Each map has its own slightly shifted wavenumber axis. Some spectra carry cosmic-ray spikes. One mixed map is scaled 0 to 1 instead of in counts. Some polymers in the mixtures have no single-polymer map.

**A first analysis for the draft.** PCA on the single-polymer maps, then a classifier on the PCA scores, with its accuracy on held-out maps.

**Chemical context.** Raman bands are set by a polymer's bonds and repeat unit, so C–H, C=O, C–Cl and aromatic ring modes fingerprint the plastic. A fluorescent background adds shot noise but no Raman signal, so a pixel can have many counts and still a low signal to noise ratio. ABS is a copolymer that contains styrene, so its spectrum shares bands with polystyrene.

## 7. Counting carbons from isotope patterns

**Question.** Do an electron-ionization time-of-flight, an electron-ionization Orbitrap and an electrospray Orbitrap instrument report the M+1/M intensity ratio that each ion's formula predicts, and does any deficit shrink as the ion signal grows?

**Data.** MS1 records of known compounds from the [MassBank-data repository](https://github.com/MassBank/MassBank-data), release 2026.03, from three contributors: MSSJ (EI time-of-flight), NILU (EI Orbitrap) and NAIST (ESI Orbitrap), 745 usable spectra. Each record is a text file with the formula, instrument details and a peak list of <i>m</i>/<i>z</i> and intensity. MassBank consortium, MassBank-data release 2026.03, Zenodo (2026), doi:10.5281/zenodo.3378723. Licenses are set per record: keep MSSJ and NILU records marked CC BY and NAIST records marked CC BY-SA. The theory comes from NIST's [Atomic Weights and Isotopic Compositions](https://www.nist.gov/pml/atomic-weights-and-isotopic-compositions-relative-atomic-masses), Standard Reference Database 144, doi:10.18434/T4Z01F.

**What you meet on loading.** The records are key and value lines followed by a peak block, so you write a short parser. Each record states its own license and spectrum type, which you filter on. Some spectra have no molecular ion. The Orbitrap resolves peaks at the same nominal mass (¹³C and ¹⁵N), which you sum. In electron ionization the [M−H]⁺ ion carrying one ¹³C falls under M⁺.

**A first analysis for the draft.** Compute each formula's theoretical isotope pattern by convolving the element patterns, and compare measured and predicted M+1/M for one instrument.

**Chemical context.** Carbon is 1.07% ¹³C, so each carbon atom adds about 1.1% of the monoisotopic intensity to M+1, and for compounds of C, H, N and O the M+1/M ratio is mostly a carbon count. Chlorine is 24.2% ³⁷Cl and bromine 49.3% ⁸¹Br, both 2 u heavier than the light isotope, so the M+2 peak counts halogen atoms. The natural variation of ¹³C abundance sets a floor on how precisely any instrument can count carbons.

## 8. Other vegetable oils in olive oil

**Question.** Which of eight vegetable oils can ¹H NMR quantify when blended into olive oil, does a one-band calibration on the bis-allylic signal fail for the oils whose linoleic content matches olive oil's, and does PLS on the whole spectrum succeed where it fails?

**Data.** [¹H NMR fingerprints of olive oil blends](https://zenodo.org/records/14747548): 450 spectra of olive oils and of blends with 0 to 100% of another vegetable oil at 12 levels, already phased, referenced and binned at 0.02 ppm from 0.01 to 10.99 ppm. One Excel file, 3.7 MB. Alonso-Salces, R. M. et al., *Food Chem.* **366**, 130588 (2022), doi:10.1016/j.foodchem.2021.130588. License CC BY 4.0.

**What you meet on loading.** The data are in one `.xlsx` workbook, which `pd.read_excel` reads; the course environment includes the openpyxl package it needs. There is no codebook, so the oil codes have to be decoded from the paper's methods; an open copy of the manuscript is in the [Universitat de Barcelona repository](https://hdl.handle.net/2445/180440). Some sample names repeat. The bins between 4.09 and 4.27 ppm are missing: the authors scaled every spectrum to that half of one glycerol signal, then removed it. Because the spectra are already processed, the work starts at integration.

**A first analysis for the draft.** Integrate the bis-allylic band against a glycerol signal to get the linoleic fraction of each pure oil, then fit a calibration line against blend percentage for one oil.

**Chemical context.** In a triacylglycerol the bis-allylic CH₂, i.e., the CH₂ between two double bonds, resonates near 2.77 ppm and exists only in chains with two or more double bonds, so its integral divided by a glycerol signal of known proton count gives the linoleic fraction with no external standard. Olive oil is mostly oleic acid, with one double bond, whereas sunflower oil is mostly linoleic acid, with two. High-oleic sunflower oil has a fatty acid profile close to olive oil's and is harder to detect.

## 9. Perovskite nanocrystal synthesis read by absorbance

**Question.** Which precursor concentrations set the thickness of the cesium lead bromide nanoplatelets a synthesis makes, does a model that predicts the product survive a test on whole plates it has never seen, and how does the exciton energy depend on thickness?

**Data.** [High-throughput synthesis of CsPbBr₃ nanocrystals](https://doi.org/10.6078/D1XT4F), 1,351 robotic syntheses on 15 plates. Each row has the reagent volumes in µL, concentrations in mM, temperature, an absorbance spectrum from 250 to 700 nm in optical density, and an emission spectrum. Dahl, J. C., Wang, X., Chan, E. M., Alivisatos, A. P., Dryad (2020), doi:10.6078/D1XT4F; article in *J. Am. Chem. Soc.* **142**, 11915 (2020), doi:10.1021/jacs.0c04997. License CC0.

**What you meet on loading.** The ID column has no header and encodes plate and well. Absorbance is clipped at 4.0 below about 300 nm in most spectra. The metadata PDF gives the wrong file names. Some columns duplicate others.

**A first analysis for the draft.** Find the absorption peak positions of the nearly pure samples of each product and convert them to energies in eV.

**Chemical context.** Lead bromide perovskites form three-dimensional CsPbBr₃ nanocrystals and also two-dimensional nanoplatelets that are n layers of PbBr₆ octahedra thick. Confinement in the thin dimension moves each platelet's sharp exciton absorption to higher energy as n falls, so the absorption spectrum reads out which products a synthesis made. Which product forms depends on the ratio of cesium, lead and bromide and on the balance of oleylamine and oleic acid ligands.

## 10. Phase transitions of potassium niobate

**Question.** At what temperatures, with uncertainty, do the two structural phase transitions of KNbO₃ occur on heating and on cooling, is the hysteresis between them larger than the uncertainty in temperature, and how does the thermal expansion change across each transition?

**Data.** [Thermal evolution of the crystal structure of KNbO₃](https://doi.org/10.5061/dryad.td26kr2): 103 laboratory powder patterns with Cu Kα radiation from 19° to 60° 2θ in counts, on heating from 30 to 650 °C and cooling back in 10 °C steps, with the authors' refined lattice parameters and a furnace temperature calibration. Skjærvø, S. L. et al., Dryad (2018), doi:10.5061/dryad.td26kr2; article in *R. Soc. Open Sci.* **5**, 180368 (2018), doi:10.1098/rsos.180368. License CC0.

**What you meet on loading.** The patterns are in Bruker's binary RAW format, version 1.01, which no course library reads: the file opens with the text `RAW1.01`, a 712 byte file header follows, and each scan range has a 304 byte header, then a supplementary header whose length the range header states, then its counts as 32-bit floats, so you write a reader with Python's `struct` module. The furnace setpoint is not the sample temperature; a calibration in an Excel workbook, which `pd.read_excel` reads, converts one to the other. Some cooling setpoints are off the 10 °C grid.

**A first analysis for the draft.** Track the splitting of one reflection near 45° 2θ through the heating series and locate the two transitions.

**Chemical context.** KNbO₃ is a perovskite oxide that is orthorhombic at room temperature, tetragonal at intermediate temperature and cubic at high temperature. Below the cubic phase it is ferroelectric because Nb⁵⁺ sits off the centre of its NbO₆ octahedron, and the splitting of reflections that are single in the cubic phase measures that distortion. Both transitions are first order, which is why they occur at different temperatures on heating and on cooling. Each reflection is a Kα₁ and Kα₂ doublet, which a peak fit has to include.

## 11. Nanoparticle size by three techniques

**Question.** Does the height measured by atomic force microscopy read silica nanoparticles smaller than electron microscopy and small-angle X-ray scattering do, while it reads gold nanoparticles correctly, by more than the combined uncertainty, and can your own particle segmentation reproduce the expert-annotated size distributions?

**Data.** The image database of the nPSize reference-material project on Zenodo: 95 [AFM height maps](https://zenodo.org/records/5578927) of 512 × 512 pixels in nm at 5.87 nm per pixel, 40 [SEM images](https://zenodo.org/records/5578878) at 1.4 to 1.9 nm per pixel, 11,227 [expert-annotated particles](https://zenodo.org/records/5577401), [SAXS curves](https://zenodo.org/records/5886834) and the [validation report](https://zenodo.org/records/7016466) with the reference sizes. pollen-metrology.com, nPSize image and annotation records, Zenodo (2021), doi:10.5281/zenodo.5578927, doi:10.5281/zenodo.5578878 and doi:10.5281/zenodo.5577401; Deumer, J., Gollwitzer, C., Zenodo (2022), doi:10.5281/zenodo.5886834; Bartczak, D., Hodoroaba, V.-D., Zenodo (2022), doi:10.5281/zenodo.7016466. Licenses CC0 for the images and annotations, CC BY 4.0 for the SAXS data and the report.

**What you meet on loading.** The maps are `.h5` files, but each holds one uncompressed array after a 2048 byte header, which numpy reads directly. The material and pixel size of each image are only in the annotation file and the file names. The report's section 2 text swaps the labels of the silica materials nPSize12 to 14. Its Table 1 and Tables 12 and 13 agree with the annotated sizes: 12 and 13 are bimodal, 14 has one mode. Start with nPSize01 (gold) and nPSize10 (silica); the bimodal silica nPSize12, with 4 AFM maps, is an extension. The SEM images carry a data bar that has to be cropped.

**A first analysis for the draft.** Segment the particles in the AFM maps of one material, take each particle's maximum height, and report the median size with a bootstrap confidence interval.

**Chemical context.** nPSize01 is citrate-stabilized gold spheres of about 30 and 60 nm mixed by particle number, and nPSize10 is silica spheres of about 50 nm. The AFM height of a rigid sphere above a flat substrate is its diameter and is not widened by the tip, whereas SEM measures a projected area and SAXS measures the particle form factor, whose first minimum for a sphere of radius R falls where q times R is 4.493. A size that three independent techniques agree on is the reference value a fourth is judged against.

## 12. Hydrogen on platinum

**Question.** Does the charge for hydrogen adsorption on Pt(111) agree across 10 laboratories once the integration limits and the double-layer correction are chosen the same way, and on stepped platinum surfaces does the charge at the steps equal one hydrogen atom per step atom?

**Data.** [echemdb electrochemistry data](https://zenodo.org/records/21412548), version 0.9.2: 358 cyclic voltammograms from 93 papers, each a CSV of time, potential and current with a JSON file describing the electrode, crystal face, electrolyte, scan rate, reference electrode and source figure. Most curves were digitized from published figures. Engstfeld, A. et al., echemdb electrochemistry data v0.9.2, Zenodo (2026), doi:10.5281/zenodo.21412548. License CC BY 4.0. Cite the source paper of each curve you use as well.

**What you meet on loading.** On Windows the zip does not extract, because its paths are too long, so read the files from inside the zip with the `zipfile` module. Current is given in several units, and some curves in amperes with no electrode area. The curves use 14 different reference electrodes. Digitized points are in the order they were traced, not in time order, so you identify each sweep by the sign of its current.

**A first analysis for the draft.** For the Pt(111) curves in 0.1 M perchloric acid, subtract the double-layer current and integrate the hydrogen region to a charge in µC cm⁻².

**Chemical context.** Between about 0.05 and 0.40 V against the reversible hydrogen electrode, Pt(111) in acid adsorbs hydrogen by the reaction H⁺ + e⁻ ⇌ H(ads), so the integrated charge divided by the electron charge counts adsorbed atoms. One hydrogen on each of the 1.5 × 10¹⁵ surface atoms per cm² of Pt(111) would give 240 µC cm⁻². Stepped surfaces cut at a small angle to (111) have terraces a known number of atoms wide separated by steps, and hydrogen at the steps adsorbs in a sharp peak near 0.12 V.
