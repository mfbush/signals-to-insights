# Session 1: The course, the tools, and what chemical data is

*Matt Bush, Department of Chemistry, University of Washington. CHEM 427/527, Autumn 2026.*

## Learning objectives

By the end of this session you can:

1. Run `activity.ipynb` from top to bottom in VS Code on the course kernel, or name the step of `setup.md` where your install stopped and the error it printed.
2. Ask Claude Code to explain a notebook cell and check one sentence of its explanation against the cell's output.
3. Classify six unlabeled instrument data excerpts by dimensionality, the physical meaning of the x-axis, and the chemical quantity the signal encodes.
4. State the four rules from `ai-practices.md` that decide how your notebooks are graded.

## 1. Why this course exists

Six standards from 0 to 25 µM, measured at 520 nm, give a straight-line fit with R² = 0.997. That number looks like the end of the analysis, and a coding assistant asked to "fit the calibration" stops there too. The residuals tell a different story: they rise across the first five standards and drop at 25 µM, the only standard above 1.2 AU. Refit without it and the slope rises by 4.3%, which lowers every concentration you would read from that line by about 4%.

Writing the fit takes one line of Python. Seeing that it is wrong for this spectrophotometer takes a chemist who looked at the residuals. The course teaches both halves on the measurements you will meet in a lab: chromatograms, mass spectra, UV-Vis and IR spectra, and images. You write Python in every session, with Claude Code in VS Code from today, and you are graded on the second half, i.e., the decisions you make about your data and the reasons you give for them.

You open this calibration series in today's notebook.

## 2. How a session runs

Every session has the same three parts.

- **Opening, 20 minutes.** Matt introduces the measurement and the method for the day. There is no reading to do before class.
- **Activity, about 100 minutes.** You work through `activity.ipynb` in the session folder, with Lucas, Chris, and Matt circulating. Most students finish in this time.
- **Third hour, office hour.** The room stays booked. Stay to finish or to ask questions, or leave if you are done.

Before each class, open a terminal in your `signals-to-insights` folder and run `git pull`, which brings in the new session folder. From session 2 on you upload the finished notebook to Canvas. From session 4 on each notebook is scored 0 to 3: 1 point for execution, i.e., it runs from top to bottom after a kernel restart, and 0 to 2 for the judgment cell at the end, which is described in `ai-practices.md`. Sessions 1 to 3 are scored 0 or 1 for completion only, so nothing about your install can cost you points while you are still setting it up.

## 3. Working with the assistant

Claude Code can write most of the code any activity asks for. It cannot tell you whether the 25 µM standard belongs in the fit, because it has never seen your instrument. The course rules follow from that, and `ai-practices.md` sets out all seven. Four of them decide how your work is graded:

1. **You own every cell.** In the final project you explain cells from your own notebook out loud. A cell you cannot explain should not be in your notebook.
2. **Ask for an explanation before asking for code.** "Explain what this cell does" comes before "fix this".
3. **Verify against your data.** Check the units, the magnitudes, and the plot.
4. **Write one judgment entry per activity.** It records one suggestion from the assistant that you changed, rejected, or verified, with a reason that cites your own numbers. You practice it in session 3, and it is scored from session 4.

The course folder contains a file named `CLAUDE.md`, which Claude Code reads every time you open it there. It states the course conventions and asks the assistant to explain before it writes, to ask before it replaces code you wrote, and to leave the judgment cell empty. It guides the assistant and does not enforce anything. You can open it, read it, and edit it. Knowing what that file does and does not control is part of using the tool well.

## 4. Getting set up

A working laptop needs git, uv (which installs Python and the course packages), VS Code, a Claude Pro account, and a copy of the course repository. `setup.md` installs them in that order and ends with `setup-check.ipynb`, which prints `Setup check passed` when everything works. It takes about 45 minutes.

Some laptops take all three onboarding sessions to set up, and the schedule is built for that.

- **Session 1, today.** If your install is not finished, you work on it with your helper. Lucas and Chris each look after half the room by last name, and you keep the same helper through session 3.
- **Sessions 2 and 3.** If your laptop still does not work, you pair with a student whose laptop does, and you sit at the keyboard for as much of the activity as you can. The pair submits one notebook with both names and splits up once both laptops work.
- **Session 3 ends with a setup checkpoint.** If your install still fails, you leave with a named appointment in the next week's office hours.
- **Session 4, Tuesday, October 13, is the hard deadline.** From session 4 on the assistant is part of every activity and every notebook is scored on your own laptop.

Fill in the setup status survey on Canvas whenever your status changes. When something fails, copy the full error text, not a description of it, because the exact text is how a helper finds the fix.

## 5. Today

Everyone does the worksheet, `worksheet.md` in this folder. It is the session 1 submission, it needs no code, and it takes about 60 minutes. You classify six excerpts of instrument data files, with the instrument names removed, by three properties: the number of dimensions, what the x-axis measures physically, and which chemical quantity the signal carries. A chromatogram and a mass spectrum are both a column of numbers against another column of numbers, and the methods you apply to each later in the course differ because the axis and the quantity differ. Submit your answers on Canvas by 11:59 pm on Friday, October 2.

If your install works, you also run `activity.ipynb`. You plot the calibration series from section 1 and type the two prompts written into the notebook: the first asks Claude Code to explain the notebook cell by cell, and the second asks it to change the plot. Check what it says about each cell against what the cell printed. The notebook is not submitted today.

If your install does not work yet, the rest of your time goes to setup with your helper.

The habit the course grades starts with the worksheet: before you analyze a file, know what the instrument measured and what each number in the file means.
