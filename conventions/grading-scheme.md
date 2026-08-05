# assessment scheme: the 0-4 grade-point model

A reusable grading scheme, recorded here so it can be applied consistently across other syllabi. It covers what the scheme is, why it took its present form, the exact charts and student-facing sentences to reproduce, the Canvas setup that makes the gradebook agree with the syllabus, and the decisions to settle when applying it to a new course.

## the core idea

Each graded assignment is scored 0 to 4, and that score is its grade-point value: 4 is an A, 3 a B, 2 a C, 1 a D, 0 an F. The course grade is the average of the assignment scores (weighted if the assignments carry different weights), which is the course GPA, converted to a letter.

The 0 to 4 score is grade points, not a percentage. A student who does consistently good work (3s) averages 3.0, which is a B. Nothing is divided by four.

## two bugs this scheme has already been through

Both are recorded so neither gets reintroduced.

The first was the divide-by-four conversion. An earlier scheme converted the 0 to 4 average to a letter by treating it as a percentage: average divided by 4, times 100. That turned a 3 into 75%, which read as a C, so consistently good work came out a C.

The second was the parallel percentage column. The chart carried a course average column and a percentage column side by side, with the percentage giving the conventional equivalent of the letter (a B at 80 to 89%) rather than the average divided by four. The two columns were internally consistent only if nobody computed the points. Canvas does compute the points: with every item out of 4, an average of 3.0 shows as 75% in the gradebook, which the percentage column called a C while the average column called it a B. At 2.7 the gap was worse, a B minus by average and 67.5% of points. The percentage column has been dropped. The course average is the only conversion the syllabi state.

## grade conversion chart (use as is)

| grade | course average / GPA |
|---|---|
| A | 4.0 |
| A- | 3.7 |
| B+ | 3.3 |
| B | 3.0 |
| B- | 2.7 |
| C+ | 2.3 |
| C | 2.0 |
| C- | 1.7 |
| D+ | 1.3 |
| D | 1.0 |
| F | below 1.0 |

Notes on the chart:

- These are grade-point anchors, not range endpoints. The rounding rule below is what turns an average falling between two anchors into a letter, so the anchors and the rule have to travel together.
- All 11 anchors are listed rather than collapsed into 5 bands, so a student can see which of B-, B, and B+ a given average lands on.
- The values are the CSUEB standard: A 4.0, A- 3.7, B+ 3.3, B 3.0, B- 2.7, C+ 2.3, C 2.0, C- 1.7, D+ 1.3, D 1.0, F 0.0. Source: the GPA computation policy, https://www.csueastbay.edu/aps/academic-services/academic-policies/gpa-computation.html

## student-facing text to reproduce below the chart

Two paragraphs, in this order and close to this wording:

> An average that falls between two grades is rounded to the nearest one, and an exact midpoint is rounded up in your favor. A term of steady 3s averages 3.0 and posts as a B. Mostly 3s with a few 4s lands near 3.2, which rounds to 3.3 and posts as a B+.

> Canvas displays a running percentage of the points you have earned out of the points available, so a 3.0 average appears there as 75% and posts as a B under the scale above.

The worked example is the fastest way for a student to see that the scale is grade points. The Canvas sentence heads off a term of watching a number that looks like a C while holding a B.

## per-assignment rubric

Score each assignment 0 to 4. The level names and descriptions are course-specific: rewrite the descriptions for the work each course assigns. Only the 0-to-4 grade-point structure is fixed. The MUS 601 version, as a model:

| score | level | description |
|---|---|---|
| 4 | outstanding | top-level work, the standard the course aims for |
| 3 | good | solid and well executed, minor gaps |
| 2 | below average | present but underdeveloped |
| 1 | unacceptable | minimal or seriously flawed |
| 0 | not submitted | no submission, or work that does not engage the task |

No letter tags in the level column, and keep the 5 integer levels tied to 4/3/2/1/0 = A/B/C/D/F.

A caution on the score-of-2 description. A 2 is a C, which passes and sits above the C- that undergraduate majors and minors need for a course to count. Description language calling a 2 unpassing contradicts the scale. Describe what the work lacks, and leave the consequence to the minimum-grade block, which names C- as the real threshold.

## canvas setup

The gradebook agrees with the syllabus only if the course is built so that the Canvas percentage is a faithful image of the 0 to 4 average. Two conditions:

- Every graded item is worth exactly 4 points in Canvas. Mixed point values break the correspondence.
- Weighting runs through weighted assignment groups whose percentages match the syllabus table, rather than through unequal point totals.

With those in place, the Canvas percentage is the weighted average divided by 4, times 100, and a custom grading scheme converts it back. The boundary for each letter is the midpoint between its anchor and the next anchor down, which is the rounding rule expressed as a percentage:

| letter grade | canvas lower bound |
|---|---|
| A | 96.25 |
| A- | 87.5 |
| B+ | 78.75 |
| B | 71.25 |
| B- | 62.5 |
| C+ | 53.75 |
| C | 46.25 |
| C- | 37.5 |
| D+ | 28.75 |
| D | 25 |
| F | 0 |

Checked against every anchor: 4.0 posts A at 100%, 3.7 posts A- at 92.5%, 3.3 posts B+ at 82.5%, 3.0 posts B at 75%, 2.7 posts B- at 67.5%, 2.3 posts C+ at 57.5%, 2.0 posts C at 50%, 1.7 posts C- at 42.5%, 1.3 posts D+ at 32.5%, 1.0 posts D at 25%. The syllabus worked example holds too: 3.2 is 80%, which clears the 78.75 boundary and posts B+.

The default Canvas scheme cannot be used with this model. Left in place, it posts a 3.0 average as a C.

## decisions to settle per course

- Graduate versus undergraduate standing. The MUS 601 syllabus adds graduate rules from the Graduate Student Handbook: only C or better counts toward the degree, a C- or below must be repeated, and a cumulative 3.0 GPA is required to stay in good standing (below it triggers academic probation). Those are graduate rules. The lower-division courses are undergraduate, so do not copy that language. Use the undergraduate standing and minimum-grade rules instead.
- Weighting. In 601 the five papers weigh equally, so the course average is a straight mean. If a course weights assignments differently, use the weighted average of the 0 to 4 scores. The conversion chart does not change.

## style, to match across syllabi

- One row per grade, high to low, A through F.
- The column header reads "course average / GPA", and the numeric column is right-aligned, per the table treatment in house-style.md.
- The rounding rule, the worked example, and the Canvas sentence sit below the chart as prose, in the wording given above.
