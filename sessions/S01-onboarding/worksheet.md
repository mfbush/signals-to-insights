# Session 1 worksheet: What is chemical data?

This worksheet needs no code and no install, so you can read it on GitHub in a browser. Work with the student next to you, and each of you submits your own answers in the Canvas assignment "S1 worksheet" by 11:59 pm on Friday, October 2. It is scored 0 or 1 for completion: 1 point when all six excerpts and both questions in part 4 have an answer. A late submission still earns the point until 11:59 pm on Wednesday, October 7, the night before session 3, and earns 0 after that.

The worksheet has four parts and takes about 60 minutes: part 1 (5 minutes) sets out the three properties you classify by, part 2 (30 minutes) is the six excerpts, part 3 (10 minutes) compares your answers with another pair, and part 4 (15 minutes) asks two questions about what you found.

## Part 1. Three properties of a data file

An instrument never records the chemical quantity you want. A chromatograph records a detector signal many times a second, and the amount of each compound is inferred afterward from the area under a peak. A mass spectrometer records how many ions arrive at each mass-to-charge ratio, i.e., m/z, and the identity of a molecule is inferred from which m/z values appear. Each instrument converts the sample into a signal in a fixed sequence of steps, and the file it writes keeps some information and has already lost the rest.

To know what you can do with a file, you need three properties.

1. **Dimensionality**, i.e., how many axes the signal depends on. A signal that depends only on time or only on m/z is one-dimensional. An image with a full spectrum at every pixel depends on x position, y position, and wavelength or m/z, so it is three-dimensional, which is called a data cube.
2. **The physical meaning of each axis**, with its unit: time, wavelength, m/z, or position.
3. **The chemical quantity the signal encodes**: how much of a compound is present, which compound it is, where it is in the sample, or a combination of these.

Most of the files you will meet are one of three kinds: a time series (signal against time), a spectrum (signal against wavelength, frequency, or m/z), or a data cube. The methods later in the course depend on which kind you have. A smoothing function written for a spectrum and applied along the wrong axis of a data cube runs without an error and averages neighboring pixels instead of neighboring wavelengths.

## Part 2. Six excerpts

Each excerpt below is the header and a few lines of a file exported from an instrument, with the instrument's name and model removed. Rows and columns left out are shown as `...`. The instruments come from three classes: two chromatographic, two mass spectrometric, and two imaging.

For each excerpt, answer four questions in the Canvas assignment:

1. How many dimensions does the signal have?
2. What does each axis measure physically, and in what unit?
3. What chemical quantity does the signal encode?
4. Which of the three instrument classes produced it, and what in the excerpt told you?

### Excerpt A

```text
# Sample: std_mix_03    Acquired: 2026-08-14 10:22
# Sampling rate: 20 Hz    Signal units: pA
Time (min),Signal (pA)
...
4.3000,15.0
4.3008,27.6
4.3017,68.4
4.3025,139.6
4.3033,190.7
4.3042,166.7
4.3050,94.8
4.3058,39.6
...
```

### Excerpt B

```text
# Sample: std_mix_03    Injection volume: 10 uL
# Detection: 254 nm, bandwidth 4 nm    Sampling rate: 2 Hz
Time (min),Absorbance (mAU)
...
6.1000,1.8
6.1083,9.6
6.1167,38.2
6.1250,71.5
6.1333,64.0
6.1417,30.9
6.1500,8.1
...
```

### Excerpt C

```text
# Scan 1    Polarity: positive    Scan range: m/z 50.0 to 500.0
# Centroided peak list
m/z,Intensity (counts)
...
195.0877,2410000
196.0911,248000
197.0934,22000
217.0696,312000
...
```

### Excerpt D

```text
# Chromatogram type: TIC    Polarity: positive
# Summed over m/z 100.0 to 1000.0    Scan interval: 0.5 s
Time (min),Intensity (counts)
...
8.4000,1.12E+07
8.4083,1.87E+07
8.4167,3.95E+07
8.4250,5.21E+07
8.4333,4.46E+07
8.4417,2.30E+07
8.4500,1.31E+07
...
```

### Excerpt E

This is a header file. It describes a separate binary file of 68,812,800 bytes that holds the numbers.

```text
ENVI
description = {tablet_scan_07}
samples = 320
lines = 240
bands = 224
header offset = 0
data type = 4
interleave = bil
byte order = 0
wavelength units = Nanometers
wavelength = {400.00, 402.47, 404.93, 407.40, ..., 947.53, 950.00}
```

Here `samples` is the number of pixels across, `lines` the number of pixels down, `bands` the number of wavelengths, and `data type = 4` means each number is stored in 4 bytes.

### Excerpt F

```text
# Raster: 150 x 100 positions, step 50 um
# Each position: m/z 150.0 to 1000.0, 8500 bins
x,y,mz_150.0,mz_150.1,mz_150.2,...,mz_152.0,mz_152.1,...,mz_999.9
1,1,0,12,0,...,1840,6210,...,0
2,1,0,9,3,...,1905,6388,...,0
3,1,4,0,0,...,1770,5942,...,2
...
```

## Part 3. Compare with another pair

Find another pair and compare your answers excerpt by excerpt. For each excerpt where the two pairs disagree, decide which property you disagree on: dimensionality, an axis, or the chemical quantity. Change your Canvas answers if the other pair convinces you, and note in the answer that you changed it and why.

## Part 4. Two questions

Answer each in two to three sentences in the Canvas assignment.

1. One of the six files is not what the instrument recorded but a summary computed from it. Which excerpt is it, what did the instrument record, and what can you no longer do with the exported file that you could have done with the recording?
2. Which excerpt was hardest for you to classify, and was it the dimensionality, an axis, or the chemical quantity that was unclear? Name one thing that would go wrong later in an analysis if you had classified it wrong.
