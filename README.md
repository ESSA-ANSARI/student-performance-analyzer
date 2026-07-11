# ?? Student Performance Analysis

A complete **Data Analytics** project built using **Python, Pandas, Matplotlib, and Seaborn** to analyze student performance data.

This project demonstrates the complete data analysis workflow, including data cleaning, exploratory data analysis (EDA), visualization, correlation analysis, and exporting a cleaned dataset.

---

# ?? Project Overview

The objective of this project is to analyze student performance data and discover patterns that may influence exam scores.

The project covers:

- Data Loading
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Statistical Summary
- Data Visualization
- Correlation Analysis
- Exporting Cleaned Data

---

# ?? Dataset

The dataset contains information about students including:

- Study Hours
- Attendance
- Resources
- Extracurricular Activities
- Motivation
- Internet Access
- Gender
- Age
- Learning Style
- Online Courses
- Discussions
- Assignment Completion
- Exam Score
- Educational Technology Usage
- Stress Level
- Final Grade

---

# ?? Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn

---

# ?? Project Structure

```
student_performance_analyzer/
¦
+-- Data/
¦   +-- student_performance.csv
¦   +-- cleaned_students_data.csv
¦
+-- Images/
¦   +-- exam_score_distribution.png
¦   +-- studyhours_vs_examscore.png
¦   +-- gender_distribution_boxplot.png
¦   +-- correlation_heatmap.png
¦
+-- Notebooks/
¦
+-- student_analysis.py
¦
+-- README.md
```

---

# ?? Project Workflow

### 1. Data Loading

- Loaded the dataset using Pandas.

### 2. Data Cleaning

- Checked missing values.
- Removed duplicate records.
- Verified data types.
- Inspected dataset structure.

### 3. Exploratory Data Analysis (EDA)

Calculated:

- Average Exam Score
- Average Attendance
- Average Study Hours

Compared Exam Scores by:

- Gender
- Stress Level
- Learning Style

### 4. Data Visualization

Created visualizations including:

- Histogram of Exam Scores
- Scatter Plot of Study Hours vs Exam Score
- Box Plot of Exam Score by Gender
- Correlation Heatmap

### 5. Correlation Analysis

Analyzed relationships between numerical variables using a correlation matrix.

### 6. Export

Saved the cleaned dataset as:

```
cleaned_students_data.csv
```

---

# ?? Key Insights

- The dataset contained **1,534 duplicate records**, which were removed during data cleaning.
- No missing values were found.
- The average exam score was approximately **70.31**.
- The average attendance was approximately **80.24%**.
- Students studied an average of **20 hours**.
- Male and female students had very similar average exam scores.
- Stress level showed only a weak relationship with exam scores.
- Final Grade showed a strong negative correlation with Exam Score in this dataset, indicating the grading scale is likely encoded inversely.

---

# ?? Visualizations

### Exam Score Distribution

Shows how exam scores are distributed across all students.

---

### Study Hours vs Exam Score

Explores the relationship between study time and exam performance.

---

### Gender-wise Exam Score Distribution

Compares exam score distributions between genders.

---

### Correlation Heatmap

Displays relationships between all numerical features.

---

# ?? How to Run

Clone this repository:

```bash
git clone https://github.com/your-username/student_performance_analyzer.git
```

Install the required libraries:

```bash
pip install pandas matplotlib seaborn
```

Run the project:

```bash
python student_analysis.py
```

---

# ?? Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Visualization
- Correlation Analysis
- Python Programming
- Pandas
- Matplotlib
- Seaborn
- Data Interpretation

---

# ?? Future Improvements

Future versions of this project may include:

- Interactive Dashboard using Power BI
- SQL-based data analysis
- Machine Learning models for score prediction
- Streamlit web application
- Advanced statistical analysis

---

# ????? Author

**Essa Ansari**

B.Sc. Computer Science Student

Aspiring Data Scientist | Data Analyst | Machine Learning Enthusiast

GitHub: https://github.com/ESSA-ANSARI

LinkedIn: https://www.linkedin.com/in/essa-ansari-769443316/

---

? If you found this project useful, consider giving it a star!