# School_District_Analysis

# Overview of the school district analysis: Explain the purpose of this analysis.
Our purpose is to create a reporting script that can be ran to get recurring reports based on school size, budget, type by grade etc. It also allows us to create additional reports/modifications as needed. Additionally, we were informed that 9th grade students from Thomas High may have cheated so we are scrubbing their data from our reports to re-evaluate the report scores we have issued.

# Results: Using bulleted lists and images of DataFrames as support, address the following questions.

## How is the district summary affected?
First, we should note that student size and budget did not change - the student IDs are still valid and budget was calculated from school data (not student data). Overall, there was little change in the district scores - a 1% increase for % passing reading and % overall passing rates, and a .1 increase in average math score. Since average reading score did not change (while % passing did), our conclusion is that Thomas High students achieved a 81.9 reading score on average, and the reduction to the pool of scores used to calculate these averages is why the reading & overall passing % increased. 
Thomas High has a non-extreme budget for its students (~$630/student) and are typical for size (~1,200) so it's very possible that the scores are valid, though other evidence could exist. It is very surprising that Thomas High achieved the average math and reading scores almost perfectly though (only .1 score off of math), so additional analysis would be warranted.
## How is the school summary affected?
## How does replacing the ninth graders’ math and reading scores affect Thomas High School’s performance relative to the other schools?
How does replacing the ninth-grade scores affect the following:
Math and reading scores by grade
Scores by school spending
Scores by school size
Scores by school type
# Summary: Summarize four major changes in the updated school district analysis after reading and math scores for the ninth grade at Thomas High School have been replaced with NaNs.
