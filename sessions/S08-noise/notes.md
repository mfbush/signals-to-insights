# Session 8: Noise in chemical measurements

Tuesday, October 27. The first session on a real count trace from a mass spectrometer, and on a detection limit that a federal rule defines and a laboratory has to meet.

## Learning objectives

By the end of this session you can:

1. Show from a measured ICP-MS count trace that counts scatter with a variance close to their mean, that a window four times longer halves the relative noise, and where that stops, with a seeded Poisson simulation beside the measured windows.
2. Compute the spike MDL and the blank MDL by 40 CFR 136 Appendix B at each integration time, report the greater, and show from your table how far 3 times the blanks' standard deviation falls below it.
3. Choose an integration time and a background treatment from the MDL each gives, and show by how much each fourfold step lowers the MDL against the halving counting alone would give.
4. Report each home's lead as a number or as zero by the MDL, and check an assistant's first answer against these notes, correcting it at once if it is wrong and clearing the conversation before a better prompt.

**AI practice.** *Correct early, and clear context.* Before TASK 2 you ask the assistant for your lab's detection limits in plain words and check its first answer against section 3 below: t or 3, the blanks' mean, the greater of two. You correct a wrong answer at once, in one sentence, then clear the conversation and ask again with a prompt that carries this page's words.

## 1. A lead result is a number or zero

A drinking-water laboratory measures lead in tap water from homes, and federal rules decide how each result is written down. 40 CFR 141.89 requires the lab to reach a **method detection limit** (MDL) for lead of 0.001 mg/L, which is 1 µg/L, by the procedure in 40 CFR 136 Appendix B, and to report every result below its MDL as zero. A result between the MDL and 5 µg/L, the practical quantitation level, may be reported as measured or as 2.5 µg/L; the notebook reports it as measured. The lab's manager sets how long the instrument counts each reading and how the background is subtracted, and these set the MDL. Set the MDL too low, and results the lab cannot tell from its own blanks go into a home's record as lead. Set it too high, and homes with lead are recorded as zero.

These calls fall near 1 µg/L, a tenth of the 10 µg/L action level that applies from November 2027. The action level is a 90th percentile over many homes, which a call near the MDL moves only when that percentile sits near the MDL; session 9 computes it.

## 2. Counting ions gives Poisson noise

An ICP-MS turns the lead in a sample into ions and counts them as they reach the detector, so each reading is a whole number. To see what that does to the noise, look at a solution whose concentration does not change. Today's real trace is dissolved silver at 0.1 µg/L, counted in windows of 1 ms for 60.0 s: 59,999 readings with a mean of 2.800 counts.

When ions arrive independently, the counts in a window follow a **Poisson distribution**, whose variance equals its mean. A reading of N counts then carries a standard deviation of √N, and a relative standard deviation of 1/√N, i.e., √N divided by N. The trace's variance over its mean is 1.048, close to 1. Summed into longer windows, its relative standard deviation is 0.612 at 1 ms and 0.166 at 16 ms, close to 1/√N (0.598 and 0.149). A window four times longer holds four times the counts and halves the relative noise.

That rule stops near 16 ms. At 1.02 s the trace's relative standard deviation is 0.0247, whereas 1/√N gives 0.0187, and at 4.10 s it is 0.0164 against 0.0093. The extra noise comes from the plasma and the sample introduction, which wander over tens of milliseconds to seconds, and counting longer does not average it away. Seeded Poisson counts with the same means follow 1/√N all the way, so the difference is in the instrument.

## 3. The method detection limit by Appendix B

To find its MDL, a lab prepares seven **method blanks**, clean water taken through every step of the method, and seven **spikes**, the same with a known amount of lead added, and reads them on at least three days.

The spike MDL is MDL_s = t × s_s, i.e., Student's t times the standard deviation of the seven spike results. The blank MDL is MDL_b = mean_b + t × s_b, i.e., the blanks' mean plus t times their standard deviation, with a negative mean taken as zero. The lab's MDL is the greater of the two. Here t is the one-sided Student's t at 99% for six degrees of freedom, one fewer than the seven replicates, which Appendix B tabulates as 3.143. In the notebook it is `T_99` in Parameters.

The worked calculation uses the notebook's section 1 method study at 0.4 s. The seven spikes have a standard deviation of 0.0949 µg/L, so MDL_s = 3.143 × 0.0949 = 0.298 µg/L. The seven blanks have a mean of 0.209 µg/L and a standard deviation of 0.139 µg/L, so MDL_b = 0.209 + 3.143 × 0.139 = 0.646 µg/L. The MDL is 0.646 µg/L, set by the blanks.

Two shortcuts give a lower number. The spike MDL alone, 0.298 µg/L, leaves out the lead the blanks carry. The older rule of 3 times the blanks' standard deviation, which session 1 used, gives 0.417 µg/L here: it uses 3 in place of 3.143 and drops the blanks' mean. A blank's mean above zero is lead that every sample also picked up from its reagents, so a result just above that mean is no evidence of lead from the tap.

## 4. Noise a longer count does not remove

A longer integration time lowers only the part of the noise that comes from counting. In the method study the spike MDL falls from 1.306 µg/L at 0.025 s to 0.757 at 0.1 s and 0.298 at 0.4 s, close to the 1/√t that counting alone predicts. At 1.6 s it is 0.281 µg/L, whereas counting alone would give 0.163.

What stops it is noise that is the same however long you count. Each blank and spike picks up its own small amount of lead from the acids in preparation, so the seven differ before any ion is counted, and each reading carries the plasma's slower noise, the floor of section 2. The background also rises through the day, and a blank read in the afternoon carries more of it than one read in the morning. These are **systematic** in a single reading, the same in every count of it, and a longer count measures them more precisely without making them smaller. **Random** noise, such as counting noise, averages away.

Drift can be corrected another way. The run reads a **calibration blank**, clean acid with no lead, before every fourth sample. Treatment A subtracts the background at the start of the day, from the day's calibration line, so every later reading, homes included, carries the drift as apparent lead. Treatment B subtracts the calibration blanks' count rate interpolated to the minute of each reading, so it follows the drift, at the cost of those blank readings, where EPA Method 200.8 asks for one per ten samples. The notebook's section 3 computes both and prints each cost.

The notebook records a result below the MDL as zero, as the rule requires, with a `detected` column beside it. In session 5 a below-limit result became `NaN`, because an analysis of how often a compound occurs asks a different question than a compliance record.

## 5. What the MDL does not promise

The MDL protects against one error, reporting lead in a home whose sample held none, and does not promise that a home with lead is reported as a number. A home whose true lead equals the MDL gives results that scatter around the MDL, so about half of them fall below it and are reported as zero. Currie's **detection limit**, L_D (IUPAC, 1995, [doi:10.1351/pac199567101699](https://doi.org/10.1351/pac199567101699)), is the true concentration detected with high probability, and when the noise is the same near zero it is about twice the critical level that the MDL resembles. A home between the MDL and L_D is often reported as zero, a cost of the rule rather than an error in the arithmetic.

## 6. Correct early, and clear context

The assistant answers from what is in its conversation and what it reads in the repository, including this page. Its first answer to a plain question about detection limits is often right, and then the practice is to verify it: check t, the blanks' mean and the greater of two against section 3, and the numbers against your own table. If one is wrong, correct it at once in one sentence that names the fix. An early correction costs one message; a late one costs the table.

If two corrections have not fixed it, clear the conversation rather than send a third, because each failed attempt stays in the conversation and pulls the next answer toward it. Then write a better first prompt, one that names this page's section, your variables, the columns and the units. The notebook has you clear and send such a prompt either way, so you see what it changes.

## 7. Today

You have one lab, assigned on the board from `lab_01` to `lab_36`, in `data/labs/`; set `LAB` in Parameters, and nothing is downloaded. Section 1 reads the silver trace, sums it into longer windows and compares it with Poisson counts, then computes the spike MDL of one lab's method study at each integration time. Section 2 reads your lab (TASK 1), asks the assistant for the detection limits twice, before and after clearing, computes the blank MDL and the greater of the two at each time (TASK 2), and asks you to choose an integration time (TASK 3) and report your 40 homes (TASK 4). Section 3 computes everything again with bracketing calibration blanks and prints what each treatment costs.

The judgment cell is scored 0 to 2 by the rubric in the syllabus, in the format on the AI practices page. Part (a) asks which integration time and which background treatment you would set for your lab, with your spike MDL, blank MDL and the greater under that treatment, how many homes it reports as numbers, how many calls the spike MDL alone would have changed, and what the other treatment would have cost. Part (b) is one entry with a reason from your output; the answers before TASK 2 are its natural source. To submit, click **Restart**, then **Run All**, save, and upload `activity.ipynb` to Canvas by 1:30 pm on Thursday, October 29. A longer count lowers only the counting noise.
