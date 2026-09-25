# DS605 Lab 5 — Machine Learning with Scikit-learn and From Scratch

**Name:** Ummehani Khatri
**Roll No:** 202618029
**Course:** DS605 — Fundamentals of Machine Learning

## 1. Objective

This lab implements Machine Learning models using the **UCI Productivity Prediction of Garment Employees** dataset.

The assignment has three main parts:

* Implement Regression and Classification using Scikit-learn.
* Implement the same models from scratch using only NumPy and Pandas.
* Compare the implementations and optimize the manual Logistic Regression model.

## 2. Dataset

**Dataset:** Productivity Prediction of Garment Employees

The dataset contains information related to garment production, including:

* Team
* Targeted productivity
* SMV
* WIP
* Over time
* Incentive
* Idle time
* Idle men
* Number of style changes
* Number of workers
* Date
* Quarter
* Department
* Day

### Target Variables

**Regression:**

`actual_productivity`

**Classification:**

A new `MeetsTarget` column was created:

```text
MeetsTarget = 1  if actual_productivity >= targeted_productivity
MeetsTarget = 0  otherwise
```

`actual_productivity` was not used as an input feature for classification.

## 3. Dataset Preprocessing

The dataset contained missing values in the `wip` column.

Missing `wip` values were replaced using the median:

```python
df["wip"] = df["wip"].fillna(df["wip"].median())
```

Categorical features were converted using one-hot encoding.

Numerical features were standardized using the training-set mean and standard deviation.

The same train-test split was used for all implementations:

* Training samples: **957**
* Testing samples: **240**
* Test size: **20%**
* Random state: **42**

## 4. Part A — Scikit-learn Implementation

### Linear Regression

Scikit-learn `LinearRegression` was used to predict `actual_productivity`.

Results:

| Metric          |      Value |
| --------------- | ---------: |
| MAE             |   0.112096 |
| RMSE            |   0.150645 |
| R²              |   0.145317 |
| Training Time   | 0.010311 s |
| Prediction Time | 0.000297 s |

### Logistic Regression

Scikit-learn `LogisticRegression` was used to predict `MeetsTarget`.

Results:

| Metric          |      Value |
| --------------- | ---------: |
| Accuracy        |   0.758333 |
| Precision       |   0.776744 |
| Recall          |   0.943503 |
| F1-score        |   0.852041 |
| Training Time   | 0.030429 s |
| Prediction Time | 0.000397 s |

## 5. Part B — Models From Scratch

The manual implementations use only **NumPy and Pandas** for Machine Learning operations.

### Manual Linear Regression

Linear Regression was implemented using the normal equation with NumPy matrix operations.

Results:

| Metric          |      Value |
| --------------- | ---------: |
| MAE             |   0.112096 |
| RMSE            |   0.150645 |
| R²              |   0.145317 |
| Training Time   | 0.013178 s |
| Prediction Time | 0.000036 s |

The results are almost identical to the Scikit-learn implementation.

### Manual Logistic Regression

Logistic Regression was implemented using:

* Sigmoid function
* Gradient descent
* Vectorized NumPy operations
* 0.5 classification threshold
* Manually calculated evaluation metrics

Results:

| Metric          |      Value |
| --------------- | ---------: |
| Accuracy        |   0.750000 |
| Precision       |   0.757709 |
| Recall          |   0.971751 |
| F1-score        |   0.851485 |
| Training Time   | 0.122072 s |
| Prediction Time | 0.000104 s |

## 6. Part C — Optimization

The manual Logistic Regression implementation was optimized by changing the gradient-descent configuration.

The optimized version used:

* Learning rate: `0.05`
* Epochs: `2000`
* Vectorized NumPy calculations

### Optimized Manual Logistic Regression

| Metric          |      Value |
| --------------- | ---------: |
| Accuracy        |   0.762500 |
| Precision       |   0.772727 |
| Recall          |   0.960452 |
| F1-score        |   0.856423 |
| Training Time   | 0.056200 s |
| Prediction Time | 0.000078 s |

Compared with the basic manual implementation:

* Accuracy increased from **0.750000 to 0.762500**
* F1-score increased from **0.851485 to 0.856423**
* Training time decreased from **0.122072 s to 0.056200 s**

## 7. Final Comparison

| Model                                |      MAE |     RMSE |       R² | Accuracy | Precision |   Recall |       F1 | Train Time | Prediction Time |
| ------------------------------------ | -------: | -------: | -------: | -------: | --------: | -------: | -------: | ---------: | --------------: |
| Sklearn Linear Regression            | 0.112096 | 0.150645 | 0.145317 |        - |         - |        - |        - |   0.010311 |        0.000297 |
| Manual Linear Regression             | 0.112096 | 0.150645 | 0.145317 |        - |         - |        - |        - |   0.013178 |        0.000036 |
| Sklearn Logistic Regression          |        - |        - |        - | 0.758333 |  0.776744 | 0.943503 | 0.852041 |   0.030429 |        0.000397 |
| Manual Logistic Regression           |        - |        - |        - | 0.750000 |  0.757709 | 0.971751 | 0.851485 |   0.122072 |        0.000104 |
| Optimized Manual Logistic Regression |        - |        - |        - | 0.762500 |  0.772727 | 0.960452 | 0.856423 |   0.056200 |        0.000078 |

## 8. Implementation Comparison

### Linear Regression

The manual Linear Regression produced almost exactly the same results as Scikit-learn.

This shows that the NumPy implementation correctly reproduced the main Linear Regression calculation.

### Logistic Regression

The manual Logistic Regression produced slightly different results from Scikit-learn because the model was trained using a manually implemented gradient-descent procedure.

The optimized version improved the classification results while also reducing training time compared with the basic manual implementation.

## 9. Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Jupyter Notebook
* UCI Machine Learning Repository

## 10. Repository Files

Recommended repository structure:

```text
DS605-Lab05/
│
├── DS605_Lab05.ipynb
├── model_comparison.csv
└── README.md
```

## 11. Conclusion

This lab demonstrated the complete Machine Learning workflow:

```text
Raw Dataset
     ↓
Data Preprocessing
     ↓
Train-Test Split
     ↓
Model Training
     ↓
Prediction
     ↓
Evaluation
     ↓
Scikit-learn vs From Scratch
     ↓
Optimization
```

Linear Regression was successfully implemented using both Scikit-learn and NumPy. Logistic Regression was also implemented manually using gradient descent, followed by an optimized version.

The experiment demonstrates how Machine Learning libraries simplify implementation while manual NumPy implementations provide an understanding of the underlying mathematical operations.
