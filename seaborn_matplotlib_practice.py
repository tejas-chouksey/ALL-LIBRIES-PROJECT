# CSV + PANDAS + MATPLOTLIB + SEABORN PRACTICE
# Dataset: student_practice_dataset.csv
# Solve each question below.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# TOPIC 1: CSV & PANDAS
# =========================

# Q1. Load the CSV file using Pandas.

df = pd.read_csv("student_practice_dataset.csv")
df = pd.read_csv("student_practice_dataset.csv", parse_dates=["enrollment_date"])

# Q2. Display the first 10 rows.

print(df.head(10))

# Q3. Display the last 5 rows.

print(df.tail(5))

# Q4. Display 10 random rows.

print(df.sample(10))

# Q5. Find the number of rows and columns.

print(df.shape)

# Q6. Print all column names as a list.
print(df.columns.tolist())

# Q7. Print the data type of each column.

print(df.dtypes)

# Q8. Run df.info().

print(df.info())

# Q9. Display the statistical summary of numerical columns.

print(df.describe())

# Q10. Find missing values in every column.

print(df.isnull().sum())

# =========================
# TOPIC 2: DATA ANALYSIS
# =========================

# Q11. Find the average age.

print(df["age"].mean())

# Q12. Find the minimum and maximum age.

print(df["age"].min())
print(df["age"].max())

# Q13. Find the average attendance percentage.

print(df["attendance_pct"].mean())

# Q14. Find the highest Python marks.

print(df["marks_python"].max())

# Q15. Find the lowest Math marks.

print(df["marks_math"].min())

# Q16. Find the average marks of all five subjects.

print(df[["marks_python" , "marks_math" , "marks_ml" , "marks_dbms"]].mean().mean())

# Q17. Find the total fees paid.

print(df["fees_paid"].sum())

# Q18. Find the total fees due.

print(df["fees_due"].sum())
# Q19. Count students in each gender.

print(df["gender"].value_counts())

# Q20. Count students in each city.

print(df["city"].value_counts())

# =========================
# TOPIC 3: FILTERING
# =========================

# Q21. Display students whose age is greater than 20.

print(df["age"] > 20)

# Q22. Display students whose attendance is greater than 75.

print(df["attendance_pct"] > 75)

# Q23. Display students whose Python marks are greater than 80.

print(df[df["marks_python"] > 80])

# Q24. Display students whose Math marks are less than 50.

print(df[df["marks_math"] < 50])

# Q25. Display students belonging to the B.Tech course.

print(df[df["course"] == "B.tech"])

# Q26. Display students belonging to the CSE department.

print(df[["department", "course"]].dtypes)

print(df[df["department"] == "CSE"])

# Q27. Display students from Indore.



# Q28. Display students whose fees_due is greater than 50000.

# Q29. Display students with attendance > 75 AND Python marks > 75.

# Q30. Display students with Math marks > 80 OR Python marks > 80.


# =========================
# TOPIC 4: MATPLOTLIB
# =========================

# Q31. Create a bar chart showing students in each gender.

df["gender"].value_counts().plot( kind = "bar")
plt.show()

# Q32. Create a bar chart showing students in each course.

df["course"].value_counts().plot(kind = "bar")
plt.show()

# Q33. Create a bar chart showing students in each city.

df["city"].value_counts().plot(kind = "bar")
plt.show()

# Q34. Create a pie chart showing students by gender.

df["gender"].value_counts().plot(kind = "pie")
plt.show()

# Q35. Create a histogram of age.

df["age"].plot(kind = "hist")
plt.show()

# Q36. Create a histogram of attendance_pct.

df["attendance_pct"].plot(kind = "hist")
plt.show()

# Q37. Create a histogram of marks_python.

# Q38. Create a line chart showing average marks of all five subjects.

df[["marks_python", "marks_math", "marks_stats", "marks_dbms", "marks_ml"]].mean().plot(kind = "line")
plt.show()

# Q39. Create a scatter plot between attendance_pct and marks_python.

df.plot(kind = "scatter" , x = "attendance_pct" , y = "marks_python")
plt.show()

# Q40. Add a title, x-axis label and y-axis label.



# =========================
# TOPIC 5: SEABORN
# =========================

# Q41. Create a Seaborn countplot for gender.

sns.countplot(data = df , x = "gender")
plt.show()

# Q42. Create a Seaborn countplot for course.

sns.countplot(data = df , x = "course")
plt.show()

# Q43. Create a Seaborn countplot for department.



# Q44. Create a Seaborn histplot for age.

sns.histplot(data = df , x = "age")
plt.show()

# Q45. Create a Seaborn histplot for marks_python.

# Q46. Create a Seaborn boxplot for marks_math.

# Q47. Create a Seaborn boxplot for attendance_pct.

# Q48. Create a boxplot comparing Python marks for different genders.

sns.boxplot(data = df , x = "gender" , y = "marks_python")
plt.show()

# Q49. Create a scatterplot between attendance_pct and marks_python.

sns.scatterplot(data = df , x = "attendance_pct" , y = "marks_python")
plt.show()

# Q50. Add hue="gender" to the scatterplot.

sns.scatterplot(
    data=df,
    x="attendance_pct",
    y="marks_python",
    hue="gender"
)

plt.show()


# =========================
# TOPIC 6: ADVANCED SEABORN
# =========================

# Q51. Create a correlation matrix using numerical columns.

# Q52. Display the correlation matrix using a heatmap.

# Q53. Use annot=True in the heatmap.

# Q54. Create a heatmap for the five subject marks.

# Q55. Create a barplot showing average Python marks for each course.

# Q56. Create a barplot showing average attendance for each department.

# Q57. Create a boxplot comparing Python marks across courses.

# Q58. Create a boxplot comparing ML marks across departments.

# Q59. Create a scatterplot between fees_paid and fees_due.

# Q60. Create a scatterplot between attendance_pct and marks_ml using hue="gender".


# =========================
# TOPIC 7: DATA CLEANING
# =========================

# Q61. Find missing values in marks_math.

# Q62. Find missing values in marks_python.

# Q63. Fill missing marks_math values using the mean.

# Q64. Fill missing marks_python values using the median.

# Q65. Check missing values again.

# Q66. Find duplicate rows.

# Q67. Remove duplicate rows.

# Q68. Convert enrollment_date into datetime.

# Q69. Extract the year from enrollment_date.

# Q70. Sort the dataset by marks_python in descending order.


# =========================
# TOPIC 8: FINAL ANALYSIS
# =========================

# Q71. Find the top 10 students by Python marks.

# Q72. Find the top 10 students by attendance.

# Q73. Find the 10 students with the highest fees_due.

# Q74. Find average marks for each department.

# Q75. Find average attendance for each course.

# Q76. Find students in each city and visualize the result.

# Q77. Find average Python marks for each gender and visualize it.

# Q78. Find students with attendance > 80 AND Python marks > 80.

# Q79. Find correlation between attendance and all five subject marks.

# Q80. Create a final analysis using 3 different charts.
