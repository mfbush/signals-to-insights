# Session 4: Chemical data, formats, and structures

Tuesday, October 13. From today the assistant is part of every activity and the judgment cell is scored.

## Learning objectives

By the end of this session you can:

1. Read a JCAMP-DX file as a document: name its header fields, its data block, and the five fields that fix what the numbers mean.
2. Parse the header into a dictionary with `open()`, string slicing and `.get()`, and expand the compressed data block into wavenumber and absorbance arrays.
3. Check a parsed spectrum against the file's own consistency fields and say which check catches which reading mistake.
4. Name what the file records and what it does not, and the question a collaborator could not answer without it.

## 1. A data file is a document

Session 2's peak list was a CSV with a header row and two columns, m/z and intensity in counts, and to use it you had to know what the file never said: which instrument produced it and with what settings, who ran it and when, and the threshold that separated a peak from noise, which you chose yourself. A chemical data format is designed to carry that knowledge inside the file. Every well-designed one holds three layers. The measurement values are the first. The acquisition metadata, i.e., the instrument, its settings and the units, is the second, and without it two measurements of the same sample cannot be compared. The provenance, i.e., who measured what, when, and from which sample, is the third, the layer most often missing and hardest to recover. Today's file carries the first two and part of the third, and the activity shows you what each layer is worth.

## 2. JCAMP-DX, read by hand

Today's file is the gas-phase infrared spectrum of acetone from the NIST Chemistry WebBook, in JCAMP-DX, the plain-text exchange format that spectrometer software has written since 1988. Its first 25 lines are the header: 23 fields, one per line as `##NAME=value`, plus two lines that continue the owner's notice. The fields give the title, the CAS registry number, `##STATE=gas`, the units of both axes, and the numbers that describe the data block. The block that follows is 88 lines like this one, the first:

```
450.0 40 76 71 59 67 74 97 132 180 202
```

To read it, you need three header fields. `##XYDATA=(X++(Y..Y))` says that each line starts with one wavenumber and continues with the values at that wavenumber and at the ones after it. `##DELTAX=4.0` says the spacing, so the ten values on this line sit at 450, 454, 458 and so on to 486 per cm. `##YFACTOR=0.000078659` says that the stored numbers are integers to be multiplied by that factor: the first value is 40 times 0.000078659 = 0.003146 AU, which is the header's own `##FIRSTY=0.003146`. The largest integer in the block is 10000, at 1738 per cm, and 10000 times the factor is 0.78659 AU, the header's `##MAXY`. NIST scales every record so that its maximum stores as 10000, which is why `YFACTOR` is `MAXY` divided by 10,000. Ten values per line and 88 lines give 880 points, the header's `##NPOINTS=880`, from `##FIRSTX=450.0` to `##LASTX=3966.0`.

So a data line is not a point, and the integers are not absorbances. That is the whole reason to read the header first.

## 3. Parsing it with `open()`, slicing and a dictionary

To turn the header into something code can use, read the file with `open()`, which gives you every line as a string, and build a dictionary. For a header line, `line[2:]` slices off the `##`, and `split("=", 1)` divides what is left at the first `=` into the field name and its value, so `##DELTAX=4.0` becomes the key `DELTAX` with the value `"4.0"`. The two lines under `##OWNER=` do not start with `##`; they continue the copyright notice, and the parser skips them. Once the loop reaches `XYDATA`, every later line is data until `##END=`.

Two ways to read a dictionary: `header["DELTAX"]` returns the value and raises `KeyError` if the field is absent, whereas `header.get("RESOLUTION")` returns `None` for an absent field. Every value is text until `float()` converts it, the header's included. The activity builds the expansion of the block in four cells, then wraps it as `read_jcamp(path)` so that your own file, in section 2, takes one line.

## 4. The checks a file carries

The header holds three numbers that any correct reading of the block must reproduce: `NPOINTS`, the count; `LASTX`, the last wavenumber; and `MAXY`, the largest value. The expanded reading of acetone gives 880 points, a last wavenumber of 3966 and a maximum of 0.78659, all three matching. These checks matter because the most natural wrong reading looks right. Asked to load a `.jdx` file, a first attempt, a person's or an assistant's, treats each line as one point, the first number as x and the second as y, which is what `np.loadtxt` on the block gives when you keep the first two of its eleven columns. For acetone that reading has 88 points, ends at 3930 per cm, and puts the strongest band at 1730 per cm with 0.684 AU instead of 1738 per cm with 0.787 AU, because it keeps one absorbance in ten and the top of the carbonyl band, the part above 0.7 AU, spans only 12 per cm, from 1734 to 1746, less than the 40 per cm between line starts. Against the header it fails all three checks. For a molecule whose strongest band is a sharp feature the miss is larger: the one-point-per-line reading can land on a different band altogether, hundreds of per cm away, and still look like the spectrum.

To see what the 8 per cm costs, consider an analyst who decides whether a batch is the compound on its label. The analyst compares the batch's infrared bands with those of a reference spectrum, and the European Pharmacopoeia requires the bands to correspond in position, with the wavenumber scale of an FT-IR instrument held within 1.0 per cm. A reference read one point per line moves acetone's carbonyl band by eight times that tolerance, enough to fail a genuine batch and delay the medicine made from it.

Although a plot that looks like a spectrum is reassuring, the file's own numbers are the test, so run the checks before you report anything from a parsed file.

## 5. What the file does not say

Read the header for what is absent as well as what is present. `DELTAX` is the spacing between points, not the resolution of the instrument, and the NIST/EPA records give no `RESOLUTION`, no path length, no pressure beyond `gas`, no instrument and no date, so their absorbances cannot be compared between records as concentrations. The Coblentz Society records, which three of you will download, give all five: `##RESOLUTION=4` or `2`, a `STATE` that names the pressure, such as "GAS (150 mmHg DILUTED TO A TOTAL PRESSURE OF 600 mmHg WITH N2)", a `PATH LENGTH`, a `SPECTROMETER/DATA SYSTEM` and a `DATE`. They also differ in units: they store transmittance, where the strongest band is the smallest value, and absorbance is minus the logarithm base ten of transmittance, $A = -\log_{10} T$. A few store the x axis in micrometers, where the wavenumber in per cm is 10,000 divided by the wavelength.

For contrast, mzML, the open format for mass spectrometry data, records each scan as an XML element whose metadata lines carry a controlled vocabulary, so that `ms level` is always the term with accession `MS:1000511` whatever the instrument, with units stated on each value. Its data arrays are base64-encoded binary, not readable text, so a library decodes them. The three layers are the same as in JCAMP-DX; mzML fixes the field names and hides the numbers, whereas JCAMP-DX leaves the names loose and shows the numbers. We return to mass spectra as data in session 12.

## 6. Today

You have one molecule, assigned on the board with its CAS registry number. In section 2 you set that number in the notebook, download the record from the WebBook by the address the notebook prints, keep the file's name, and put it in `data/`. Download it once; the WebBook limits repeated requests. If it refuses you, say so, and we will post the same files on Canvas. The same `read_jcamp` reads it, the checks apply, and you find the strongest band, choosing the largest or the smallest value by the file's `YUNITS`, after asking the assistant how it would. Section 3 has you ask the assistant to load your block with `np.loadtxt`, then reads it one point per line beside the expanded reading and asks which one the header supports.

The judgment cell is scored today, 0 to 2, by the rubric in the syllabus, in the format on the AI practices page. Part (a) asks for the wavenumber and value of your strongest band, the header field you needed for each, and what you would have reported without it. Part (b) is one entry: a suggestion from the assistant that you changed, rejected or verified, with a reason from your file. Submissions are individual from today. To submit, click **Restart**, then **Run All**, save, and upload `activity.ipynb` to Canvas by 1:30 pm on Thursday, October 15, with your downloaded file still in `data/` under its WebBook name, because the graders run your notebook against the same files. Whatever the plot looks like, the file's own numbers are the test.
