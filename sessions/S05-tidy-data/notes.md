# Session 5: Tidy data and the sample table

Thursday, October 15. The first session in pandas, on the EPA's UCMR 5 monitoring data for PFAS in drinking water.

## Learning objectives

By the end of this session you can:

1. State the three rules of tidy data, and point to the cell, column or row in a wide laboratory report that breaks each one.
2. Reshape a wide results table to one measurement per row with pandas, split a composite sample identifier into its parts, and encode a below-reporting-limit result as missing rather than zero.
3. Join the measurement table to the sample table on its key with a left merge, and say what an inner merge would have discarded.
4. Compute a detection rate and a mean detected concentration by group, and say how the choice of what counts as an observation changes the number.

## 1. A table you can read is a table you cannot query

Between 2023 and 2025 every large public water system in the United States, and a sample of the small ones, measured 29 PFAS in the water it delivers, under the Fifth Unregulated Contaminant Monitoring Rule, and the EPA publishes every result: 1,992,002 of them. Today's file for Washington is the first sampling event's results for six of those PFAS, laid out the way a laboratory reports them: one row per sample, one column per compound, so that you can read across a row for all six results. That layout is easy to read and hard to compute on. To ask "how often was PFOA detected in groundwater" of it, you would have to pick one column by name, parse its cells, and look up each sample's water type somewhere else.

Tidy data, i.e., the layout in which one row is one observation, one column is one variable, and one cell is one value, is the layout every pandas operation assumes. Against those three rules the laboratory report breaks all three. `PFOA` is a column name, whereas the compound is a variable and belongs in a column of its own. A row bundles six measurements. Two kinds of cell hold more than one value: `WA5300050_TP1_2024-01-17_SE1`, which is a system id, a sample point, a date and an event joined by underscores, and `< 0.004`, which is a code meaning "below the reporting limit of 0.004 µg/L". The activity repairs the three in four steps and then asks the question in one line.

## 2. Four steps, and the rule each restores

To split the identifier, apply session 4's `split` to every row at once: `results["sample_id"].str.split("_", expand=True)` returns a table with one column per piece, and each piece becomes a column of its own, which restores one value per cell for the identifier.

To make the compound columns numeric, decide first what a below-limit result is. It is a measurement that was made and did not reach the reporting limit; it is not zero and not a number the laboratory measured. pandas has a value for that, `NaN`, which `mean` and `count` skip. The activity marks the cells whose text starts with `<`, sets them to `NaN` with `.loc`, and converts the rest with `astype(float)`. Although `pd.to_numeric(errors="coerce")` gives the same `NaN` values in one call, it does so by discarding any text it cannot parse, so it records nothing about why a value is missing; mark the below-limit results first and the count of `NaN` values is then a count you can check against the file.

To get one measurement per row, `melt` keeps the identifier columns and turns the six compound columns into two, one holding the old column name and one the value: `results.melt(id_vars=[...], value_vars=PFAS, var_name="compound", value_name="concentration_ug_L")`. Six times as many rows, `PFOA` is now a value you can filter on, and one row is one measurement, which restores one variable per column and one observation per row together. A `detected` column, true where the concentration is not `NaN`, records the laboratory's yes or no.

## 3. The sample table and the left merge

A measurement table records what the instrument reported. A sample table records what each sample was: here, for each sample point, the water system it belongs to, the system's name and size, and whether the facility draws groundwater or surface water. Your lab notebook is a sample table in prose; the digital version has one row per sample and one column per fact, and a key that the measurement table shares. Here the key is two columns, the system id and the sample point id, and `merge(samples, on=["pwsid", "sample_point_id"], how="left")` attaches the facts to every measurement row.

`how` is a choice with consequences. A left merge keeps every measurement row and marks a sample point with no sample table row as `NaN` in the attached columns, so the gap is visible. An inner merge keeps only rows with a match on both sides, so a measurement whose sample point is missing from the sample table vanishes without a trace. In this session's files every sample point has a row, the counts before and after are equal, and the notebook prints 0 rows that an inner merge would drop; the reason to write `left` anyway is the file where that number is not 0. Read the identifier columns as text when you load the sample table, with `dtype`, because a sample point id such as `001` is a label, and `read_csv` would otherwise turn it into the number 1.

## 4. Below the reporting limit is not zero

The choice in step 2 sets the answer to the session's question. New Jersey's first sampling event has 815 PFOA results; 292 are above the reporting limit and their mean is 0.00912 µg/L, 2.3 times the maximum contaminant level of 0.004 µg/L that the EPA set in April 2024. That level equals the reporting limit in this program, so every detection is at or above it. Store the 523 below-limit results as zero and the mean of the 815 becomes 292 times 0.00912 over 815, 0.00327 µg/L, below the level, for a state where every measured value is above it. Store them as `NaN` and `mean` returns the mean of the 292 measurements, with `count` giving 292 to say how many that is. Zero substitution does not lower a true value; it invents 523 values that were never measured.

What to do with the `NaN` values afterwards is a separate decision, made in the open: leave them out, as here; replace them with half the reporting limit, a common convention; or use a method built for censored data. Each is defensible when it is stated. Zero is not, because it is a claim.

## 5. What is an observation

A detection rate is a count of detections over a count of something, and the something is a choice that the tidy table makes explicit. Per result, it is detections over measurements, which is what the laboratory's table gives directly. Per sample point, it is entry points with at least one detection over entry points. Per system, it is water systems with at least one detection over systems, which a regulator asks for, because the maximum contaminant level applies to the water a system delivers. With one measurement per row, each is one `groupby`: group by the system id, take `.any()` of `detected`, which is true for a group if any row in it is true, and take the mean of that. For New Jersey the per-result and per-system rates are 35.8% and 49.8%, because a system with several entry points and one detection is one detecting system but mostly non-detecting results. Section 3 of the activity computes all three for your state, and the judgment cell asks which one answers the question.

## 6. Today

You have one state, assigned on the board. Set its code in Parameters; its two files are in the repository, so nothing is downloaded. Section 2 turns section 1's first three steps into a function, merges your state's sample table, and computes PFOA by water type; two prompts to the assistant, before the function and before the merge, are where part (b) of the judgment cell comes from. Section 3 computes the three rates.

The judgment cell is scored 0 to 2 by the rubric in the syllabus, in the format on the AI practices page. Part (a) asks for your two rates with their denominators, the mean detected concentration, which rate answers the systems question, and what the mean would have been with zeros. Part (b) is one entry with a reason from your tables. To submit, click **Restart**, then **Run All**, save, and upload `activity.ipynb` to Canvas by 1:30 pm on Tuesday, October 20. A below-limit result is a measurement that was made, and the table has to say so.
