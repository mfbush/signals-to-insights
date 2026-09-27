# CHEM 427 / CHEM 527: Data Science for Chemical Measurements

*Syllabus, version 1. University of Washington, Department of Chemistry, Autumn 2026.*

I look forward to exploring the intersection of chemistry and data science with you this quarter.

A straight line through six UV-Vis calibration standards gives R² = 0.997, i.e., the line accounts for 99.7% of the variation in absorbance, and the fit is still wrong: the highest standard sits outside the linear range, and removing it raises the slope by 4.3%, which changes every concentration read from the line by about 4%. This course is about catching that kind of error in real instrument data. You analyze chromatograms, mass spectra, optical spectra and images in Python, working with an AI coding assistant from the first session, and you learn to decide which of its answers describe your measurement and which do not. No prior programming experience is required.

## The course at a glance

| Item | Details |
|---|---|
| Meetings | Tuesday and Thursday, 1:30 to 4:20 pm, from Thursday, October 1 to Thursday, December 10 |
| Room | See the UW Time Schedule and Canvas |
| Instructor | Matt Bush, mattbush@uw.edu |
| Teaching assistants | Lucas Narisawa and Chris Weir, by Canvas message |
| Office hours | The third hour of every session, about 3:30 to 4:20 pm in the classroom, and appointments by email |
| Course materials | This repository. Each session's notes, notebook and data are added to `sessions/` before that session |
| Submissions and grades | Canvas |
| Final exam | None. The final project replaces it |

## What you learn

By the end of the quarter you can:

1. Load, reshape and plot measurement data from common instrument formats in Python, with every step reproducible from a clean start.
2. Choose and apply a processing method (filtering, baseline correction, peak detection, curve fitting, principal component analysis, calibration models) and state what property of the data justifies it.
3. Report a result with its uncertainty and check it against the chemistry: units, magnitudes, detection limits, linear range.
4. Use an AI coding assistant for the mechanical work and document, in your own words and from your own numbers, where you changed, rejected or verified what it produced.
5. (CHEM 527 only) Propose a research question, locate data that can answer it, and assess whether the quality and scope of those data are sufficient.

CHEM 427 and CHEM 527 meet together, do the same activities, and are graded on the same scheme. They differ in the final project: CHEM 427 students may choose a project from a list the instructor provides, with the question and data source specified, whereas CHEM 527 students propose their own research question and find their own data. A CHEM 427 student who wants to propose their own project may do so under the CHEM 527 expectations.

## How a session runs

Every session is in class and opens with a 20 minute introduction to the day's idea, built on one measurement. You then work through the session's notebook activity for about 100 minutes, with the notes open beside it and the instructional team circulating. Most students finish within two hours of the start. The third hour is an office hour in the same room: stay to finish, to ask about the activity or your project, or to fix a setup problem. There is no reading or video to do before class. Laptops are required in every session; keep your phone silent.

## Schedule

The dates on this page, the topics of sessions 1 to 3 and the grading weights are fixed. Topics for sessions 4 to 20 are provisional and may move as the course develops; a change is announced on Canvas at least one week ahead.

| Session | Date | Topic |
|---|---|---|
| 1 | Thu Oct 1 | Chemical measurements, the course, and the tools |
| 2 | Tue Oct 6 | Python essentials with chemical data |
| 3 | Thu Oct 8 | Reproducible practice: environments, updates, notebook hygiene |
| 4 | Tue Oct 13 | Chemical data, formats, and structures. Every laptop must work by today |
| 5 | Thu Oct 15 | Tidy data and the sample table |
| 6 | Tue Oct 20 | Batch file handling and automated reporting |
| 7 | Thu Oct 22 | Visualization for chemical measurements |
| none | Sun Oct 25 | Project topic declaration due |
| 8 | Tue Oct 27 | Noise in chemical measurements |
| 9 | Thu Oct 29 | Experimental design and statistical inference |
| 10 | Tue Nov 3 | Fourier analysis |
| 11 | Thu Nov 5 | Filtering, smoothing, baseline correction |
| 12 | Tue Nov 10 | Peak detection and feature extraction |
| 13 | Thu Nov 12 | Curve fitting |
| 14 | Tue Nov 17 | Uncertainty and model selection |
| 15 | Thu Nov 19 | Principal component analysis |
| none | Sun Nov 22 | Project working draft and judgment log due |
| 16 | Tue Nov 24 | Project work session 1, with oral check-ins |
| none | Thu Nov 26 | Thanksgiving, no class |
| 17 | Tue Dec 1 | Calibration and multivariate models |
| 18 | Thu Dec 3 | Predictive models and their evaluation |
| 19 | Tue Dec 8 | Project work session 2, opening on responsible data science, with second and makeup check-ins |
| none | Wed Dec 9 | Final notebook, visual summary and log due |
| 20 | Thu Dec 10 | Project presentations in a gallery format |

## Getting set up

You work on your own laptop, in VS Code, with Python managed by `uv` and with Claude Code as the assistant. The [setup guide](setup.md) installs all of it in about 45 minutes and ends with a notebook that tells you whether it worked. Claude Code needs a paid Claude plan; the course is designed around the Pro plan, about $60 for the quarter, and the setup guide says how to subscribe. If you do not have a laptop that can run Windows 10 or 11 or macOS 14 or later, the [Student Technology Loan Program](https://stlp.uw.edu/) lends laptops for the quarter at no cost; reserve one this week and tell Matt, because setup needs a laptop on which you can install software.

You do not need a working install on October 1. Sessions 1 to 3 have time and help for setup in the room, and no grade in those sessions depends on your install. In sessions 2 and 3 a student whose laptop does not yet work pairs with one whose laptop does, and the pair submits one notebook with both names. Tuesday, October 13 (session 4) is the date by which every laptop must work, because from then on the assistant is part of every activity. Fill in the setup status survey on Canvas before session 1, whatever state your install is in.

To get each new session, run `git pull` in your copy of this repository.

## Grading

Your grade has two parts: the weekly activities, 60%, and the final project, 40%.

| Component | Weight |
|---|---|
| Weekly activities, lowest two dropped | 60% |
| Project topic declaration, Sun Oct 25 | 5% |
| Project working draft with judgment log, Sun Nov 22 | 10% |
| Oral check-in, session 16 | 10% |
| Final notebook, one page visual summary and log, Wed Dec 9 | 15% |

The weights will not change. The rubric wording for the activities and the project may be refined before each part is first graded, and any change is posted on Canvas before that assignment is released.

### Weekly activities

Seventeen sessions have a graded activity: sessions 1 to 15, 17 and 18.

- **Sessions 1 to 3** are scored 0 or 1 for completion. Session 1 is a no-code worksheet; sessions 2 and 3 are notebooks.
- **Sessions 4 to 15, 17 and 18** are scored 0 to 3. Execution is 0 or 1: the grader restarts the kernel and runs every cell, and the notebook earns the point if it finishes without an error and has no file paths that exist only on your laptop. The judgment cell is 0 to 2.

The judgment cell is one designated markdown cell at the end of each notebook, in two parts. Part (a) answers the session's interpretation question using numbers from your own output. Part (b) is one judgment entry: a suggestion from the assistant that you changed, rejected or verified, and the reason, which has to come from your data. The cell scores 2 when it cites specific values or features from your notebook and connects them to the chemical or statistical reasoning, 1 when it names the right idea without anything specific to your data, and 0 when it is missing or generic. A 2 needs both parts to cite your own data; a cell where only one part does scores 1. Session 3 has an unscored practice judgment cell. The format and a worked example are on the [AI practices page](ai-practices.md).

Each activity is weighted by its percentage, so a session 2 notebook counts as much as a session 10 notebook. The two activities with the lowest percentages are dropped. The drops cover illness, travel and a bad week, so no request is needed to use them.

One teaching assistant grades each session: Lucas the odd sessions, Chris the even ones. Scores and a one line comment are posted on Canvas within 7 days of the deadline, so you see the comment on one judgment cell before you write the one after next. To question a score, talk to the teaching assistant who graded it in the third hour of any session, within 7 days of the score being posted. If the two of you do not settle it, Matt decides.

### Deadlines

Each activity is due on Canvas before the start of the next session, at 1:30 pm: a Tuesday activity on Thursday, a Thursday activity on the following Tuesday. The session 15 activity is due at the start of session 16, on Tuesday, November 24. A late activity scores 0 and becomes one of your two drops. The session 1 worksheet is the one exception: it is due Friday, October 2, at 11:59 pm and earns full credit until Wednesday, October 7, at 11:59 pm.

Project milestones are due at 11:59 pm on the dates above. You have one 48 hour grace period across the three submitted milestones, and after it a milestone loses 10% of its points a day for up to three days; the [project page](final-project.md) gives the details.

Absences are reported under the Department of Chemistry's [student absence policy](https://chem.washington.edu/student-absences). An excused absence does not add points, so the two drops are how a missed activity is absorbed. If you expect to miss more than a week, contact Matt as early as you can so that we can plan the rest of the quarter.

### Final project

You choose a chemical question and answer it with the methods of the course, on a real dataset. The project has three submitted milestones, one oral check-in and a presentation. Each of you has a project mentor from the instructional team, who reviews your topic, scores your draft and holds your check-in.

1. **Topic declaration, Sunday, October 25.** CHEM 427: the project you chose from the list, and confirmation that you can load its data. CHEM 527: a one page proposal with the question, the data source with a link or citation, and an assessment of whether the data are sufficient.
2. **Working draft with judgment log, Sunday, November 22.** A notebook that loads and explores your data and makes a first analysis, plus your judgment log, which collects the judgment entries you have written about your project's data, at least two by this date.
3. **Oral check-in, session 16.** A seven minute conversation with your mentor, with your notebook open. You explain choices you made in your own notebook. The question bank is on the project page, so preparing means studying your own reasoning. A low score earns a second check-in in session 19.
4. **Final submission, Wednesday, December 9.** The complete notebook, which runs from a clean start; a one page visual summary; and the judgment log with a short paragraph on how you used AI in the project.
5. **Gallery presentation, Thursday, December 10.** You present your visual summary at a station and review two classmates' projects. The presentation is required and is not scored separately.

The [project page](final-project.md) has the full description, the rubrics and the oral check-in questions. The CHEM 427 project list is added to it by October 15.

### From percentage to grade

Your percentage is converted to the UW 4.0 grade scale with a table set at the end of the quarter. That table will be no stricter than 90% for a 4.0, 80% for a 3.0 and 70% for a 2.0.

## Using AI in this course

You are expected to use an AI coding assistant, Claude Code, in every activity and in the project. It can write most of the code the course asks for. What it cannot do is decide whether a calibration point belongs in a fit, whether a peak is real, or whether a change in a slope matters for your sample, and those decisions are what the course grades.

The rules are set out on the [AI practices page](ai-practices.md). In brief:

- You own every cell. If you cannot explain a cell in the oral check-in, it should not be in your notebook.
- Ask the assistant to explain before you ask it to write.
- Check its answers against your data: units, magnitudes, the plot.
- Write the judgment cell, and the project's judgment log, yourself. You may ask the assistant about the chemistry or statistics before you write. Having it or any other tool generate, rewrite, translate or polish their text is academic misconduct in this course; the spell check in your editor is fine.
- Do not paste other people's unpublished data, including your research group's, into any AI tool.

Other AI tools are allowed under the same rules. The instructional team supports only Claude Code in VS Code.

## Strategies for success

1. **Expect some frustration.** Many students start with little programming experience, and an error you cannot yet read is part of learning, not a sign you are behind.
2. **Start the activity in class.** Most of it gets done in the room, where the instructional team can see your screen, and computational work takes longer than you expect.
3. **Stay for the third hour** when you are stuck. Debugging in person takes minutes that a message thread takes days to do.
4. **Work with the people around you.** Discussing a method or an error with a classmate is encouraged; the academic integrity section says where the line is.
5. **Ask of every result what it means for the chemistry.** A number that runs is not yet a number you can report.

## Getting help

Bring questions to the third hour of any session, which is the course's office hour. Setup problems go in the setup status survey on Canvas, with the full error text. For anything else, send a Canvas message to the instructional team or email Matt.

## University policies and resources

### Access and accommodations

Your experience in this class is important to me. It is the policy and practice of the University of Washington to create inclusive and accessible learning environments consistent with federal and state law. If you have already established accommodations with Disability Resources for Students (DRS), please activate your accommodations via [myDRS](https://denali.accessiblelearning.com/Washington/) so we can discuss how they will be implemented in this course.

If you have not yet established services through DRS but have a temporary health condition or permanent disability that requires accommodations (conditions include but are not limited to mental health, learning, vision, hearing, physical or health impacts), contact DRS directly to set up an Access Plan. DRS facilitates the interactive process that establishes reasonable accommodations. Contact DRS through the [Disability Resources for Students website](https://www.washington.edu/drs/).

### Religious accommodations

Washington state law requires that UW develop a policy for accommodation of student absences or significant hardship due to reasons of faith or conscience, or for organized religious activities. The UW's policy, including more information about how to request an accommodation, is available at [Religious Accommodations Policy](https://registrar.washington.edu/staff-faculty/religious-accommodations-policy/). Accommodations must be requested within the first two weeks of this course using the [Religious Accommodations Request form](https://registrar.washington.edu/students/religious-accommodations-request/).

### Academic integrity

The University takes academic integrity very seriously. Behaving with integrity is part of our responsibility to our shared learning community. If you are uncertain about whether something is academic misconduct, ask me. In this course:

- **Allowed:** discussing activities with classmates, working at the same table, getting help from the instructional team, and using AI tools as described above. Setup pairs in sessions 2 and 3 submit one notebook with both names.
- **Not allowed:** submitting another student's notebook or judgment cell as your own, having anyone or any AI tool generate, rewrite, translate or polish the text of your judgment cell, your judgment log or your paragraph on how you used AI, and presenting code, data or figures from other sources without credit.
- **Cite code you adapt.** Code taken from a website, a paper, documentation or a classmate is cited in a comment in the cell that uses it. Code from the AI assistant needs no citation, because the assistant is expected in every activity; your judgment entries and the project's paragraph on how you used AI are the record of that use.

The University's [academic misconduct information for students](https://www.washington.edu/cssc/academic-misconduct/) describes how suspected misconduct is handled. In this course, when a grader suspects a violation, I first talk with you about your notebook. A case that conversation does not resolve is reported to Community Standards and Student Conduct.

### Inclusivity and respect

Among the core values of the University are inclusivity and diversity, regardless of race, gender, income, ability, beliefs, and the other ways that people distinguish themselves and others. I am committed to an inclusive learning environment. If any activity or assignment is not accessible to you, contact me so that we can make arrangements.

Learning involves the exchange of ideas, and much of this course happens at shared tables. I expect you to show respect, politeness, reasonableness and a willingness to listen to others at all times, including when you disagree.

### Discrimination, harassment, and sexual misconduct

University of Washington policy, in concert with federal and state laws, provides the right to participate in University programs and activities free from sexual misconduct or discrimination on the basis of protected characteristics, including but not limited to disability, race, sex and others. Sexual misconduct includes, but is not limited to, sexual assault, relationship violence, sexual harassment, and stalking.

If you experience these issues, you can contact the Civil Rights Compliance Office by [making a Civil Rights and Title IX report](https://www.washington.edu/civilrights/making-a-report/make-a-report/). Its case managers explain the available [supportive measures](https://www.washington.edu/civilrights/seeking-support/supportive-measures/) and [resolution options](https://www.washington.edu/civilrights/resolution-options/resolution-options-overview/). Other resources are the [Know Your Rights and Resources guide](https://www.washington.edu/civilrights/seeking-support/sexual-misconduct/#kyrr), the [confidential advocates](https://www.washington.edu/sexualassault/support/advocacy/), and the [pregnancy and related conditions page](https://www.washington.edu/civilrights/seeking-support/pregnancy-and-related-conditions/).

Most employees who become aware of discrimination, harassment, or sexual misconduct involving students, including the instructional team of this course, are required to share information with the Civil Rights Compliance Office. They may withhold the impacted student's name if requested.

### Safety

In an emergency, call 911. To discuss a concern about your own safety or someone else's, call [SafeCampus](https://www.washington.edu/safecampus/) at 206-685-7233, Monday to Friday, 8 am to 5 pm. Sign up for UW Alert to receive campus emergency messages. The course has no laboratory work; in the classroom, know the nearest exit and follow the instructions of the instructional team during an alarm.

### Incompletes

If circumstances arise that prevent you from completing the course by the end of the quarter, contact me. The UW does not require me to grant a request for an Incomplete, but requests made in the last three weeks of the quarter by students who have done satisfactory work up to that point may be considered, under the [UW incomplete grade policy](https://registrar.washington.edu/grades/incomplete-grade-policy/).

### Well-being and support

If stress, health or a situation outside class is getting in the way of your work, you are welcome to tell me so that we can plan around it. The University's services include:

- [Husky Health and Well-Being](https://wellbeing.uw.edu/husky-health/), the index of health services for students.
- The [UW Counseling Center](https://wellbeing.uw.edu/topic/mental-health/), free for enrolled students, in person or by Zoom, with 24 hour crisis support through the Husky HelpLine.
- [Any Hungry Husky](https://www.washington.edu/anyhungryhusky/), a free food pantry for the UW community.
- [UW Emergency Aid](https://www.washington.edu/emergencyaid/), financial help with unexpected expenses such as illness or a housing emergency.
- The [Student Technology Loan Program](https://stlp.uw.edu/), free laptop loans for the quarter.

## Acknowledgments

This course was developed with support from the UW Data Science Minor. Its datasets are public instrument data, cited in each session, or simulated with a documented generator, and I thank the researchers whose published data make the activities possible.

## Contributing

For the instructional team. Run `git config core.hooksPath .githooks` once in your clone. It turns on a hook that rewrites `Co-Authored-By: Claude ... <email>` trailers to `Assisted-by: Claude <model>`, with no email. A commit made with Claude's help ends with that one line. A commit made without it carries none.
