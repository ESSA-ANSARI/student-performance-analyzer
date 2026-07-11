"""
Student Performance Analysis

Author: Essa Ansari

Description:
This project performs data cleaning,
exploratory data analysis (EDA),
visualization,and correlation analysis
on a student performance dataset.

"""
#===================
#Import Libraries
#===================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#==================
#Data Loading
#==================
df = pd.read_csv("Data/student_performance.csv")

#==================
#Viewing Data
#==================
print("\nFrist 5 Rows")
print(df.head())

print("\nDataset Statistics")
print(df.describe())

print("\nDataset Information")
df.info()

#==================
#Cleaning Data
#==================
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Values:")
print(df.duplicated().sum())

print("Shape Before Cleaning:", df.shape)

df = df.drop_duplicates()

print("Shape After Cleaning:", df.shape)

df.info()

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

#=================
#EDA
#=================
print("\nAverage Exam Score:", df["ExamScore"].mean().round(2))
print("\nAverage Attendence:", df["Attendance"].mean().round(2))
print("\nAverage Study Hours:", df["StudyHours"].mean().round(2))

print("\nAverage Exam Score by Gender")
print(df.groupby("Gender")["ExamScore"].mean().round(2))

print("\nAverage Exam Score by Stresslevel")
print(df.groupby("StressLevel")["ExamScore"].mean().round(2))

print("\nAverage Exam Score by Learning Style")
print(df.groupby("LearningStyle")["ExamScore"].mean().round(2))

#=====================
#Data Visualization
#=====================
plt.figure(figsize=(8,5))

plt.hist(
    df["ExamScore"],
    bins=15,
    edgecolor="black"
    )

plt.title("Exam Score Distribution")
plt.xlabel("Exam Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("Images/exam_score_distribution.png")
plt.show()

plt.figure(figsize=(8,5))

plt.scatter(
    df["StudyHours"],
    df["ExamScore"],
    alpha=0.5
)

plt.xlabel("StudyHours")
plt.ylabel("ExamScore")
plt.title("Study Hours v/s Exam Score")
plt.tight_layout()
plt.savefig("Images/studyhours_vs_examscore.png")
plt.show()

plt.figure(figsize=(6,5))

sns.boxplot(
    x="Gender",
    y="ExamScore",
    data=df
)
plt.title("Exam Score Distribution by Gender")
plt.tight_layout()
plt.savefig("Images/gender_distribution_boxplot.png")
plt.show()

#=======================
#Correlation Analysis
#=======================
corr = df.corr()
print("\nCorrelation Analysis:", corr)

plt.figure(figsize=(12, 8))

sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)

plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("Images/correlation_heatmap.png")
plt.show()

df.to_csv("Data/cleaned_students_data.csv", index=False)
print("\nAnalysis Completed Successfully!")
print("Cleaned dataset saved in Data/")
print("Visualizations saved in Images/")

print("\nINSIGHTS")
print("- Average exam score is 70.31.")
print("- Dataset contains no missing values.")
print("- 1,534 duplicate rows were removed.")
print("- Male and Female average scores are nearly identical.")
print("- Stress Level has very weak correlation with Exam Score.")
print("- Final Grade is strongly negatively correlated with Exam Score.")