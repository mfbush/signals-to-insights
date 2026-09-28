# Working with an AI assistant in this course

You use Claude Code in every session from the first one, and it can write most of the code any activity asks for. What it cannot do is decide whether a calibration point belongs in the fit, whether a peak is real, or whether a 4% change in a slope matters for your sample. Those decisions are the course. This page sets out the seven practices that keep them yours, the format of the judgment entry you write in every activity, and two limits that come with the tool.

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

The repository includes a file named `CLAUDE.md` that Claude Code reads whenever you open it in the course folder. It states the course conventions and asks the assistant to explain before it writes, to ask before replacing code you wrote, to leave the judgment cell empty, and to tell you when a result should be checked against the chemistry. It guides the assistant and does not enforce anything. You can read it, and you can edit it. Knowing what that file does and does not control is part of using the tool well.
