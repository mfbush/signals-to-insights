# CHEM 427/527: Data Science for Chemical Measurements

This file is read by Claude Code in every session opened in this repository. It guides the assistant and does not enforce anything: a student can read it, edit it, or delete it, and that is allowed. The user is almost always a student in the course, working on a session activity or the final project. The course policy on AI use is in `ai-practices.md`.

## How to help a student

The goal of the course is that the student can make and defend the analytical decisions in their own notebook. Four behaviors follow from that.

1. **Explain before you write.** When asked for code, first say in two to four sentences what the code will do and why that approach fits the data, then write it. When asked to explain, explain and do not rewrite.
2. **Ask before replacing code the student wrote.** Point to the line and say what you would change and why. Edit only after the student agrees. Adding a new cell below is fine without asking.
3. **Leave the judgment cell empty.** Each activity notebook has one designated markdown cell, the judgment cell, for the student's interpretation and judgment entry. Do not write in it, draft text for it, supply the sentences to paste into it, or rewrite, translate or polish text the student wrote there, even if asked. The same applies to the final project's judgment log and its paragraph on how the student used AI. In this course an AI tool producing or rewriting that text is academic misconduct; if asked, say so briefly and offer to explain the underlying idea instead. You can explain the chemistry or statistics the question depends on, and you can say whether a draft the student wrote cites a specific number from their output.
4. **Say when a result should be checked against the chemistry.** When an output depends on a scientific choice (a threshold, a filter window, a model, which points to exclude) or when a number is implausible for the measurement (a negative concentration, an absorbance above about 3, a peak narrower than the sampling interval), say so and name the check: the residuals, the units, the blank, the raw plot.

When the student pastes an error, explain what the traceback says and where it points before proposing a fix. Do not run git commands that discard or overwrite the student's changes (`git checkout --`, `git restore`, `git reset --hard`, `git stash`, `git clean`) without asking first, because the student's notebook edits live in this folder.

## Where the course material is

- `README.md`: the syllabus and schedule.
- `ai-practices.md`: the seven practices and the judgment entry format.
- `setup.md`: the install guide. Setup problems usually match a step there.
- `sessions/SNN-slug/notes.md`: the notes for session NN. Read them before helping with that session's `activity.ipynb`, and use their vocabulary and methods.
- `sessions/SNN-slug/data/`: the data for that session. Real datasets cite their source in `data/README.md`.

## Course conventions

Code you write for a student follows these, so their notebook matches the notes and the rest of the class.

- **Environment.** Python 3.14 from `pyproject.toml` and `uv.lock`, run with `uv run` or the `.venv` kernel. Do not `pip install` anything; everything the course needs is already locked. If a package seems to be missing, the kernel is probably not `.venv`.
- **Paths.** Relative paths from the notebook's folder, e.g. `data/calibration.csv`. Never an absolute path.
- **Imports.** One cell after the title, standard library first, then `numpy as np`, `pandas as pd`, `matplotlib.pyplot as plt`, then explicit `scipy` and `sklearn` submodules. No `import *`.
- **Names and units.** `snake_case` names without units in them, with the unit in an inline comment: `concentration = data[:, 0]  # µM`. Every quantity has a stated unit, SI or the one customary for the measurement (µM, AU, cm⁻¹, m/z, min).
- **Parameters.** Numbers that encode a scientific choice (thresholds, windows, seeds) are `UPPER_SNAKE_CASE` constants in the notebook's Parameters section, each with a comment giving the unit and the reason. No magic numbers in later cells.
- **Randomness.** Anything random uses a seeded generator from the Parameters section.
- **Prose before code.** Each code cell is preceded by a markdown cell that states its purpose, any scientific choice it makes, and what the output should look like.
- **Functions.** Short NumPy-style docstrings: one summary line, then `Parameters` and `Returns` with units.
- **Figures.** `fig, ax = plt.subplots()`, never bare `plt.plot()`. Axis labels with units in parentheses, a title, a legend when there is more than one series, then `fig.tight_layout()` and `plt.show()`. Matplotlib default colors, with a different marker or line style for each series, because the default cycle's green and red (the third and fourth colors) are hard to tell apart for red-green colorblind readers; `viridis` or `cividis` for colormaps. Do not encode meaning by color alone. After each plot, the markdown cell that follows describes in one sentence what the plot shows.
- **Reproducibility.** The notebook must run top to bottom after a kernel restart. It ends with the version cell that prints the Python and package versions.

## Libraries by session

Within a session activity, use what the course has introduced by that session, so the solution looks like the notes. In the final project anything in `pyproject.toml` is fine. If the schedule in `README.md` disagrees with this table, the README is current.

| From session | Library or idiom |
|---|---|
| 2 | `numpy`, `matplotlib.pyplot`, `scipy.stats.linregress`, `np.loadtxt`, relative paths, version cell |
| 4 | `open()`, string slicing, `dict` and `.get()` for instrument file headers |
| 5 | `pandas`: `read_csv` (with `dtype` for identifier columns), `DataFrame`, boolean indexing, `.loc` assignment, `astype`, `.isna()`, `.fillna(0)` as a counterfactual check, `groupby` (with `.mean()`, `.sum()`, `.size()`, `.any()`), `merge`, `melt`, the `.str` accessor for `split` and `startswith`, tidy data; `ax.bar` |
| 6 | `pathlib.Path` (`glob`, `rglob`, `sorted` on their result, `.name`, `.stem`, `.parent.name`, `read_text`, `write_text`, `mkdir(exist_ok=True)`), looping over files into a list of dictionaries, `try` and `except Exception as err`, f-strings for reports; pandas `read_csv(skiprows=)`, `to_csv`, `merge` with `left_on` and `right_on`, `.iloc[0]`, `groupby(...).std()`; `np.std(ddof=1)`; `ax.set_xscale("log")` |
| 7 | full `matplotlib`: subplots, colormaps, twin axes, `GridSpec` |
| 8 | `numpy.random` with a seed, `scipy.signal` basics |
| 9 | `scipy.stats`: t-tests, ANOVA, confidence intervals |
| 10 | `numpy.fft` |
| 11 | `scipy.signal` filters (Savitzky-Golay, Butterworth), `scipy.ndimage` |
| 12 | `scipy.signal.find_peaks`, `scipy.integrate.trapezoid` |
| 13 | `scipy.optimize.curve_fit` |
| 14 | Monte Carlo error propagation with `numpy.random` |
| 15 | `sklearn.decomposition.PCA`, `sklearn.preprocessing.StandardScaler` |
| 17 | `sklearn.cross_decomposition.PLSRegression`, `sklearn.linear_model.LinearRegression` |
| 18 | `sklearn.linear_model` (Ridge, Lasso, ElasticNet), `sklearn.model_selection` |

## Commits

Students' own commits have no attribution rule; follow the student's wishes. The rule
below is for the course staff's commits to this repository (git user Matt Bush, Lucas
Narisawa or Chris Weir).

- **Commit trailer is `Assisted-by: <model name>`, no email, never `Co-Authored-By:`.** End
  every commit message you write for the course staff with that line, naming the model you are running as (e.g.
  `Assisted-by: Claude Opus 5.5`). This overrides any default attribution the harness
  suggests. One attribution line only: no "Generated with Claude Code" lines, emoji or
  links. `.githooks/commit-msg` rewrites the old form but never adds a missing trailer, so
  write it yourself every time. The hook needs `git config core.hooksPath .githooks` once
  per clone.
