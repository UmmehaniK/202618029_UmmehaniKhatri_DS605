# DS605 Lab Assignment 6
## Feature Extraction and Machine Learning with Image and Text Data

**Name:** Ummehani Khatri  
**Roll No.:** 202618029  
**Subject:** DS605 – Fundamentals of Machine Learning

---

## 1. Objective

The objective of this lab is to apply traditional machine learning techniques to image and text data by performing preprocessing, feature extraction, model training, and evaluation.

---

## 2. Datasets

### Image Dataset
**Asphalt Crack Dataset – 400 Images**

- Crack images: 200
- Non-crack images: 200
- Total images: 400

### Email Dataset
**Email Spam Classification Dataset – 5,172 Emails**

- Non-spam: 3672
- Spam: 1500
- Total emails: 5172

**Dataset Note:**  
The provided `emails.csv` contains 3000 pre-extracted numerical word-count features instead of raw email text. Therefore, the email classification task was performed using these existing numerical features.

---

# PART A – Image Feature Extraction

## 3. Image Preprocessing

The images were processed using OpenCV.

The following steps were performed:

1. Images were resized to 224 × 224.
2. Images were converted to grayscale.
3. Canny edge detection was applied.
4. Numerical features were extracted from each image.

## 4. Extracted Image Features

The following features were extracted:

- Mean brightness
- Contrast
- Dark-pixel ratio
- Bright-pixel ratio
- Edge density
- Crack/Non-crack label

The final feature table contains:

**400 rows × 6 columns**

The extracted features are saved in:

`image_features.csv`

A sample image and its Canny edge visualization are saved in:

`canny_visualization.png`

## 5. Image Classification Results

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Random Forest | 0.9500 | 0.9286 | 0.9750 | 0.9512 |
| Logistic Regression | 0.9125 | 0.8837 | 0.9500 | 0.9157 |

---

# PART B – Email Classification

## 6. Email Data Preprocessing

The email dataset contains 3000 numerical word-count features for each email.

The data was divided into:

- Training samples: 4137
- Testing samples: 1035
- Total features: 3000

The following traditional machine learning models were used:

- Random Forest
- Logistic Regression

## 7. Email Classification Results

| Model | Features | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|---:|
| Random Forest | 3000 | 0.9643 | 0.9340 | 0.9433 | 0.9386 |
| Logistic Regression | 3000 | 0.9826 | 0.9578 | 0.9833 | 0.9704 |

---

# PART C – Improved Representation

## 8. Feature Selection

Feature selection was used to reduce the number of input features from 3000 to 1000.

`SelectKBest` with the chi-square method was used before Logistic Regression.

## 9. Original vs Improved Representation

| Model | Features | Accuracy | Precision | Recall | F1 Score | Train Time | Predict Time |
|---|---:|---:|---:|---:|---:|---:|---:|
| Original Logistic Regression | 3000 | 0.9826 | 0.9578 | 0.9833 | 0.9704 | 13.9144 | 0.0752 |
| Improved Logistic Regression | 1000 | 0.9729 | 0.9474 | 0.9600 | 0.9536 | 12.9046 | 0.0440 |

The improved representation reduced the number of features from 3000 to 1000. It also reduced training and prediction time, with a small decrease in the evaluation metrics.

---

# 10. Project Workflow

```text
Raw Dataset
     ↓
Preprocessing
     ↓
Feature Extraction
     ↓
Train/Test Split
     ↓
Traditional ML Models
     ↓
Evaluation
     ↓
Feature Improvement
     ↓
Final Comparison
