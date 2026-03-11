# Student-Performance-Statistical-Analysis-Python-
# Project Overview

This project focuses on analyzing student performance data using statistical methods in Python. The goal of this analysis is to understand how different factors such as gender, parental education, study habits, and other variables influence student academic performance.

Using Python libraries, the dataset was explored, cleaned, and analyzed to extract meaningful insights about student scores in subjects like Math, Science, and English.
# Objectives

Perform statistical analysis on student academic performance

Identify patterns and trends in student scores

Compare performance across different categories (gender, study habits, etc.)

Calculate statistical measures such as mean, distribution, and group comparisons
Analysis Performed

# The following statistical analysis was performed in this project:

Data inspection using df.head() and df.info()

Checking dataset structure and data types

Calculating average scores for different subjects

Comparing performance by gender

Grouping data to identify trends

Basic statistical summaries of student scores

Example operations used in the analysis:

df.head()
df.info()
df[['math_score','science_score','english_score']].mean()
df.groupby('gender')['math_score'].mean()

# Key Insights

Average scores across different subjects were calculated.

Performance comparison between male and female students was analyzed.

Patterns in student performance were identified using grouping and statistical summaries.

The analysis helps understand how different factors influence academic results.
