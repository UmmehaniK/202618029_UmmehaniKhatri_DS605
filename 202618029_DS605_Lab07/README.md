# DS605 Lab Assignment 7: Image Representation, PCA, Eigenfaces and Face Recognition

## Overview

This project explores image representation, dimensionality reduction, eigenfaces, and face recognition using the **AT&T Database of Faces (ORL)**. It applies Principal Component Analysis (PCA) using NumPy linear algebra and compares similarity-based face recognition with traditional machine-learning classifiers.

## Objectives

* Represent grayscale face images as numerical feature vectors.
* Implement PCA using covariance eigendecomposition and Singular Value Decomposition (SVD).
* Visualize eigenfaces and cumulative explained variance.
* Reduce image dimensionality while retaining at least 90% of the variance.
* Reconstruct images from their reduced PCA representations.
* Perform face recognition using Euclidean distance.
* Compare raw-pixel matching, PCA-based matching, and traditional classifiers.
* Evaluate how the number of principal components affects recognition performance.

## Dataset

**Dataset:** AT&T Database of Faces (ORL)

* Total images: 400
* Total subjects: 40
* Images per subject: 10
* Image dimensions: 112 × 92 pixels
* Image type: Grayscale
* Original features per image: 10,304 pixels

Each image is converted into a grayscale pixel matrix and flattened into a one-dimensional feature vector.

## Methodology

### Part A: Image Representation

1. Load the grayscale face images.
2. Inspect image dimensions, data types, and pixel intensity values.
3. Flatten each image into a feature vector.
4. Create the complete feature matrix and corresponding subject labels.
5. Create a reproducible training and testing split, with 8 training images and 2 testing images per subject.

### Part B: PCA, Eigenfaces and Compression

1. Calculate the mean face using the training images.
2. Center the training and testing data using the training mean face.
3. Implement principal component extraction using covariance eigendecomposition and SVD with NumPy.
4. Compare the principal directions obtained through both approaches.
5. Calculate explained variance and determine the minimum number of components needed to retain at least 90% of the variance.
6. Visualize the principal components as eigenfaces.
7. Project the images into the reduced PCA space.
8. Reconstruct sample images and compare their appearance with the original images.
9. Compare the original and reduced feature representations.

### Part C: Recognition in PCA Space

1. Calculate Euclidean distances between test images and stored training images.
2. Identify the nearest training face for each test image.
3. Calculate recognition accuracy using raw pixel vectors.
4. Calculate recognition accuracy using PCA representations.
5. Inspect correct and incorrect matches visually.

### Part D: Traditional Machine Learning

The reduced PCA representations are used to train and evaluate:

* K-Nearest Neighbors (KNN)
* Support Vector Machine (SVM)
* Logistic Regression

The classifiers are compared with the similarity-based PCA matching baseline using accuracy, precision, recall, and F1-score.

Experiments with different numbers of principal components are also conducted to examine their effects on recognition accuracy and dimensionality reduction.

## Results

Replace the placeholders below with the actual results produced by the completed notebook.

| Metric                                             | Result               |
| -------------------------------------------------- | -------------------- |
| Original features per image                        | 10,304               |
| Training images                                    | 320                  |
| Testing images                                     | 80                   |
| PCA components for at least 90% explained variance | `[Enter value]`      |
| Explained variance retained                        | `[Enter percentage]` |
| Raw-pixel matching accuracy                        | `[Enter percentage]` |
| PCA matching accuracy                              | `[Enter percentage]` |
| KNN accuracy                                       | `[Enter percentage]` |
| SVM accuracy                                       | `[Enter percentage]` |
| Logistic Regression accuracy                       | `[Enter percentage]` |
| Best-performing model                              | `[Enter model name]` |

### Observations

Discuss the observations supported by your experimental results:

* Compare the principal directions obtained through covariance eigendecomposition and SVD.
* Explain how PCA reduces the number of features required to represent each face.
* Describe the visual differences between original and reconstructed images.
* Compare recognition accuracy using raw pixels and PCA representations.
* Identify which traditional classifier performs best on the test set.
* Explain how changing the number of principal components affects recognition accuracy and compactness.

## Repository Structure

```text
DS605_Lab07/
├── DS605_Lab07.ipynb
├── README.md
├── figures/
│   ├── explained_variance.png
│   ├── eigenfaces.png
│   ├── reconstruction_examples.png
│   ├── part_c_matching_accuracy.png
│   ├── part_d_model_comparison.png
│   └── component_count_experiment.png
└── results/
    ├── part_c_recognition_results.csv
    ├── part_d_model_comparison.csv
    ├── component_count_experiment.csv
    └── project_summary.csv
```

*The repository structure should reflect the files actually included in the final repository.*

## Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Pillow
* Scikit-learn for the final traditional-machine-learning comparison

PCA and eigenface calculations are implemented using NumPy linear-algebra operations rather than Scikit-learn's PCA implementation.

## How to Run

1. Clone or download this repository.
2. Download the AT&T Database of Faces (ORL) and place its subject folders inside the `att_faces/` directory.
3. Install the required Python libraries.
4. Open `DS605_Lab07.ipynb` in Jupyter Notebook.
5. Run the notebook cells in order.

Install the dependencies using:

```bash
pip install numpy pandas matplotlib Pillow scikit-learn notebook
```

## Conclusion

This project demonstrates how grayscale images can be represented numerically and transformed into a lower-dimensional feature space using PCA. Eigenfaces provide a visual interpretation of the principal directions of variation in face images. Similarity-based matching and traditional classifiers are evaluated to understand their face-recognition performance.

The final conclusions are based on the measured results, reconstruction examples, and component-count experiments produced by the notebook.

## Course Information

* **Course:** DS605 — Fundamentals of Machine Learning
* **Assignment:** Lab Assignment 7
* **Topic:** Image Representation, PCA, Eigenfaces and Face Recognition
* **Dataset:** AT&T Database of Faces (ORL)
