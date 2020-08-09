# School_District_Analysis

# Overview of the school district analysis: Explain the purpose of this analysis.
Our purpose is to create a reporting script that can be ran to get recurring reports based on school size, budget, type by grade etc. It also allows us to create additional reports/modifications as needed. Additionally, we were informed that 9th grade students from Thomas High may have cheated so we are scrubbing their data from our reports to re-evaluate the report scores we have issued.

## How is the district summary affected?
First, we should note that student size and budget did not change - the student IDs are still valid and budget was calculated from school data (not student data). We needed to create another student count though, to account for the missing 9th graders from Thomas (otherwise Thomas pass rates will plummet since the numerator will go down with the NaNs while the denominator will not since it's not based on math or reading scores)
Overall, there were small changes to the district scores - a 1% decrease for reading math and overall passing %, and a .1 decrease in average math score. Remembering that we already factored in NaN student count totals in our analysis, it is significant that ommitting one grade from 1 out of 15 schools made a noticeable impact. Since most all scores and %s decreased, it means the 9th grade of Thomas performed better than the rest of the districts in terms of score and passing %.
## How is the school summary affected?
We see that scores dropped .06 for math and reading, while % passing dropped .3% for reading and overall,  .09% for math.
## How does replacing the ninth graders’ math and reading scores affect Thomas High School’s performance relative to the other schools?
### How does replacing the ninth-grade scores affect the following:
### Math and reading scores by grade
Only 9th grade scores from Thomas will be affected, so we will look at district wide averages (as nothing will be interesting looking at school level) Math scores for 9th graders dropped .23%, quite a large drop given that Thomas is one of 15 schools. The drop in reading was a  bit smaller, at .09%.
### Scores by school spending
Thomas falls in the $630-$644 spend bucket, and saw a small drop in math score of .016 and .012 in reading score. Similar small changes in % pass rates, uncertain on how significant size differences are without further analysis.
### Scores by school size
In our bin sizes, Thomas is set as a medium sized school. The changes are minimal, a drop of .014 in math and .09 in reading scores, and similar small drops in %s. Our medium bucket is fairly small with only 5 other schools mostly bigger, but may indicate that schools at this size etc. are strong in test taking (would need additional analysis) which would explain why students at Thomas High performed so well
### Scores by school type
Small changes in the charter schools. What stands out is that charter schools in general perform much better than district schools, so the ninth grade scores do not seem atypical to what other charter schools are scoring (without going into school comparison analysis)
# Summary:
There were some small changes the scores and % percentages. The budget information didn't change, but the scores did because we are excluding 9th graders from our analysis. Small changes to the scores resulted in math % dropping .08%, reading increased by .28% and overall % dropped by .28% While it's understandable that some scores will be similar to the average (multiple similar dependencies like location, teachers, school cirriculumn etc) it is very interesting that scores are so similar without the 9th graders. My suspicions would be that if scores were manipulated, they worked to match the average of the rest of Thomas High as much as possible to avoid detection (as none of this is hard proof - just somewhat rare occurences)
