# DS605: Fundamentals of Machine Learning

## Lab Assignment - 2

### Vectorized Programming with NumPy and Data Wrangling with Pandas

**Name:** Ummehani Khatri
**Student ID:** 202618029
**Course:** DS605 - Fundamentals of Machine Learning
**Lab:** Lab Assignment - 2
**Dataset:** Kaggle Titanic Dataset (`train.csv`)

---

## 1. Introduction

This project is part of **DS605: Fundamentals of Machine Learning - Lab Assignment 2**.

The objective of this lab is to practice:

* Vectorized programming using NumPy
* Array operations and linear algebra
* Probability distributions
* Data loading and inspection using Pandas
* Data filtering and querying
* Grouping and aggregation
* Missing-value handling
* Outlier detection
* Feature creation
* Pivot tables
* Data visualization
* Basic interpretation of data

The Titanic dataset is used for the Pandas data-wrangling portion of the assignment.

---

## 2. Dataset

The dataset used in this assignment is the **Titanic `train.csv` dataset**.

The dataset contains information about Titanic passengers, including:

* PassengerId
* Survived
* Pclass
* Name
* Sex
* Age
* SibSp
* Parch
* Ticket
* Fare
* Cabin
* Embarked

---

## 3. Technologies and Libraries

The project is implemented using Python and Jupyter Notebook.

### Libraries Used

* **NumPy** - Numerical computing and vectorized operations
* **Pandas** - Data manipulation and analysis
* **Matplotlib** - Data visualization
* **Seaborn** - Statistical visualization

---

## 4. Lab Tasks

### Part A - Vectorized Programming with NumPy

#### Task 1 - Arrays, Statistics, and Indexing

The following operations were performed:

* Generated a random NumPy array containing 100 integers
* Used a random seed for reproducibility
* Calculated minimum, maximum, median, mean, and standard deviation
* Created an array using `np.arange()`
* Implemented `np.zeros()` and `np.ones()`
* Implemented `np.linspace()`
* Created 2D and 3D arrays
* Demonstrated indexing, rows, columns, and slicing
* Used `reshape()` to create a matrix
* Used `flatten()` to convert the matrix back to one-dimensional form

#### Task 2 - Vectorized Arithmetic and Linear Algebra

The following operations were performed:

* Matrix addition
* Element-wise multiplication
* Matrix multiplication using `@`
* Matrix transpose
* Determinant calculation
* Matrix inverse
* Verification of the inverse using `np.allclose()`

#### Task 3 - Normal Distribution and Histogram

* Generated 1,000 values from a normal distribution
* Used a chosen mean and standard deviation
* Calculated the sample mean
* Calculated the sample standard deviation
* Compared sample statistics with the chosen values
* Created a histogram of the generated data

---

### Part B - Data Wrangling with Pandas

#### Task 4 - Load and Inspect Data

The Titanic dataset was loaded using Pandas.

The following functions and properties were used:

* `head()`
* `tail()`
* `shape`
* `columns`
* `info()`
* `describe()`
* `loc`
* `iloc`

#### Task 5 - Filtering and Querying

The following questions were answered using Boolean indexing and Pandas filtering:

* Number of male passengers older than 50
* Number of female first-class passengers
* Survival percentage of female first-class passengers
* Number of passengers aged 20-40 with fares above the overall median who survived
* Number of passengers travelling alone, younger than 30, who did not survive
* Number of passengers embarked at Southampton, travelling in Pclass 2 or 3, with fares above the Southampton median

#### Task 6 - GroupBy and Aggregation

The following analyses were performed:

* Survival rate by Sex
* Survival rate by Pclass
* Average Age and Fare by Pclass
* Passenger count and survival rate by Sex-Pclass
* Passenger count, average Fare, and survival rate by Embarked

#### Task 7 - Missing Values and Fare Outliers

The following operations were performed:

* Calculated missing-value counts for every column
* Calculated missing-value percentages
* Visualized missing values using a bar chart
* Filled missing Age values using mean imputation
* Compared missing Age values before and after imputation
* Tested mean, median, mode, and random-value imputation
* Calculated Q1 and Q3 for Fare
* Calculated IQR
* Calculated 1.5 × IQR lower and upper bounds
* Identified and counted Fare outliers

#### Task 8 - Features and Pivot Table

Two new features were created:

* `FamilySize = SibSp + Parch + 1`
* `IsAlone = 1` when `FamilySize = 1`, otherwise `0`

A pivot table was also created using:

* Rows: Sex
* Columns: Pclass
* Values: Mean Survived

The highest and lowest survival-rate groups were identified.

#### Task 9 - Visualizations and Observations

The following visualizations were created:

* Correlation heatmap
* Survival rate by Sex
* Age vs Fare categorized by survival status

The numerical results and visualizations were then used to identify key observations from the Titanic dataset.

---

## 5. Key Observations

1. Female passengers generally had a higher survival rate than male passengers.
2. Passenger class showed a noticeable relationship with survival, with higher-class passengers generally having better survival outcomes.
3. Fare showed a relationship with passenger class, as higher-class passengers generally paid higher fares.
4. The Fare variable contains high-value observations that can be identified as outliers using the IQR method.
5. Survival rates differed noticeably between male and female passengers.
6. Survival outcomes also varied across different passenger classes.
7. Family-related features such as `FamilySize` and `IsAlone` can be used to study differences in passenger survival.

> **Note:** The observations should be compared with the actual numerical results and plots generated from the dataset before final submission.

---

## 6. Project Structure

```text
202618029_DS605_Lab02/
│
├── train.csv
├── DS605_Lab02.ipynb
├── README.md
│
└── figures/
    ├── missing_values.png
    ├── correlation_heatmap.png
    ├── survival_by_sex.png
    └── age_vs_fare.png
```

---

## 7. How to Run

1. Download or clone this repository.
2. Make sure `train.csv` is in the same project folder as the notebook.
3. Open `DS605_Lab02.ipynb` using Jupyter Notebook or JupyterLab.
4. Run the notebook cells from top to bottom.
5. Make sure all outputs and visualizations are generated successfully.

---

## 8. Conclusion

This lab provided practical experience with NumPy and Pandas for numerical computation and data wrangling.

The NumPy section demonstrated vectorized operations, array manipulation, matrix operations, linear algebra, and normal-distribution analysis.

The Pandas section demonstrated how to inspect, filter, group, clean, transform, and visualize real-world Titanic passenger data.

Overall, the assignment helped develop fundamental skills required for machine learning and data analysis workflows using Python.

---

## 9. Submission

This repository contains the complete runnable code and supporting files required for **DS605 Lab Assignment - 2**.

**Student:** Ummehani Khatri
**Student ID:** 202618029

