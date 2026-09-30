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

That notebook ran once, for one person, in one sitting. A reproducible notebook runs from top to bottom after a restart, on someone else's laptop, and gives the same number. From session 4, every notebook is graded that way.

You first check which Python runs the notebook, then learn how each session reaches your laptop, then the habits that let a notebook survive a restart, and finally write your first judgment cell.

## 2. Which Python runs the notebook

A notebook does not run its own code. It sends each cell to a kernel, which is a Python program running in the background, and the kernel sends back the output you see under the cell. Every kernel belongs to one environment. An environment is a folder that holds one copy of Python and one set of installed packages, such as NumPy and SciPy, so two environments on the same laptop can hold different packages or different versions of the same package.

The course environment is defined by two files in the course repository. `pyproject.toml` is a short text file that lists the packages the course uses. `uv.lock` is a longer file that pins the exact version of each package, for example NumPy 2.5.3 and SciPy 1.18.1, so every laptop computes with the same code. During setup, `uv sync` read those two files and built the environment in a folder named `.venv` inside the repository. The dot at the start of the name hides the folder on most laptops. If you use conda, `environment.yml` plays the same role and the environment is named `signals`.

VS Code shows the kernel in the top right corner of every notebook, as the name of the environment. Although a `ModuleNotFoundError` reads like a missing package, in this course it almost always means the wrong kernel, because the course environment already has every package the activities use. Click the kernel name, choose the `.venv` entry, and run the cell again. Leave `pip install` alone here. It adds the package to whichever Python is selected, and that laptop then computes with different versions from everyone else's.

The code cell in section 1 of today's activity prints where the running Python lives. On a course laptop the path contains `.venv` or `signals`, and the last line reads `Course environment: yes`.

## 3. Getting each session with `git pull`

The course repository is a folder whose history git tracks. Git records that history as commits, and a commit is a saved snapshot of every file in the folder, with a date and a one-line message such as "Session 3: Reproducible practice". Your copy on your laptop is a clone, which is a full copy of the repository and its history. Each session arrives on GitHub as a new commit, and your clone gets it only when you ask.

To see what you have changed since your last update, open a terminal in your `signals-to-insights` folder and run

```bash
git status
```

It lists each file that differs from the last commit you have, under the heading `Changes not staged for commit`, with the word `modified:` before the path. Running and saving a notebook changes the file, because the saved outputs are part of it, so your session 1 and session 2 notebooks are listed.

To bring in the new session, run, in the same folder,

```bash
git pull
```

It downloads the new commits and adds their files to your clone. Your modified notebooks are left alone as long as the new commits do not touch the same files. We do not change a session's activity notebook after that session, so the new commits almost never do.

If a pull ever refuses with `Your local changes to the following files would be overwritten by merge`, git names the file. To keep your work and still update:

1. In VS Code, copy the named file and paste it into the same folder, which saves your version as `activity copy.ipynb`.
2. Put the course version back, with the path git printed:

   ```bash
   git restore sessions/S02-python-with-chemical-data/activity.ipynb
   ```

3. Run `git pull` again.

Your work is then in `activity copy.ipynb`, and the course version is up to date beside it. Use these three steps rather than the other fixes a web search offers for this message. Some of those, such as `git reset --hard`, delete your work.

## 4. Notebook hygiene

To see whether a notebook is reproducible, restart the kernel and run all cells. A restart stops the kernel and starts a new one, which clears every variable the notebook has defined. **Run All** then runs the cells from top to bottom, once each. The run uses only what the notebook defines, in the order the cells appear.

The number in square brackets to the left of each code cell is its execution count. It records when that cell last ran, counting from 1 at the last restart. After a clean **Restart** and **Run All** the counts read 1, 2, 3 and on down the page. Counts out of order, or a missing number, mean the cells ran in some other order, or a cell ran and was later deleted.

The labmate's notebook has five problems, one for each habit below.

- **Relative paths.** A path tells Python where a file is. A relative path starts from the notebook's own folder, so `data/fe_phen_calibration.csv` means the file `fe_phen_calibration.csv` in the `data` folder beside the notebook. It works on any laptop with a copy of the repository. An absolute path starts from the top of one disk, such as `/Users/labmate/Desktop/` on a Mac or `C:\Users\` on Windows, and works only on the laptop that has that folder. Elsewhere it stops the notebook with `FileNotFoundError`.
- **Imports at the top.** An import makes a library available to every later cell, and `import matplotlib.pyplot as plt` makes the name `plt` refer to matplotlib's plotting functions. Every import that a calculation or a plot needs goes in the first code cell. An import in a cell that was later deleted still works until the next restart, because the kernel remembers it. After the restart, the first use of `plt` stops with `NameError: name 'plt' is not defined`.
- **Cells in the order they run.** A cell can use only the variables that cells above it have defined. A plot cell that uses `slope` above the fit cell that defines it ran for the labmate, who ran the fit first. After a restart it stops with `NameError: name 'slope' is not defined`. Move the cell below the fit.
- **A version cell.** The last code cell prints the Python version and the version of each package the notebook uses. It changes no result today. Next year, when a rerun gives a different number, it tells you whether the change came from the data or from newer software. Session 2's notebook ends with one.
- **Check the chemistry, not only the run.** The labmate fit a straight line to percent transmittance, and the notebook runs without an error. Beer-Lambert behavior is linear in absorbance, which is computed from percent transmittance as

  $$A = -\log_{10}(T/100),$$

  i.e., the absorbance is minus the base-10 logarithm of the percent transmittance divided by 100. The 40 µM standard at 35.6 %T has an absorbance of 0.449 AU. A line through %T has $R^2 = 0.933$. Its residuals are +11, -10 and +9 %T at 0, 40 and 80 µM, which is the curve session 2 taught you to read as the wrong model.

Restart and run all catches the first three. Only a person checking the result against the chemistry catches the fifth.

## 5. The judgment cell, first practice

From session 4, every notebook ends with a judgment cell scored 0 to 2. Today's is practice and is not scored. Part (a) answers the session's question with numbers from your output. Here the question is what concentration you report for the unknown, and why. Part (b) is one judgment entry. It records a suggestion from Claude Code that you changed, rejected or verified, and the reason from your data. The AI practices page, `ai-practices.md`, has the format and a worked example.

Step 5 of section 2 asks Claude Code to review the labmate's calibration. Check what it says before you act on it. Three checks come from your own notebook. Compare the slope with the 0.0111 AU/µM that the molar absorptivity of the iron(II) phenanthroline complex predicts. Look at whether the residuals scatter around zero. Convert one standard by hand with the equation above, as for the 40 µM standard. Then write the judgment cell yourself, as the syllabus requires.

## 6. Today

Pairs work as in session 2 and submit one notebook with both names. Before you leave, fill in the setup status survey on Canvas again. If your laptop does not yet run the session 2 notebook and Claude Code, you leave with a named appointment with Lucas, Chris or Matt before session 4. From Tuesday, October 13, every laptop must work, because the assistant is part of every activity.

To submit, click **Restart**, then **Run All**, save, and upload `activity.ipynb` to Canvas by 1:30 pm on Tuesday, October 13. It is scored 3 or 0, and it earns the 3 points if it runs from top to bottom after a restart. A notebook that runs and still reports 54.5 µM earns them too. That is the reason the judgment cell exists.
