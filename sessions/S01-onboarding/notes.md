# Session 1: Chemical measurements, the course, and the tools

*Matt Bush, Department of Chemistry, University of Washington. CHEM 427/527, Autumn 2026.*

## Learning objectives

By the end of this session you can:

1. Write the calibration equation for an absorbance measurement and use it to convert an absorbance to a concentration.
2. Classify six unlabeled instrument data excerpts by dimensionality, the physical meaning of each axis, and the chemical quantity the signal encodes.
3. Run `activity.ipynb` from top to bottom in VS Code, or name the step of `setup.md` where your install stopped and the error it printed.
4. Ask Claude Code to explain a notebook cell and check one sentence of its answer against the cell's output.

## 1. From a signal to a concentration

An instrument never reports the quantity you want. A spectrophotometer reports absorbance, a chromatograph reports a detector signal against time, and a mass spectrometer reports ion counts against mass-to-charge ratio, i.e., m/z. The link between signal and amount comes from measuring standards of known concentration, which is the calibration you have done in quantitative analysis.

For absorbance the link is the Beer-Lambert law,

$$A = \varepsilon b c,$$

which says that the absorbance $A$ equals the molar absorptivity $\varepsilon$ times the path length $b$ times the concentration $c$. A calibration applies the same idea to any instrument: the signal $S$ equals the sensitivity $m$ times the concentration, plus the signal of a blank, $S_{\mathrm{bl}}$,

$$S = m c + S_{\mathrm{bl}},$$

so the concentration of an unknown is its signal minus the blank signal, divided by the sensitivity, $c = (S - S_{\mathrm{bl}})/m$. For absorbance, $m = \varepsilon b$. The five lowest standards in today's file give $m = 0.0596$ AU/µM in a 1 cm cuvette, i.e., a molar absorptivity of about 59,600 per molar per centimeter.

Two more figures of merit from your analytical chemistry courses recur all term.

- **Detection limit** is the concentration whose signal exceeds the blank by three standard deviations of the blank, $c_{\mathrm{LOD}} = 3 s_{\mathrm{bl}}/m$, i.e., three times the blank's standard deviation divided by the sensitivity. The simulated spectrophotometer behind today's file has a blank standard deviation of 0.0015 AU, so its detection limit is 0.076 µM.
- **Linear range** is the span of concentration over which $m$ is constant. Above 1.2 AU this spectrophotometer reads low, as real ones do once stray light is a measurable fraction of the transmitted light.

A chromatogram carries amount in a peak area and identity in a retention time, whereas a mass spectrum carries identity in m/z. The worksheet asks you to find these quantities in six files.

## 2. What the course adds to your chemistry courses

Your chemistry courses taught you to fit a calibration line and report its figures of merit, usually in a spreadsheet. This course does that analysis in Python on full instrument files and adds the step a fit skips: deciding whether the model describes the data.

Today's six standards, 0 to 25 µM at 520 nm, give a straight-line fit with $R^2 = 0.997$, i.e., the line accounts for 99.7% of the variation in absorbance. The residuals tell a different story: they rise across the first five standards and drop at 25 µM, the only standard above 1.2 AU and so outside the linear range. Refit without it and the slope rises by 4.3%, which lowers every concentration you would read from the line by about 4%.

Writing the fit takes one line of Python. Seeing that it is wrong for this spectrophotometer takes a chemist who looked at the residuals. You are graded on that second half, i.e., the decisions you make about your data and the reasons you give for them.

## 3. How a session runs

Every session has the same three parts.

- **Opening, 20 minutes.** Matt introduces the measurement and the method for the day. Today's opening runs about 35 minutes.
- **Activity, about 100 minutes.** You work through `activity.ipynb` in the session folder while the instructional team, Matt and the teaching assistants Lucas Narisawa and Chris Weir, circulates.
- **Third hour, office hour.** Stay to finish or to ask questions.

Before each class, run `git pull` in your `signals-to-insights` folder. From session 4 on each notebook is scored 0 to 3: 1 point for running from top to bottom after a kernel restart, and 0 to 2 for the judgment cell at the end. Sessions 1 to 3 are scored 3 or 0 for completion, so your install cannot cost you points while you set it up.

## 4. Why the course uses an AI assistant from today

Matt has written software for chemical measurements since the early 2000s, and for three years after ChatGPT went public in November 2022 he saw little value in it next to his own expertise. By early 2026 he did most of his coding with an AI agent. In one case, a trainee and he spent about 18 months trying to bring a high-speed digitizer with on-board processing into the lab's measurements with traditional practices, without headway. With an AI-assisted workflow it was online in under a month.

He expects the most successful chemists of the next 20 years to have three core competencies: choosing important questions, collaborating with AIs to answer them, and checking their answers. This course practices all three on chemical measurements, and it grades the third.

The risk is to your learning. A study that followed 26,811 secondary students in China found that AI raised homework scores by 18% and cut completion time by 30%, but lowered monthly exam scores by 20% within six months and entrance exam scores by 18 to 24% after about two years ([Strömberg, Lei and Wu, CEPR Discussion Paper 21577, 2026](https://cepr.org/publications/dp21577)). About 80% of the students using AI showed signs of outsourcing their homework. Note that those students were younger than you and that the study was observational, not a randomized trial.

To make the assistant add to what you learn, ask why it wrote each line the way it did, ask for explanations aimed at what you already know, try a step yourself before you compare it with the assistant's version, and check every result against your data.

## 5. Working with the assistant

Claude Code can write most of the code an activity asks for. It cannot tell you whether the 25 µM standard belongs in the fit, because it has never seen your instrument. Four of the seven rules in `ai-practices.md` follow from that and decide how your work is graded:

1. **You own every cell.** In the final project you explain cells from your own notebook out loud.
2. **Ask for an explanation before asking for code.**
3. **Verify against your data.** Check the units, the magnitudes, and the plot.
4. **Write one judgment entry per activity.** It records one suggestion from the assistant that you changed, rejected, or verified, with a reason that cites your own numbers.

The course folder's `CLAUDE.md` asks Claude Code to explain before it writes and to leave the judgment cell empty. It guides the assistant and enforces nothing.

## 6. Getting set up

`setup.md` installs git, uv, VS Code, and the course repository, connects your Claude Pro account, and ends with `setup-check.ipynb`, which prints `Setup check passed`. It takes about 45 minutes, and some laptops take all three onboarding sessions.

- **Session 1, today.** If your install is not finished, you work on it with a teaching assistant. Lucas and Chris each look after half the room by last name, and you keep the same teaching assistant through session 3.
- **Sessions 2 and 3.** If your laptop still does not work, you pair with a student whose laptop does, and the pair submits one notebook with both names.
- **Session 3 ends with a setup checkpoint.** If your install still fails, you leave with a named appointment in the next week's office hours.
- **Session 4, Tuesday, October 13, is the hard deadline.** From then on every notebook is scored on your own laptop.

When something fails, copy the full error text into the setup status survey on Canvas, because the exact text is how the teaching assistants find the fix.

## 7. Today

Everyone does `worksheet.md`, the session 1 submission. It needs no code, takes about 60 minutes, and is due on Canvas by 11:59 pm on Friday, October 2.

If your install works, you also run `activity.ipynb`. You plot the calibration series from section 2 and type the two prompts written into the notebook, which ask Claude Code to explain each cell and then to add the fitted line. Check its explanation against what each cell printed. The notebook is not submitted.

The habit the course grades starts with the worksheet: before you analyze a file, know what the instrument measured and what each number in the file means.
