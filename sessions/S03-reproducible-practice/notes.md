# Session 3: Reproducible practice

*Matt Bush, Department of Chemistry, University of Washington. CHEM 427/527, Autumn 2026.*

## Learning objectives

By the end of this session you can:

1. Say which Python environment runs a notebook, and fix a `ModuleNotFoundError` by choosing the course kernel, not by installing a package.
2. Update your copy of the course with `git pull`, and keep your work when git refuses to pull.
3. Make a notebook run from top to bottom after a restart, with a relative path, all imports at the top, cells in the order they run, and a version cell.
4. Write a judgment entry whose reason cites a number from your own output.

## 1. A notebook that ran once

Today's notebook was left by a labmate who graduated. It fits a calibration for iron by the phenanthroline method, and its saved output reports 54.5 µM iron in an unknown. Click **Restart** and **Run All** and it stops on its first data cell, because the file it reads is on the labmate's laptop. Make it run to the end and it still reports 54.5 µM. Fix the one mistake that produces no error, and the unknown is 46.3 µM, 15% lower.

That notebook ran once, for one person, in one sitting. A reproducible notebook runs from top to bottom after a restart, on someone else's laptop, and gives the same number, which is how every notebook is graded from session 4.

You first check which Python runs the notebook, then learn how each session reaches your laptop, then the habits that let a notebook survive a restart, and finally write your first judgment cell.

## 2. Which Python runs the notebook

A notebook runs in a kernel, i.e., one Python program with its own set of installed packages. The course kernel is the environment `uv sync` built in the hidden `.venv` folder of the course repository during setup.

The course environment is defined by two files. `pyproject.toml` lists the packages the course uses, and `uv.lock` pins the exact version of each, for example NumPy 2.5.3 and SciPy 1.18.1, so every laptop computes with the same code. If you use conda, `environment.yml` plays the same role and the kernel is named `signals`.

VS Code shows the kernel in the top right corner of every notebook. Although a `ModuleNotFoundError` reads like a missing package, in this course it almost always means the wrong kernel, since the course environment already has every package. Click the kernel name, choose the `.venv` entry, and run the cell again. Do not `pip install` it into whichever Python is selected, because that laptop then runs different versions from everyone else's.

## 3. Getting each session with `git pull`

The course repository is a folder whose history git tracks, one commit at a time. Each session arrives as a new commit, and one command, run in a terminal in your `signals-to-insights` folder, brings it in:

```bash
git pull
```

Run `git status` first to see what you have changed. Running and saving a notebook changes the file, so earlier activity notebooks are listed as modified, and `git pull` leaves those changes alone as long as the new commits do not touch the same files. We do not change a session's activity notebook after that session, so the new commits almost never do.

If a pull ever refuses with `Your local changes to the following files would be overwritten by merge`, git names the file. To keep your work and still update:

1. In VS Code, copy the named file and paste it into the same folder, which saves your version as `activity copy.ipynb`.
2. Put the course version back, with the path git printed:

   ```bash
   git restore sessions/S02-python-with-chemical-data/activity.ipynb
   ```

3. Run `git pull` again.

Other fixes a web search offers for this message, such as `git reset --hard`, can delete your work.

## 4. Notebook hygiene

To see whether a notebook is reproducible, restart the kernel and run all cells. A restart clears every variable, so the run uses only what the notebook defines, in the order the cells appear. The number in square brackets beside each code cell records when it last ran.

The labmate's notebook has five problems, one for each habit below.

- **Relative paths.** A path such as `data/fe_phen_calibration.csv` is read from the notebook's folder, so it works on any laptop with a copy of the repository. A path that starts at `/Users/` or `C:\Users\` works on one laptop.
- **Imports at the top.** Every import goes in the first code cell. An import in a cell that was later deleted still works until the next restart.
- **Cells in the order they run.** A cell that uses a variable defined further down stops with a `NameError` after a restart.
- **A version cell.** The last cell prints the Python and package versions. It prevents no error today, but next year it tells you whether a different number came from the data or from newer software.
- **Check the chemistry, not only the run.** The labmate fit a straight line to percent transmittance, and the notebook runs without an error. Beer-Lambert behavior is linear in absorbance, which is computed from percent transmittance as

  $$A = -\log_{10}(T/100),$$

  i.e., the absorbance is minus the base-10 logarithm of the percent transmittance divided by 100. A line through %T has $R^2 = 0.933$ and residuals of +11, -10 and +9 %T at 0, 40 and 80 µM, the curve session 2 taught you to read as the wrong model.

Restart and run all catches the first three. Only a person checking the result against the chemistry catches the fifth.

## 5. The judgment cell, first practice

From session 4, every notebook ends with a judgment cell scored 0 to 2, and today's is unscored practice. Part (a) answers the session's question with numbers from your output: here, what concentration you report for the unknown and why. Part (b) is one judgment entry: a suggestion from Claude Code that you changed, rejected or verified, and the reason from your data. The AI practices page, `ai-practices.md`, has the format and a worked example.

Step 5 of section 2 asks Claude Code to review the labmate's calibration. Check what it says before you act on it: the slope against the 0.0111 AU/µM that the complex's molar absorptivity predicts, the residuals, one standard converted by hand. Write the judgment cell yourself, as the syllabus requires.

## 6. Today

Pairs work as in session 2 and submit one notebook with both names. Before you leave, fill in the setup status survey on Canvas again. If your laptop does not yet run the session 2 notebook, you leave with a named appointment with Lucas, Chris or Matt before session 4, because from Tuesday, October 13, the assistant is part of every activity.

To submit, click **Restart**, then **Run All**, save, and upload `activity.ipynb` to Canvas by 1:30 pm on Tuesday, October 13. It scores 1 if it runs from top to bottom after a restart, so a notebook that runs and reports 54.5 µM scores 1 too. That is the reason the judgment cell exists.
