# DS605 - Online Shoppers Purchasing Intention Classification Challenge

## Student Information

**Name:** Ummehani Khatri  
**Roll Number:** 202618029  
**Course:** MSc Data Science  
**Subject:** DS605 - Machine Learning / Data Science  
**Challenge:** Online Shoppers Purchasing Intention Classification Challenge  

---

## Project Description

This project is completed as part of the DS605 Online Shoppers Purchasing Intention Classification Challenge.

The objective of this challenge is to predict whether an online shopping session results in a purchase. The target variable used for classification is `Revenue`.

The competition requires the use of **Logistic Regression** as the classification algorithm.

---

## Dataset

The competition provides two datasets:

- `train.csv` - Contains the training data and the `Revenue` target variable.
- `test.csv` - Contains the test data and `Session_ID`.

The test target values are hidden.

---

## Data Preprocessing

The following preprocessing steps were performed:

1. Loaded the training and test datasets.
2. Inspected the dataset and missing values.
3. Separated the `Revenue` target variable.
4. Removed `Session_ID` from the model features.
5. Handled missing numerical values using the median.
6. Handled missing categorical values using the mode.
7. Converted categorical variables using one-hot encoding.
8. Scaled the features using `StandardScaler`.
9. Created additional useful features from the available dataset.

No external datasets were used.

---

## Feature Engineering

Additional features were created to improve the Logistic Regression model, including:

- Total Pages
- Total Duration
- Log-transformed numerical features
- Pages-per-minute features
- Difference between Bounce Rates and Exit Rates

These features were created only from the provided competition dataset.

---

## Machine Learning Model

The required classification algorithm for this challenge is:

**Logistic Regression**

The model was implemented using:

```python
from sklearn.linear_model import LogisticRegression
