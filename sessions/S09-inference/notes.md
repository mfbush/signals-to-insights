# Session 9: Experimental design and statistical inference

Thursday, October 29. The first session on statistical inference, on Virginia Tech's 2015 survey of lead in Flint's tap water.

## Learning objectives

By the end of this session you can:

1. Compute the 90th percentile of first-draw lead by the Lead and Copper Rule's rank method, check it from the printed sorted values, and say why the rule uses it rather than the mean.
2. Put a one-sided 95% lower bound on the 90th percentile from the binomial rank, and say whether it shows a sample's exceedance of 15 and of 10 µg/L at 95%.
3. Choose a paired or a two-sample t-test for first-draw against flushed lead on the same homes, from how the data were collected, and show what the choice does to the interval.
4. Say whether a significant difference between first-draw and flushed lead is a meaningful one, in µg/L against the action level.

**AI practice.** *Give the assistant a check to run*, from session 6. After TASK 2 you ask the assistant for the 90th percentile by the rule's rank method, and for a cell that prints the sorted values around that rank with their ranks. You run the cell, read the value at the rule's rank under it, and set it beside your own TASK 2 value and the number the assistant reported.

## 1. A call on a city from a sample of homes

A state regulator decides whether a city's water exceeds the lead action level, which triggers corrosion control treatment and public notice. Wrong one way, residents keep drinking leaded water; wrong the other, a city replaces lines on noise. The call rests on lead by ICP-MS in tap water from a sample of homes.

Flint, Michigan, changed its water source in April 2014 without corrosion control, and lead from service lines and plumbing rose at the tap. The state's compliance sampling through the first half of 2015 reported the city under the action level. In August and September 2015, Virginia Tech's Flint Water Study measured the lead in 271 samples from 269 homes (FlintWaterStudy.org (2015), "Lead Results from Tap Water Sampling in Flint, MI during the Flint Water Crisis"), and that survey is today's data.

Under 40 CFR 141.80(c), a system exceeds the action level when the 90th percentile of its samples is above it. The level was 15 µg/L in 2015. The Lead and Copper Rule Improvements lower it to 10 µg/L, with compliance from 2027-11-01, and the notebook reads every result against both, levels fixed before anyone looks at the data.

## 2. The 90th percentile by the rule's rank

Session 8 left the 90th percentile for today. The rule, 141.80(c)(3), says to sort the results from lowest to highest, multiply the number of samples by 0.9, and take the value at that rank as the 90th percentile. A **rank** is a position in the sorted list, counted from 1 for the lowest. Python counts from 0, so the value at rank r is `sorted_values[r - 1]`.

The worked calculation uses all 271 first draws. The rank is 0.9 × 271 = 243.9, and the rule does not say how to read a fractional rank. Rank 243 holds 25.21 µg/L and rank 244 holds 26.64 µg/L, so the four common readings are 25.21 µg/L (truncate to 243), 26.50 µg/L (interpolate, as some states' forms do), 26.64 µg/L (round up to 244) and 26.94 µg/L (rank 0.9 × (n + 1) = 244.8, used by some statistics programs). NumPy's `np.percentile` gives 26.64 µg/L, matching rounding up at n = 271 by coincidence; its `method=` argument chooses among conventions. All four are above both levels.

The mean of the same samples is 10.65 µg/L and the median 3.52 µg/L, both below 15. The 90th percentile is above it because 45 of the 271 samples are above 15 µg/L, more than one in ten.

With 60 samples, as in your draw, the rank is 0.9 × 60 = 54, a whole number, and the 90th percentile is the value at rank 54. `np.percentile` interpolates between ranks 54 and 55, which across the class's draws adds 0.015 to 1.62 µg/L.

Virginia Tech stated a detection limit of 1 µg/L and reported every result as a number, including 40 first draws and 144 two-minute samples below it. Set to 0, half the limit or the limit in both bottles, they leave the 90th percentile at 26.64 µg/L, and move the mean of first draw minus 2 min flushed only from 6.69 to 7.08 µg/L, mostly through the flushed bottle.

## 3. A lower bound on a percentile

The rule takes no bound. A 90th percentile above the level is an exceedance, and the regulator acts on it. A different 271 homes would have given a different 90th percentile, though, and a lower bound says how strongly a sample shows that the city's own 90th percentile is above the level. It guards against calling a city over on the noise of which homes were sampled.

Suppose the samples are a random draw from the city's homes. Each is then below the city's true 90th percentile with probability 0.9, and the number below it in n samples is **binomial**, with n trials and probability 0.9. `binom.ppf(0.05, n, 0.9)` returns the largest rank r for which at least r samples fall below the true 90th percentile with probability of at least 95%. When at least r samples are below it, the value at rank r is below it too, so that value is a **one-sided 95% lower bound** on the 90th percentile. It is one-sided because the regulator asks one question, whether the city is above the level.

Note that Virginia Tech's homes were volunteers, not a random draw, and a utility's compliance sites are chosen by rule. In the notebook each draw is a random 60 of the 271 samples, so there the bound is a bound on those 271.

For all 271 samples, r = 236, and the value at rank 236 is 19.12 µg/L; at least 236 samples fall below the true 90th percentile with probability 0.951. The 90th percentile, 26.64 µg/L, is an exceedance under the rule, and the bound is above 15 µg/L, so the survey shows the exceedance at 95% as well, of 10 µg/L too. A two-sided 95% interval, from ranks 234 and 254, runs from 18.11 to 31.14 µg/L. With 60 samples its upper rank is 59, next to the largest value, so a small campaign bounds the percentile only loosely from above.

Your draw of 60 gives its own 90th percentile and its own bound at rank 50, and the bound clears 15 µg/L in 17 of the 36 draws and 10 µg/L in 35. A draw whose 90th percentile is above 15 and whose bound is below it is still an exceedance under the rule. What it lacks is strength: those 60 homes would be consistent with a city whose 90th percentile is under 15.

## 4. Paired or two-sample

Each home gave a first draw after at least 6 hours without use, then samples after 45 s and 2 min of running the tap. To ask how much lead stagnant water adds, compare first draws with 2 min flushed samples, choosing the test by how the data were collected.

A **two-sample t-test** (`ttest_ind`) treats the two bottles as two separate groups and compares their means. Its spread includes the differences between homes. A **paired t-test** (`ttest_rel`) takes each home's first draw minus its own flushed sample and tests whether those differences average zero. Pairing removes whatever a home's two samples share, and fits when each pair comes from one tap.

On all 271 samples the mean difference is 6.99 µg/L. The paired 95% interval runs from 4.83 to 9.14 µg/L, and the two-sample interval from 4.12 to 9.85 µg/L, wider because it carries the spread between homes. The gain from pairing depends on whether a home high in one bottle is high in the other: across the 36 draws the paired interval is 0.33 to 1.00 times the two-sample width, and in 6 draws the paired test finds a difference that the two-sample test misses at p < 0.05.

## 5. Significant against meaningful, in µg/L

A **p value** is the probability of a difference at least this large if the true mean difference were zero. A small p value does not say the difference matters. A difference of 0.1 µg/L with p = 0.001 would change no one's call, whereas the 6.99 µg/L here is more than two-thirds of the 10 µg/L level.

Ask what the difference does to the decision. The same rule applied to the 2 min flushed samples gives a 90th percentile of 7.07 µg/L on all 271, below both levels, and the 2 min flushed 90th percentile is below 10 µg/L in all 36 draws. A protocol that flushed the tap before filling the bottle would have passed a city whose first draws fail, which is why the rule fixes the sample before any result is read.

Sheet 3, not used, sets Virginia Tech's first draws beside the state's (MDEQ's) results at 21 homes: MDEQ's was lower or not detected at 16 and higher at 5.

## 6. Give the assistant a check to run

Two ways to compute a 90th percentile look right and are not the rule's: `np.percentile(x, 90)`, which interpolates between ranks 54 and 55, and `np.sort(x)[int(0.9 * len(x))]`, which counts from 0 and lands on rank 55. An assistant may also report a number from a script it ran outside your notebook.

So the prompt asks for a cell that prints the sorted values at ranks 52 to 57 with their ranks. Run that cell yourself and read rank 54 under it. Then set three numbers side by side: the printout's, your TASK 2 value and the assistant's. The printout is the check; the sentence in the chat is a claim.

## 7. Today

Your draw, `draw_01` to `draw_36`, is assigned on the board. Section 1's first code cell downloads the Flint file; if the download fails, we will post the file on Canvas. Section 1 works through all 271 samples. Section 2 selects your 60 samples (TASK 1), reads the 90th percentile at rank 54 (TASK 2) and the lower bound at rank 50 (TASK 3), and makes the call two ways (TASK 4). Section 3 runs both tests on your homes.

The judgment cell is scored 0 to 2 by the rubric in the syllabus, in the format on the AI practices page. Part (a) asks whether your draw is an exceedance of 15 µg/L and of 10 µg/L under the rule and whether its lower bound shows it at 95%, citing your output. Part (b) is one entry with a reason from your output. To submit, click **Restart**, then **Run All**, save, and upload `activity.ipynb` to Canvas by 1:30 pm on Tuesday, November 3. The rule makes the call, and the bound says how much 60 homes can show.
