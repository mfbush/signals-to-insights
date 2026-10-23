# Session 12: Peak detection and feature extraction

Tuesday, November 10. A quality-control analyst at a supplier or a pharmacy decides whether a commercial lavender oil meets the European Pharmacopoeia's chromatographic profile, a set of ten limits on its composition, each read from a gas chromatogram as an area percent. Today's activity tests three of them: camphor at most 1.2%, linalool 20.0 to 45.0%, and linalyl acetate 25.0 to 47.0%. Each percentage depends on which peaks are counted and where each starts and ends. You choose those settings for three runs of one oil from a [published dataset of 55 commercial oils](https://doi.org/10.17632/pgkrc7wyj4.1) and decide whether the oil meets the three limits. Then you test whether a second way of integrating the peaks would change your call.

## Learning objectives

By the end of this session you can:

1. Inspect a chromatogram and choose peak-detection settings from its noise, its narrowest peak, and the smallest peak that must be counted. Show that a threshold set too low counts noise as peaks and one set too high leaves out small real peaks.
2. Integrate each peak between the lowest points that separate it from its neighbors. Report each component's area as a percent of the summed area of all the peaks counted.
3. Decide whether a sample meets a specification from three replicate runs, their spread, and the distance to the nearest limit.
4. Integrate the same peaks by a second rule and show how far it moves each result. Say whether it would change your call.
5. Write a skill for a step you repeat. Check its output against a table you built by hand, and decide whether to change the skill before you use it on new data.

**AI practice.** *A SKILL.md for a repeated step*, new today. After the notebook's section 1 you save its method as a skill, from a template with four blanks, and run it on Dataset A in a new conversation. You decide whether its values match your hand-built table within 0.01 points. If they do not, you decide what in `SKILL.md` to change before you run it on your own runs. A three-line prompt record holds your prompt, both comparisons, and what you changed or verified, and the execution point needs it.

## 1. Area percent and the pharmacopoeia's profile

The [European Pharmacopoeia monograph on lavender oil](https://www.drugfuture.com/Pharmacopoeia/EP7/DATA/1338E.PDF) (Ph. Eur. 1338) reads a gas chromatogram with flame ionization detection (GC-FID) by **normalization**: each peak's area as a percentage of the summed area of all peaks, its **area percent**. A peak under 0.05% of that sum falls below the **disregard limit** and is left out of it. The monograph sets the limit with a reference solution; today's runs include none, so the activity takes it as 0.05% of the total area.

[Linalool](https://pubchem.ncbi.nlm.nih.gov/compound/Linalool) and [linalyl acetate](https://pubchem.ncbi.nlm.nih.gov/compound/Linalyl-acetate) give the two largest peaks in a true lavender oil, and [camphor](https://pubchem.ncbi.nlm.nih.gov/compound/Camphor) a small one. Lavandin, a cheaper hybrid of lavender, is richer in camphor, which is why the profile caps it. The monograph gives the components' elution order, not their retention times on a given column. The files in today's dataset name no peak, so the activity places the three by that order, and camphor's place was confirmed by its mass spectrum in one oil.

A wrong call costs in either direction. An oil cut with lavandin or with synthetic linalool can be sold as pharmacopoeial, and a genuine lot can be rejected and its supplier lose the sale. Of 51 oils sold as true lavender, [Pokajewicz, *Farmacja Polska* (2025)](https://doi.org/10.32383/farmpol/211704) classed 51% as genuine and the rest as lavandin, lavandin with synthetic additions, or artificial mixtures.

All three percentages share one denominator, so a peak counted or missed anywhere moves all three. Section 2 sets which peaks count.

## 2. Peak detection: noise, prominence, width, and spacing

`find_peaks` from SciPy returns the local maxima of a signal that meet the settings you give it. A peak's **prominence** is how far its apex rises above the higher of the lowest points on either side before taller signal, so a small peak on a large one's flank is measured from where it rises, not from the baseline. Its **width** is taken at half the prominence, in points, and the **distance** is the fewest points allowed between two apexes.

Each setting comes from the measurement, through two numbers. The **noise** is the scatter of the signal where no peak elutes: the standard deviation of the differences between neighboring points, divided by the square root of 2, because each difference carries two points' noise. The **narrowest full width at half maximum (FWHM)** is the width at half height of the narrowest real peak.

The prominence starts from the smallest peak that must count, one at the disregard limit, whose area is 0.05% of the total. A Gaussian peak's area is its height times its FWHM times 1.064, so a peak that small and that narrow stands

height = (0.05% of the total area) / (1.064 × narrowest FWHM)

above its baseline: the area of a peak at the disregard limit divided by 1.064 times the narrowest width. The prominence is half that height, so that such a peak on a neighbor's flank, where its prominence is less than its height, is still found. The width setting is half the narrowest FWHM, which drops spikes narrower than any real peak, and the distance is the whole FWHM, which keeps one apex per peak. Without the distance, a flat-topped apex comes back as two.

A prominence set lower finds noise. The disregard limit drops most of what it adds, but every bump that stays enlarges the total. A prominence set higher, for example one read from how the plot looks, misses small real peaks just above the disregard limit, so the total shrinks and every component's share grows. Figure 1 shows the three settings on Dataset A, the run the notebook's section 1 works through.

![Dataset A's signal from 44 to 52 min on a 0 to 3 mV scale, near 1 mV between peaks. Crosses mark 26 apexes, most of them small bumps; circles mark 13; triangles mark 7, missing six small peaks the circles mark.](figures/detection.png)

*Figure 1. Dataset A from 44 to 52 min, with the apexes found at 5 times the noise (crosses), at the disregard limit (circles) and at 0.5 mV (triangles). Look for small peaks circled but without a triangle.*

Section 3 sets where each peak starts and ends.

## 3. Integration: bounds, drop-line, and valley skim

Once its apex is found, a peak needs a start and an end. Its **bounds** are the lowest points of the signal between its apex and each neighbor's apex, searched only a fixed number of points away. Its area, in mV min, is the signal above a baseline between the bounds, summed by `trapezoid` from SciPy.

- The **drop-line** rule draws one baseline through the bounds that sit on the true baseline, and splits a cluster of overlapping peaks by a vertical line at each valley.
- The **valley-skim** rule draws a straight line under each peak between its own two bounds, so the area under a shared valley belongs to neither peak.

The two rules agree wherever the signal returns to the baseline between peaks, and part where two peaks overlap. Figure 2 shows a doublet whose valley sits far above the baseline, in run A of the solution's oil, which no student holds. Each skim line rises from an outer bound on the baseline to the high valley, and on the peak's outer flank it runs above the signal, so the skim subtracts the area between them. Both skim areas come out negative, so both peaks fall under the disregard limit and leave the total. In that run linalool rises from 19.16 to 22.97%, across the 20.0% limit, with its own area the same by both rules. A valley that does not return to the baseline calls for the drop-line.

![A doublet in one GC-FID run, peaks 22.9 and 26.1 mV at 59.45 and 59.55 min, valley 16.3 mV. A dashed drop-line baseline runs flat near 1 mV; dotted skim lines rise from 59.12 and 60.04 min to the valley, above both outer flanks.](figures/valley.png)

*Figure 2. A doublet whose valley does not return to the baseline, with the drop-line baseline (dashed) and the valley-skim lines (dotted). Look where the dotted lines cross the signal.*

An area percent is complete only with the list of peaks its total includes. Section 4 sets how far from a limit a value must sit for a call on it to hold.

## 4. Replicate runs and the margin to a limit

One run gives one value, and replicate runs show how far that value moves when nothing about the oil changes. The mean over runs A, B, and C is the result, and their standard deviation is the **replicate spread**. The **margin** is the distance from the mean to the nearest limit, in percentage points. A margin many times the spread holds; a call on a margin smaller than the spread could reverse with the next run.

The integration rule is a third distance. A call depends on the rule only where the shift between the two rules exceeds the margin. The data system's area percents come from its own list of peaks, so quote them beside yours, not in their place.

## 5. A SKILL.md for a repeated step

A **skill** is a file of instructions, `SKILL.md`, in a folder under `.claude/skills/`, that Claude Code runs as a command when you type `/` and its name ([Claude Code skills](https://code.claude.com/docs/en/skills)). Its header gives the `name` and a `description` of when to use it; the body is the method, with `$ARGUMENTS` standing for what you type after the command, here a run's path.

The body states every choice of the method as a number, from the stretch searched to each component's time and range. The template gives every window in points, because a looser wording is read one way by the assistant and another by your code. In the course's trials, run before these notes existed, a skill that stated no baseline chose a flat line at the run's minimum and read linalool several points low.

The check is to run the skill once on data whose answer you know. A skill that follows the method reproduces Dataset A's hand-built table within 0.01 points, the last digit of a rounding. A match counts only if the skill's own text made it: read the report's parameter line and anything it took from outside `SKILL.md`, such as these notes, and write that step into the file. A larger difference points at a step in `SKILL.md` to change before the skill reads your runs, and TASK 3's table is the second check. That order, a known answer first and new data second, holds for any skill you write.

## 6. Today

Your oil is beside your student number from session 4 in `data/samples.csv`.

The judgment cell is scored 0 to 2 by the rubric in the syllabus: part (a) is your oil's call with its evidence, part (b) one entry with a reason from your output. To submit, click **Restart**, then **Run All**, save, and upload `activity.ipynb` to Canvas by 1:30 pm on Thursday, November 12.

Your call rests on three distances read together: the margin, the spread, and the rule's shift. A drop-line splits a doublet by a vertical line at its valley; session 13's `curve_fit` offers the alternative, a peak shape fitted to each.
