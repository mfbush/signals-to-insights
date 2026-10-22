# Data for session 10

Two real files and one table of seeds. `fid` and `acqus` are a ¹H free induction decay of ethanol and the spectrometer's parameters for it, from the Biological Magnetic Resonance Data Bank; both are in the repository, so nothing is downloaded in class. `records.csv` gives each student's record for sections 2 and 3, which the notebook builds from `fid` and a seed.

## The ethanol FID: `fid` and `acqus`

### Source

Biological Magnetic Resonance Data Bank (BMRB), entry bmse000297, ethanol, experiment set01, 1D ¹H ([doi:10.13018/BMSE000297](https://doi.org/10.13018/BMSE000297)), files `fid` and `acqus` from the entry's `nmr/set01/1H/` folder on the BMRB metabolomics server, accessed 2026-10-10. BMRB disseminates its data in the public domain and asks users to acknowledge BMRB, which we do here and in the notebook. The two files are copied unchanged: `fid` is 131,072 bytes, SHA-256 `2d4eb82cc62be0897d0b583625cecf097c2ac7211eeb00b4b1132da3e3e0ad64`, and `acqus` is 6,596 bytes, SHA-256 `7514424ca61b297a9f6d7ba915553fad4592c7606132ad9374cc8e39f478731b`.

### The sample and the acquisition

100 mM ethanol in D₂O with 50 mM sodium phosphate, 500 µM sodium azide and 500 µM DSS as the shift reference, pH 7.4, 298 K as BMRB records it (`acqus` has `TE= 306`), on a Bruker DMX 400 spectrometer, one scan with the pulse program `zg`.

### The decay itself, `fid`

A binary file with no header: 32,768 signed 32-bit integers, big-endian, which pair up as the real and imaginary parts of 16,384 complex points, real first. The notebook reads it with `np.fromfile(path, dtype=">i4")`. The points are 1 / `SW_h` apart, 208 µs, so the record lasts 3.408 s. The spectrometer's digital filter delays the signal by 72.138 points at these settings and takes about 10 more to rise, so the decay peaks at point 82, not 0; `remove_filter_delay` in section 1 removes the delay.

### The parameter file, `acqus`

A text file in Bruker's JCAMP-DX parameter format, one parameter per line in the form `##$NAME= value`. The notebook's `read_acqus` reads every `##$` line into a dictionary. Those it uses:

| Parameter | Value | What it is |
|---|---|---|
| `TD` | 32768 | values in `fid`, real and imaginary counted separately |
| `SW_h` | 4807.69 | spectral width, Hz: the window the spectrum covers |
| `SFO1` | 400.131880611 | the spectrometer frequency for ¹H, MHz, which converts ppm to Hz |
| `O1` | 1880.611 | the carrier, Hz above the reference frequency, here at 4.700 ppm |
| `BYTORDA` | 1 | byte order: 1 is big-endian |
| `DTYPA` | 0 | data type: 0 is 32-bit integer |
| `DECIM`, `DSPFVS` | 32, 12 | the digital filter's settings, which set its delay |

## The records: `records.csv`

Each student's record is the real FID with two changes made from a seed: an extra exponential decay drawn from 0 to 2 Hz, and at least 0.2 Hz in every record, the broadening a poorer shim gives, and complex noise. `make_record` in section 2 builds it, so the file holds only two columns, `record` and `seed`, for 30 records, `record_01` to `record_30`. Every run of the notebook rebuilds the same record from the same seed.

The seeds were chosen by the generator `make_records.py`, which the instructors keep, trying seeds from 427 upward. A seed was kept only if the call the notebook asks for is clear under both of section 3's treatments: the larger valley between the triplet's lines is at most 0.77 of the outer line at the record's call and at least 0.83 one step shorter, so no call sits on the 0.8 line. A rerun rewrites the file byte for byte.
