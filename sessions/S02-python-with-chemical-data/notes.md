# Session 2: Python with chemical data

*Matt Bush, Department of Chemistry, University of Washington. CHEM 427/527, Autumn 2026.*

The slides from the opening are in this folder as [Session 2 opening slides (PDF)](slides/S02-opening-slides.pdf) and in the Session 2 module on Canvas.

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

The residuals of the six-point line do not scatter. They rise from -0.016 AU at 0 µM to +0.032 AU at 20 µM and drop to -0.041 AU at 25 µM, which is a curve, and a curve in the residuals means the model is wrong rather than the data are noisy. Fit only the five standards at or below 1.2 AU, the top of the linear range, and those five residuals are no more than 0.0031 AU from zero, whereas the 25 µM standard sits 0.0865 AU below the line.

Today you make that plot yourself. You first index lists of measurements, then select from them with loops and comprehensions, then write functions with docstrings, and finally fit with NumPy arrays.

## 2. Values, types and lists

Every value in Python has a type, and the type decides what you can do with it. Four types cover today's notebook. A `float` is a number with a decimal point, such as the concentration `10.0`. An `int` is a whole number, such as the count of standards, `6`. A `str`, i.e., a string, is text between quotes, such as the unit `"AU"`. A `list` is an ordered collection of values between square brackets, separated by commas, such as the six absorbances `[0.002, 0.296, 0.599, 0.897, 1.192, 1.405]`. A variable is a name that refers to a value and is set with `=`, so `absorbances = [0.002, ...]` stores that list under the name `absorbances` for later cells to use.

Each item in a list has an index, i.e., its position in the list counted from 0. The first standard is `absorbances[0]`, the third is `absorbances[2]`, and the last of six is `absorbances[5]`. Although a chemist numbers the standards 1 to 6, asking for `absorbances[6]` stops the notebook with `IndexError: list index out of range`, because no item has that position. A negative index counts from the end, so `absorbances[-1]` is the last standard however many there are.

To print a value with a label and a chosen number of digits, use an f-string, i.e., a string with the letter `f` before the opening quote. Python replaces each pair of curly braces with the value of the expression inside it, and a format code after a colon sets the digits, so `f"{a:.3f} AU"` prints the value of `a` to three decimal places followed by AU.

## 3. Loops and list comprehensions

To repeat one step for every standard, write a loop. A `for` loop runs the indented lines under it, its body, once for each item of a list, and gives the current item a name on each pass. The simplest loop prints each absorbance:

```python
for a in absorbances:
    print(a)
```

On the first pass `a` is 0.002, on the second 0.296, and so on, so the cell prints six lines. Python uses the indentation, four spaces, to tell where the body ends.

An `if` statement runs its own indented lines only when its condition is `True`. Put one inside the loop and the loop selects:

```python
for a in absorbances:
    if a > LINEAR_LIMIT:
        print(a)
```

With `LINEAR_LIMIT` set to 1.20 AU, this prints one line, 1.405, the 25 µM standard.

To walk two lists side by side, `zip` pairs their items in order, the first concentration with the first absorbance, the second with the second, and so on. The loop then unpacks each pair into two names:

```python
for c, a in zip(concentrations, absorbances):
    print(c, a)
```

The activity runs each of these three loops, then a fourth that combines them: `zip` for the pairs, an `if` with an `else`, which holds the lines that run when the condition is `False`, and an f-string for each printed line.

A list comprehension, i.e., a loop written inside square brackets that builds a new list, does the same selection in one line and keeps the result instead of printing it. Read it as the loop above written on one line: the value to keep, then the `for`, then the `if`.

```python
in_range = [a for a in absorbances if a <= LINEAR_LIMIT]
```

The result, `in_range`, is a list of the five absorbances at or below 1.20 AU.

The same shape filters a mass spectrum. The activity's peak list is a simulated electrospray spectrum of a caffeine standard, 28 peaks stored as (<i>m</i>/<i>z</i>, intensity) pairs. Each pair is a tuple, i.e., values in parentheses that are fixed once made, and the comprehension unpacks it into two names the way the `zip` loop does. Keep the peaks at or above 5% of the base peak, the most intense peak in the spectrum, and five remain, all caffeine ions: protonated caffeine at <i>m</i>/<i>z</i> 195.088, its carbon-13 isotope peak 1.003 higher, the sodium adduct, a fragment and the protonated dimer. Lower the threshold to 1% and twelve remain.

Which list is right depends on the question, not on the code. That is why `THRESHOLD` is a named constant in the Parameters cell, i.e., the cell near the top of the notebook where every chosen number is set once, with its reason in a comment.

## 4. Functions and docstrings

A function is a named calculation that takes inputs, its arguments, and hands back an output, its return value. The `def` line names the function and its arguments, the indented body does the calculation, and the `return` line hands back the result, so the calculation is written and checked once and then used wherever it is needed. The first function is the Arrhenius equation,

$$k = A \, e^{-E_a / RT},$$

which says that the rate constant $k$ equals the prefactor $A$ times the exponential of minus the activation energy $E_a$ divided by the gas constant $R$ times the temperature $T$. The docstring, i.e., the text in triple quotes directly under the `def` line, says in words what the function computes and lists each argument and the return value with its unit. Every course notebook uses the NumPy style, in which the arguments appear under the heading `Parameters` and the output under `Returns`.

The units are the reason to write it. With $E_a$ in J/mol, the function reproduces the rate table to within 3% at 283, 313 and 343 K. Pass 80 for 80 kJ/mol and it returns $1.9 \times 10^{11}$ per second at 313 K, about $2 \times 10^{13}$ times the measured $9.0 \times 10^{-3}$ per second, and Python prints no error. An error message is the easy case.

You then write your own function, `concentration_from_absorbance`, the inverse of the calibration from session 1, with a docstring in the same format.

## 5. Arrays and the residual plot

A NumPy array is a sequence of numbers stored so that arithmetic applies to every element at once, which removes the loop. For the array `absorbance`, the expression `absorbance - 0.001` subtracts a blank from all six values in one step. A comparison applied to an array gives a boolean mask, i.e., an array of `True` or `False` with one value per element:

```python
in_linear_range = absorbance <= LINEAR_LIMIT
```

Indexing with the mask, `concentration[in_linear_range]`, keeps the five standards marked `True`. The function `scipy.stats.linregress` fits a straight line by least squares and returns its slope and intercept. Subtract each fitted line from the measured absorbances and one line of arithmetic gives all six residuals.

The two fits read an unknown at 0.742 AU as 12.68 µM and 12.43 µM, 2.0% apart. Which one to report is the question of the notebook's last **Explain** cell, and the residual plot holds the answer.

## 6. Error messages and the assistant

An error message, i.e., a traceback, is Python's report of where the notebook stopped and why. It lists the lines that were running with the failing line last, so read it from the bottom. The last line gives the type of error and a message, such as `IndexError: list index out of range`, and the arrow above it marks the line that failed. Read those two first.

When it makes no sense, paste the whole traceback into Claude Code and ask for an explanation first:

```text
Explain this error message. Say which line it points to and why it fails. Do not fix it.
```

Then make the fix yourself. Section 1 of the notebook has one error built in for practice. Change the code only after you can say in your own words why the line failed.

## 7. Today

If your laptop is not working yet, you pair with a student whose laptop is and sit at the keyboard as much as you can. The pair submits one notebook with both names.

The notebook does not run to the end until its three **[TASK]** cells are done. The **Explain** cells are not graded, but write them in your own words. The last one asks the question that the judgment cell asks from session 3 onward: which number would you report, and what in your output is the reason?

To submit, click **Restart**, then **Run All**, save, and upload `activity.ipynb` to Canvas by 1:30 pm on Thursday, October 8. It scores 3 if it runs from top to bottom after a restart, and 0 if it does not.

Every fit in the rest of the course is checked the way section 4 of the notebook checks this one, by its residuals.
