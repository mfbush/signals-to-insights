# Session 2: Python with chemical data

*Matt Bush, Department of Chemistry, University of Washington. CHEM 427/527, Autumn 2026.*

## Learning objectives

By the end of this session you can:

1. Index a list of measurements, and select values from it with a loop and with a list comprehension.
2. Write a function whose NumPy-style docstring states the unit of every argument and of the result.
3. Compute the residuals of a calibration fit with NumPy and SciPy, and use a residual plot to decide which standards belong in the fit.
4. Use Claude Code to explain an error message, and name the line the error points to before you change any code.

## 1. What session 1's line left out

Session 1 ended with a straight line through six standards, 0 to 25 µM at 520 nm, with a slope of 0.0571 AU/µM and $R^2 = 0.9975$. To see whether a line describes the data, look at the residuals. The residual of a standard is its measured absorbance minus the absorbance the line predicts at its concentration,

$$r_i = A_i - (m c_i + A_{\mathrm{bl}}),$$

i.e., the measured absorbance of standard $i$ minus the slope times its concentration plus the blank. If the model is right, the residuals scatter around zero by about the read noise, 0.0015 AU here.

The residuals of the six-point line do not scatter. They rise from -0.016 AU at 0 µM to +0.032 AU at 20 µM and drop to -0.041 AU at 25 µM, which is a curve, and a curve in the residuals means the model is wrong rather than the data noisy. Fit only the five standards at or below 1.2 AU, the top of the linear range, and those five residuals are no more than 0.0031 AU from zero, whereas the 25 µM standard sits 0.0865 AU below the line.

Today you make that plot yourself. You first index lists of measurements, then select from them with loops and comprehensions, then write functions with docstrings, and finally fit with NumPy arrays.

## 2. Values, types and lists

Every value in Python has a type, and the type decides what you can do with it. A concentration such as `10.0` is a `float`, a count of standards is an `int`, a unit such as `"AU"` is a `str`, and six absorbances in square brackets are a `list`.

Python counts positions in a list from 0, so the third standard is at index 2 and the last of six is at index 5. Although a chemist numbers the standards 1 to 6, asking for index 6 stops the notebook with `IndexError: list index out of range`. A negative index counts from the end, so `absorbances[-1]` is the last standard however many there are.

An f-string, i.e., a string with `f` before the opening quote, fills each `{}` field with a value: `{a:.3f}` prints `a` to three decimal places.

## 3. Loops and list comprehensions

A loop repeats one step for each item of a list, and `zip` walks two lists side by side, so `for c, a in zip(concentrations, absorbances)` gives one standard per pass.

A list comprehension, i.e., a loop inside square brackets that builds a new list, selects in one line:

```python
in_range = [a for a in absorbances if a <= LINEAR_LIMIT]
```

The same shape filters a mass spectrum. The activity's peak list is a simulated electrospray spectrum of a caffeine standard, 28 peaks. Keep the peaks at or above 5% of the base peak, the most intense peak, and five remain, all caffeine ions: protonated caffeine at m/z 195.088, its carbon-13 isotope peak 1.003 higher, the sodium adduct, a fragment and the dimer. Lower the threshold to 1% and twelve remain.

Which list is right depends on the question, not on the code, so `THRESHOLD` is a named constant in the Parameters cell with its reason in a comment.

## 4. Functions and docstrings

A function packages a calculation so it is written and checked once. The first function is the Arrhenius equation,

$$k = A \, e^{-E_a / RT},$$

which says that the rate constant $k$ equals the prefactor $A$ times the exponential of minus the activation energy $E_a$ divided by the gas constant $R$ times the temperature $T$. The docstring, i.e., the text in triple quotes under the `def` line, lists each argument with its unit, in the NumPy style every course notebook uses.

The units are the reason to write it. With $E_a$ in J/mol, the function reproduces the rate table to within 3% at 283, 313 and 343 K. Pass 80 for 80 kJ/mol and it returns $1.9 \times 10^{11}$ per second at 313 K, about $2 \times 10^{13}$ times the measured $9.0 \times 10^{-3}$ per second, and Python prints no error. An error message is the easy case.

You then write your own function, `concentration_from_absorbance`, the inverse of the calibration from session 1, with a docstring in the same format.

## 5. Arrays and the residual plot

A NumPy array does arithmetic on every element at once. Where the list needed a comprehension, the array version of the linear-range selection is a boolean mask, i.e., one `True` or `False` per standard:

```python
in_linear_range = absorbance <= LINEAR_LIMIT
```

Indexing with the mask, `concentration[in_linear_range]`, keeps the five standards marked `True`. `scipy.stats.linregress` fits each line, and one line of arithmetic gives all six residuals.

The two fits read an unknown at 0.742 AU as 12.68 µM and 12.43 µM, 2.0% apart. Which one to report is the question of the notebook's last **Explain** cell, and the residual plot holds the answer.

## 6. Error messages and the assistant

An error message, i.e., a traceback, reads from the bottom. The last line gives the type of error and a message, and the arrow above it marks the line that failed. Read those two first.

When it makes no sense, paste the whole traceback into Claude Code and ask for an explanation first:

```text
Explain this error message. Say which line it points to and why it fails. Do not fix it.
```

Then make the fix yourself. Section 1 of the notebook has one error built in for practice. A fix you cannot explain is not yours yet.

## 7. Today

If your laptop is not working yet, you pair with a student whose laptop is and sit at the keyboard as much as you can. The pair submits one notebook with both names.

The notebook does not run to the end until its three **[TASK]** cells are done. The **Explain** cells are not graded, but write them in your own words: the last one asks what the judgment cell asks from session 3, i.e., which number you would report and what in your output is the reason.

To submit, click **Restart**, then **Run All**, save, and upload `activity.ipynb` to Canvas by 1:30 pm on Thursday, October 8. It scores 1 if it runs from top to bottom after a restart.

Every fit in the rest of the course is checked the way section 4 of the notebook checks this one, by its residuals.
