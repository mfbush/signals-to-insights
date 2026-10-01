# Working with an AI assistant in this course

You use Claude Code in every session from the first one, and it can write most of the code any activity asks for. What it cannot do is decide whether a calibration point belongs in the fit, whether a peak is real, or whether a 4% change in a slope matters for your sample. Those decisions are the course. This page sets out the seven practices that keep them yours, the format of the judgment entry you write in every activity, two limits that come with the tool, and the ladder of eight practices that sessions 4 to 19 add one at a time.

## The seven practices

1. **You own every cell.** In the oral check-in for the final project you explain cells from your own notebook. If you cannot explain a cell, it should not be in your notebook.
2. **Ask for an explanation before asking for code.** Type "Explain what this cell does" before "fix this". The explanation tells you whether the fix you were about to ask for is the right one.
3. **Verify against your data.** Check units, magnitudes, and the plot. The assistant has never seen your instrument, so an absorbance of 14 or a retention time of minus 2 minutes looks as reasonable to it as any other number.
4. **Write one judgment entry per activity.** The entries are the evidence that you, not the assistant, did the science. The format is below.
5. **When stuck, paste the error message, not a description of it.** The full traceback names the line and the cause. "It doesn't work" names neither.
6. **Do not paste other people's unpublished data into any AI tool.** That includes data from your research group, which belongs to the group and not to you.
7. **Usage limits exist.** Do the reading and the thinking first, then use the assistant for the mechanical work.

## The judgment cell

Every activity notebook from session 4 on has one designated markdown cell, the judgment cell, the last markdown cell before the software environment cell, in two parts. Part (a) answers the interpretation question for that session using numbers from your own output. Part (b) is one judgment entry. The cell is scored 0 to 2 as a whole, a 2 needs both parts to cite your own data, and the rubric is the same in every session. You write the judgment cell yourself, and the same rule covers the final project's judgment log and its paragraph on how you used AI. Asking the assistant about the chemistry or statistics before you write is allowed, and is often how a judgment entry starts. Having it or any other AI tool generate, rewrite, translate or polish the text of the cell is academic misconduct in this course; the spell check in your editor is fine. The assistant in this repository is asked to leave the cell empty. A suspected case starts with a conversation with Matt about your notebook, and one that conversation does not resolve is reported to Community Standards and Student Conduct, as the [syllabus](README.md) sets out.

A judgment entry records one suggestion from the assistant that you changed, rejected, or verified, and the reason. The reason has to come from your data: a residual, a unit, a detection limit, a peak shape, a number you checked by hand. A reason that would fit any student's notebook does not count.

```markdown
**Judgment entry**

- **What the assistant suggested:** one or two sentences, summarized, not pasted.
- **What I did:** changed it, rejected it, or verified it.
- **Why, from my data:** one to three sentences that cite something specific in this notebook.
```

A worked example, from a six point UV-Vis calibration series at 0, 5, 10, 15, 20 and 25 µM:

```markdown
**Judgment entry**

- **What the assistant suggested:** fit all six standards with `linregress` and use the
  line to find the unknown's concentration. The fit gave a slope of 0.0571 AU/µM and
  R² = 0.997.
- **What I did:** changed it. I refit using the five standards from 0 to 20 µM.
- **Why, from my data:** the residuals are not random. They rise from -0.016 to +0.032 AU
  across the first five standards and then drop to -0.041 AU at 25 µM, whose absorbance of
  1.405 AU is the only one above 1.2 AU. Refit without it, the other five fall on a line
  (R² = 0.99998) that the 25 µM point misses by 0.087 AU, which is the flattening of the
  response at high absorbance rather than scatter. The slope rises 4.3%, to 0.0596 AU/µM.
```

The R² of 0.997 is what made the first fit look fine. Note that "verified" is a full entry too, as long as it names what you checked, for example "I recomputed the slope by hand from the 0 and 20 µM standards and got 0.0595 AU/µM". "I checked the output and it looked right" is not an entry.

The final project's judgment log uses the same format for entries about your project's data. By the working draft in November you will have written a dozen in the activities.

## Privacy and usage limits

Claude Code sends the files it reads and everything you type to Anthropic, and your account's privacy settings include a Model Improvement switch that decides whether those sessions may be used to train future models, so set it the way you want before you start. On the Pro plan, chat on claude.ai and Claude Code draw on the same usage limit, which is why an hour of asking the assistant to guess at an error can leave you short in class.

## The CLAUDE.md file

The repository includes a file named `CLAUDE.md` that Claude Code reads whenever you open it in the course folder. It states the course conventions and asks the assistant to explain before it writes, to ask before replacing code you wrote, to leave the judgment cell empty, and to tell you when a result should be checked against the chemistry. It guides the assistant and does not enforce anything. You can read it, and you can add to it: put your own conventions in `CLAUDE.local.md`, as the practice ladder below explains, so that `git pull` keeps working. Knowing what that file does and does not control is part of using the tool well.

## The practice ladder

From session 4, each session names one way of working with the assistant, in a line after the objectives in its notes, and the activity uses it at one marked point. Eight practices are introduced one at a time, and later sessions reuse them by name. The prompt for part (b) of the judgment cell names that session's practice. An entry that came from using it is the expected one, though any entry grounded in your data scores the same. Nothing about points changes.

| Session | Practice |
|---|---|
| 4 | Ask questions as you would a senior colleague |
| 5 | Specific prompts |
| 6 | Give it a check it can run |
| 7 | Explore and plan before code |
| 8 | Correct early, and clear the context |
| 9 | Give it a check it can run, reused |
| 10 | Keep a CLAUDE.md |
| 11 | Explore and plan before code, reused |
| 12 | A skill for a repeated step |
| 13 | Specific prompts, reused |
| 14 | Correct early, and clear the context, reused |
| 15 | A fresh-context review |
| 16 | A skill, on your project |
| 17 | Keep a CLAUDE.md, reused |
| 18 | Give it a check it can run, reused |
| 19 | A fresh-context review, on your project |

The examples below are for the Claude Code extension in VS Code. The practices are what matters, and they hold if a button moves in a later release.

**Ask questions as you would a senior colleague.** This extends practice 2. A colleague who has read infrared files for years answers "how would you find the strongest band?" in a sentence, and the useful follow-up is "what in my file told you that?" Ask the assistant the same way, before you ask it to change anything, and read the answer against the file. To point it at a file, type `@` and the file's name, for example `@data/acetone_ir.jdx`.

**Specific prompts.** This extends practice 5. A prompt that names the file, the column, the constraint and what done looks like gets code you can check, whereas "make these numeric" gets code that merely runs. Compare `My PFAS columns hold strings like "< 0.004". How do I make them numeric?` with a prompt that names the table, says that a below-limit result becomes `NaN`, and asks for a count that shows it did. To point at a few lines of a file, select them in the editor and press Alt and K (Option and K on a Mac), which puts a reference to those lines in your prompt.

**Give it a check it can run.** This extends practice 3. "The loop read every file" is a claim. A printed count of files read and files logged, next to the number of rows in the sequence table, is evidence. Ask the assistant to run the check, then read the output, not its summary of the output. In a notebook the assistant runs code by adding a cell at the end of the notebook and asking you to click **Execute** or **Cancel**. Read what it printed, then delete that cell, so that your notebook still ends with the software environment cell when you run all.

**Explore and plan before code.** For a figure or an analysis with several choices in it, get the plan in words first. Click the mode indicator at the bottom of the prompt box and choose **Plan**, or type `/plan` followed by the task. The plan opens as a document you can comment on. Approve it when the panels, axes and choices are the ones your data need, and only then let the assistant write code. The course's `CLAUDE.md` asks it to give a plan in words, without code, until you say to proceed.

**Correct early, and clear the context.** When the first answer goes the wrong way, say so at once, with the reason from the notes, for example "use t for six degrees of freedom, as the notes do, not 3". After two corrections that do not take, start again with a better first prompt in the notes' vocabulary: type `/` and choose **Clear conversation**. A long conversation full of wrong turns gives worse answers than a short one, and it uses more of your usage limit. To undo the assistant's edits too, hover over an earlier message and use its rewind button.

**Keep a CLAUDE.md.** This extends the section above. Put your own conventions in a file named `CLAUDE.local.md` in the top folder of the repository, beside `CLAUDE.md`, rather than editing the course's file. Claude Code reads it after `CLAUDE.md` at the start of every conversation, and the repository ignores it, so `git pull` keeps working and the file stays yours. In session 10 you add one convention, start a new conversation, and check whether the assistant's code changes. Type `/memory` to see which files it reads. A fresh clone of the repository does not have the file, so keep a copy of anything you want to keep.

**A skill for a repeated step.** A skill is a file of instructions for one task you do more than once, such as finding and integrating the peaks in a chromatogram, which the assistant reads only when that task comes up. It lives at `.claude/skills/<name>/SKILL.md` in the repository, a path the repository also ignores, and it opens with a short header that names the skill and says when to use it. Type `/` and the name to run it, for example `/peak-report`. If you create the `.claude/skills` folder during a conversation, start a new conversation before you run the skill. Session 12 has you write one and check it against a table you built by hand, and session 16 uses it on your project.

**A fresh-context review.** A conversation that did not watch you build the notebook reads it the way a colleague reads a draft. Open one with **Claude Code: Open in New Tab** from the Command Palette, give it the notebook, the notes and a list of what to check, and ask it not to edit anything. It reports problems, and you decide which are real by checking each against your notebook. A review reads the whole notebook, so it costs about five questions' worth of your usage limit. It leaves the judgment cell to you and says only whether each part cites a number from your output.
