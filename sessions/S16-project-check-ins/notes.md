# Session 16: Project work session 1, with oral check-ins

Tuesday, November 24. Your mentor decides, in seven minutes, how well you can explain your own project notebook: where the data came from, why the method fits them, what the result says, and which of the assistant's suggestions you checked. That conversation is the oral check-in, worth 10% of the course. Everyone is checked in today, two at a time, and the rest of the session is project work with one task: a skill for a step your project repeats, run on your project data.

## Learning objectives

By the end of this session you can:

1. Explain your project's data, method, and result from your own notebook. Answer a follow-up question with a value from your output.
2. Write or adapt a skill that reproduces a step your project repeats. Check it on a case whose answer your notebook already holds, then run it on your project data.
3. Decide from your data whether the skill's rule fits them. Record the decision as an entry in your judgment log.

**AI practice.** *A SKILL.md for a repeated step*, from session 12, now on your project. The skill lives in your project repository, which commits it, and the final submission's Workflow criterion reads it with the notebook cell that shows its output. You decide whether its output matches a value you computed by hand, and whether its rule suits your data rather than session 12's chromatograms. That decision is a judgment log entry, which you write without the assistant.

## 1. The oral check-in

The check-in follows [section 3 of the project page](../../final-project.md#3-oral-check-in): four dimensions (Data, Method, Result, and Judgment), each scored 0 to 5 on the ladder there, and a bank of 17 questions from which your mentor chose three or four after reading your working draft. A 5 on a dimension needs an answer to a follow-up you could not have prepared, given from your own data. A correct answer that would hold for anyone's data scores a 3.

The order is the Canvas page "Session 16 check-in order", in the Session 16 module, with your time and your station. It was drawn at random for each mentor. Lucas holds station A, for last names A to K, from 1:30 pm to 3:16 pm. Chris holds station B, for last names L to Z, from 1:38 pm to 3:24 pm, 8 minutes behind station A so that Matt can sit in on the first check-in at each. Each station breaks for 10 minutes after its sixth slot. Lucas and Chris show you where the stations are at 1:30 pm.

Each slot is 8 minutes: 7 to talk and 1 for your mentor to write a note. Come to your station a minute before your time with your laptop open to:

1. your project notebook, run from a clean start (**Restart**, then **Run All**) so that every output is there to point at;
2. `judgment-log.md`, since the Judgment question is taken from one of its entries;
3. the commit you submitted for the working draft, on GitHub, because your mentor read that one. If a cell has changed since, say so when a question reaches it.

There are no slides, and nothing to prepare except your own reasoning. To prepare that, read your notebook from the top and say aloud, for each output, the number it gives and why your analysis needs it. Any cell you cannot explain is the one to work on before Tuesday.

If you cannot attend, tell your mentor before 1:30 pm on Tuesday, November 24, and you are checked in during session 19, on Tuesday, December 8, with no cap. A total of 9 or below earns a second check-in in session 19 with Matt, and the higher of the two totals counts, up to 14.

## 2. A skill for your project's repeated step

A **skill** is a file of instructions, `SKILL.md`, in a folder under `.claude/skills/`, that Claude Code runs as a command when you type `/` and its name ([Claude Code skills](https://code.claude.com/docs/en/skills)). [Section 5 of the session 12 notes](../S12-peak-detection/notes.md#5-a-skillmd-for-a-repeated-step) introduced it with `/peak-report`, which found and integrated the peaks of one chromatogram by rules you set.

A repeated step is a computation your notebook makes more than once by the same rule, on several runs, samples, files, or settings: the peak areas of each replicate, a fit to each spectrum, a calibration for each batch. Choose the step your notebook does by hand most often, or will do once the final adds its second method. The skill makes that rule a written thing, so that the assistant applies the same one each time and a reader of your repository can see what it was.

Your session 12 skill sits in the course folder, which ignores it, and Claude Code reads skills only from the repository you have open and from your home folder. The project's skill goes in the project repository at `.claude/skills/<name>/SKILL.md`, and you commit it. If you create the `.claude/skills` folder during a conversation, start a new conversation before you run the skill.

The [example project repository](https://github.com/mfbush/signals-to-insights-project-example) has one, `phase-fraction`, which writes the cell that fits a two-phase model to every scan of one temperature run. It shows four habits worth copying:

1. The header's `description` says when to use the skill, in the words you would use to ask for it.
2. The body names the notebook's own functions and constants, and tells the assistant to add no new number and to stop if one seems missing.
3. Every choice is a number or a name: the tolerance on a setpoint, the columns of the table, the decimals printed.
4. The skill gives one cell and says, before the code, what the table should show and what to check in it.

The check is the one from session 12. Run the skill first on a case whose answer your notebook already holds, computed by hand. If the two differ by more than the last digit of a rounding, find the step in `SKILL.md` that caused it and change it before the skill reads new data. A match counts only if the skill's own text produced it, so read what the assistant says it used and write anything it took from elsewhere into the file.

## 3. Today

Nothing is collected today. The final submission's Workflow criterion scores the skill on December 9, and the entry counts toward the two judgment log entries the final needs from after November 22. Lucas, Chris, and Matt spend most of the session at the stations, so ask a neighbor first and keep a question for your mentor in your task file. While you wait for your slot, and after it:

1. Choose your project's repeated step, and open a task for the skill in `tasks/` with a dated entry, as for any piece of work.
2. Write `.claude/skills/<name>/SKILL.md` in your project repository, or copy your session 12 skill there and adapt it to your data.
3. In a new conversation, type `/<name>` with its argument, on the case your notebook already computed by hand. Compare the two, and change `SKILL.md` until they agree for a reason you can name.
4. Run the skill on your project data. Paste the cell it gives into a cell you add to the notebook and keep, run it, and read its output.
5. Write one judgment log entry, yourself, on whether the skill's rule fits your data: what it assumes, the value in your output that tests the assumption, and what you kept or changed.
6. Commit the skill, the notebook, the log, and the task, and push.

A skill that reproduces a number you already trust is a skill you can use on the next file.
