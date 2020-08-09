# Dependencies and Setup
import numpy as np
import pandas as pd

# File to Load (Remember to change the path if needed.)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read the School Data and Student Data and store into a Pandas DataFrame
school_data_df = pd.read_csv(school_data_to_load)
student_data_df = pd.read_csv(student_data_to_load)

# Cleaning Student Names and Replacing Substrings in a Python String
# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]

# Iterate through the words in the "prefixes_suffixes" list and replace them with an empty space, "".
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")

# Check names.
student_data_df.head(10)

# Install numpy using conda install numpy or pip install numpy. 
# Step 1. Import numpy as np.
import numpy as np

# Step 2. Use the loc method on the student_data_df to select all the reading scores from the 9th grade at Thomas High School and replace them with NaN.

student_data_df.loc[
    (student_data_df['school_name'] == "Thomas High School") & 
    (student_data_df['grade'] == '9th'), 
    ['reading_score']] = np.nan

student_data_df

#  Step 3. Refactor the code in Step 2 to replace the math scores with NaN.
student_data_df.loc[
    (student_data_df['school_name'] == "Thomas High School") & 
    (student_data_df['grade'] == '9th'), 
    ['math_score']] = np.nan

    #  Step 4. Check the student data for NaN's. 
student_data_df

# Deliverable 2 Requirements
school_data_complete_df = pd.merge(student_data_df, school_data_df, on=["school_name", "school_name"])

# The district summary DataFrame (3 pt)
# Total counts & sums
student_count = student_data_df["Student ID"].count()
school_count = school_data_df["school_name"].count()
total_budget = school_data_df["budget"].sum()

# dfs for passing, avgs
average_math_score = school_data_complete_df["math_score"].mean()
passing_math = school_data_complete_df[school_data_complete_df["math_score"] >= 70]
passing_math_count = passing_math["Student ID"].count()

average_reading_score = school_data_complete_df["reading_score"].mean()
passing_reading = school_data_complete_df[school_data_complete_df["reading_score"] >= 70]
passing_reading_count = passing_reading["Student ID"].count()

passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70) & (school_data_complete_df["reading_score"] >= 70)]
passing_math_reading_count = passing_math_reading["Student ID"].count()


# Calculate the percent that passed either subject. Combine for complete passing %s
passing_math_percentage = passing_math_count / float(student_count) * 100
passing_reading_percentage = passing_reading_count / float(student_count) * 100
overall_passing_percentage = passing_math_reading_count / float(student_count) * 100


district_summary_df = pd.DataFrame(
          [{"Total Schools": school_count,
          "Total Students": student_count,
          "Total Budget": total_budget,
          "Average Math Score": average_math_score,
          "Average Reading Score": average_reading_score,
          "% Passing Math": passing_math_percentage,
         "% Passing Reading": passing_reading_percentage,
        "% Overall Passing": overall_passing_percentage}])

# Format the columns.
district_summary_df["Total Students"] = district_summary_df["Total Students"].map("{:,}".format)
district_summary_df["Total Budget"] = district_summary_df["Total Budget"].map("${:,}".format)
district_summary_df["Average Math Score"] = district_summary_df["Average Math Score"].map("{:.1f}".format)
district_summary_df["Average Reading Score"] = district_summary_df["Average Reading Score"].map("{:.1f}".format)
district_summary_df["% Passing Math"] = district_summary_df["% Passing Math"].map("{:.0f}".format)
district_summary_df["% Passing Reading"] = district_summary_df["% Passing Reading"].map("{:.0f}".format)
district_summary_df["% Overall Passing"] = district_summary_df["% Overall Passing"].map("{:.0f}".format)

district_summary_df.head()

# The school summary DataFrame (3 pt)
# Can re-structure data to get most variables, use variables on capita
per_school_types = school_data_df.set_index(["school_name"])["type"]
per_school_counts = school_data_complete_df["school_name"].value_counts()
per_school_budget = school_data_df.set_index(["school_name"])["budget"]
per_school_capita = per_school_budget / per_school_counts

per_school_counts
# average by group (school name)
per_school_math = school_data_complete_df.groupby(["school_name"]).mean()["math_score"]
per_school_reading = school_data_complete_df.groupby(["school_name"]).mean()["reading_score"]

# passing %s by school

#math
per_school_passing_math = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)]
per_school_passing_math = per_school_passing_math.groupby(["school_name"]).count()["student_name"]
per_school_passing_math = per_school_passing_math / per_school_counts * 100
#reading
per_school_passing_reading = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)]
per_school_passing_reading = per_school_passing_reading.groupby(["school_name"]).count()["student_name"]
per_school_passing_reading = per_school_passing_reading / per_school_counts * 100
#overall
per_passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70) & (school_data_complete_df["reading_score"] >= 70)]
per_passing_math_reading = per_passing_math_reading.groupby(["school_name"]).count()["student_name"]
per_overall_passing_percentage = per_passing_math_reading / per_school_counts * 100

per_school_summary_df = pd.DataFrame({
             "School Type": per_school_types,
             "Total Students": per_school_counts,
             "Total School Budget": per_school_budget,
             "Per Student Budget": per_school_capita,
             "Average Math Score": per_school_math,
           "Average Reading Score": per_school_reading,
           "% Passing Math": per_school_passing_math,
           "% Passing Reading": per_school_passing_reading,
           "% Overall Passing": per_overall_passing_percentage})

per_school_summary_df.head()

# The top 5 performing schools, based on the overall passing rate (2 pt)
top5_df = per_school_summary_df.nlargest(5,"% Overall Passing")

# The bottom 5 performing schools, based on the overall passing rate (2 pt)
bot5_df = per_school_summary_df.nsmallest(5,"% Overall Passing")

# The average math score for each grade level from each school (3 pt)
# Creating grade dfs to be used
grade9_df = school_data_complete_df[school_data_complete_df['grade'] == '9th']
grade10_df = school_data_complete_df[school_data_complete_df['grade'] == '10th']
grade11_df = school_data_complete_df[school_data_complete_df['grade'] == '11th']
grade12_df = school_data_complete_df[school_data_complete_df['grade'] == '12th']

# math
grade9_math_df = grade9_df.groupby(["school_name"]).mean()["math_score"]
grade10_math_df = grade10_df.groupby(["school_name"]).mean()["math_score"]
grade11_math_df = grade11_df.groupby(["school_name"]).mean()["math_score"]
grade12_math_df = grade12_df.groupby(["school_name"]).mean()["math_score"]

math_scores_by_grade = pd.DataFrame({
               "9th": grade9_math_df,
               "10th": grade10_math_df,
               "11th": grade11_math_df,
               "12th": grade12_math_df})



# The average reading score for each grade level from each school (3 pt)
# reading
grade9_reading_df = grade9_df.groupby(["school_name"]).mean()["reading_score"]
grade10_reading_df = grade10_df.groupby(["school_name"]).mean()["reading_score"]
grade11_reading_df = grade11_df.groupby(["school_name"]).mean()["reading_score"]
grade12_reading_df = grade12_df.groupby(["school_name"]).mean()["reading_score"]

reading_scores_by_grade = pd.DataFrame({
               "9th": grade9_reading_df,
               "10th": grade10_reading_df,
               "11th": grade11_reading_df,
               "12th": grade12_reading_df})



# The scores by school spending per student (3 pt)
# Establish the bins.
size_bins = [0, 600, 625, 1000]
group_names = ["Small (<600)", "Medium (600-625)", "Large (625-1000)"]

per_school_summary_df["Student Budget Spend"] = pd.cut(per_school_summary_df["Per Student Budget"], size_bins, labels=group_names)

budget_math_scores = per_school_summary_df.groupby(["Student Budget Spend"]).mean()["Average Math Score"]

budget_reading_scores = per_school_summary_df.groupby(["Student Budget Spend"]).mean()["Average Reading Score"]

budget_passing_math = per_school_summary_df.groupby(["Student Budget Spend"]).mean()["% Passing Math"]

budget_passing_reading = per_school_summary_df.groupby(["Student Budget Spend"]).mean()["% Passing Reading"]

budget_overall_passing = per_school_summary_df.groupby(["Student Budget Spend"]).mean()["% Overall Passing"]

budget_summary_df = pd.DataFrame({
          "Average Math Score" : budget_math_scores,
          "Average Reading Score": budget_reading_scores,
          "% Passing Math": budget_passing_math,
          "% Passing Reading": budget_passing_reading,
          "% Overall Passing": budget_overall_passing})

budget_summary_df

# The scores by school size (3 pt)
# Establish the bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]

per_school_summary_df["School Size"] = pd.cut(per_school_summary_df["Total Students"], size_bins, labels=group_names)

size_math_scores = per_school_summary_df.groupby(["School Size"]).mean()["Average Math Score"]

size_reading_scores = per_school_summary_df.groupby(["School Size"]).mean()["Average Reading Score"]

size_passing_math = per_school_summary_df.groupby(["School Size"]).mean()["% Passing Math"]

size_passing_reading = per_school_summary_df.groupby(["School Size"]).mean()["% Passing Reading"]

size_overall_passing = per_school_summary_df.groupby(["School Size"]).mean()["% Overall Passing"]

size_summary_df = pd.DataFrame({
          "Average Math Score" : size_math_scores,
          "Average Reading Score": size_reading_scores,
          "% Passing Math": size_passing_math,
          "% Passing Reading": size_passing_reading,
          "% Overall Passing": size_overall_passing})

size_summary_df

# The scores by school type (3 pt)
type_math_scores = per_school_summary_df.groupby(["School Type"]).mean()["Average Math Score"]

type_reading_scores = per_school_summary_df.groupby(["School Type"]).mean()["Average Reading Score"]

type_passing_math = per_school_summary_df.groupby(["School Type"]).mean()["% Passing Math"]

type_passing_reading = per_school_summary_df.groupby(["School Type"]).mean()["% Passing Reading"]

type_overall_passing = per_school_summary_df.groupby(["School Type"]).mean()["% Overall Passing"]

type_summary_df = pd.DataFrame({
          "Average Math Score" : type_math_scores,
          "Average Reading Score": type_reading_scores,
          "% Passing Math": type_passing_math,
          "% Passing Reading": type_passing_reading,
          "% Overall Passing": type_overall_passing})

district_summary_df
#per_school_summary_df
#math_scores_by_grade
#reading_scores_by_grade
#budget_summary_df
#size_summary_df
#type_summary_df