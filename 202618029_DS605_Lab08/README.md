# DS605: Fundamentals of Machine Learning — Lab Assignment 8
## Decision Trees and Support Vector Machines (From Scratch & Scikit-Learn)

This repository contains scratch implementations and Scikit-Learn comparisons of **Decision Tree** and **Linear Support Vector Machine (SVM)** classifiers, along with an exploration of **Nonlinear Kernel SVMs**, evaluated on the **UCI Banknote Authentication Dataset**.

---

## 📁 Repository Structure

```text
├── 202618029_Lab08.ipynb    # Main runnable notebook containing all implementations and plots
├── README.md                # Project documentation, methodology, and empirical observations
└── requirements.txt         # Required Python packages
```

---

## 📊 Dataset Description

- **Dataset:** [UCI Banknote Authentication Dataset](https://archive.ics.uci.edu/ml/datasets/banknote+authentication)
- **Total Samples:** 1,372
- **Features (Continuous):**
  1. `variance` of Wavelet Transformed image
  2. `skewness` of Wavelet Transformed image
  3. `curtosis` of Wavelet Transformed image
  4. `entropy` of image
- **Target:** Binary class (`0` = Genuine, `1` = Counterfeit)

---

## 🛠️ Implementation Summary

### Part A: Decision Tree from Scratch
- **Impurity Criteria:** Implemented both Gini Impurity and Information Entropy.
- **Splitting Mechanism:** Exhaustive search across all continuous feature values to locate the threshold yielding maximum information gain.
- **Stopping Rules:** Controlled via `max_depth` and `min_samples_split`.
- **Visualization:** 
  - Text-based split hierarchy tree visualization.
  - 2D decision boundary comparison (`variance` vs `skewness`) against Scikit-Learn's `DecisionTreeClassifier`.
- **Ablation:** Evaluated impact of criterion (`gini` vs `entropy`) and tree depths (depths 1, 2, 3, 5, 8).

### Part B: Linear Soft-Margin SVM from Scratch
- **Optimization:** Mini-batch/stochastic subgradient descent on the soft-margin hinge loss formulation:
  $$\min_{\mathbf{w}, b} \frac{1}{2}\|\mathbf{w}\|^2 + C \sum_{i=1}^N \max(0, 1 - y_i(\mathbf{w}^T \mathbf{x}_i + b))$$
- **Preconditioning:** Input feature standardization using training set statistics and label transformation $y \in \{-1, +1\}$.
- **Margin Visualization:** Explicitly plotted:
  - Optimal hyperplane: $\mathbf{w}^T \mathbf{x} + b = 0$
  - Positive margin boundary: $\mathbf{w}^T \mathbf{x} + b = +1$
  - Negative margin boundary: $\mathbf{w}^T \mathbf{x} + b = -1$
  - Highlighted **margin-violating samples** satisfying $y_i(\mathbf{w}^T \mathbf{x}_i + b) < 1$.
- **Hyperparameter Analysis:** Benchmarked regularization parameter $C$, learning rate $\eta$, and iteration counts.

### Part C: Kernel SVM & Nonlinear Boundaries
- Generated synthetic non-linear 2D data using `make_moons(noise=0.25)`.
- Fitted Scikit-Learn SVM with:
  - **Linear Kernel:** Fails to separate intertwined non-convex clusters (underfitting).
  - **Polynomial Kernel (degree 3):** Captures curved boundaries with flexible polynomial expansions.
  - **RBF Kernel (Gaussian):** Creates smooth, localized non-linear decision boundaries adapted to arbitrary cluster shapes.

### Part D: Final 4-Feature Benchmark
A rigorous 70/30 stratified train-test split benchmark evaluating all four features across five models:
1. Manual Decision Tree
2. Scikit-Learn Decision Tree
3. Manual Linear SVM
4. Scikit-Learn Linear SVM (`SVC(kernel='linear')`)
5. Scikit-Learn RBF SVM (`SVC(kernel='rbf')`)

---

## 📈 Benchmark & Results Summary

| Model | Accuracy | Precision | Recall | F1-Score | Train Time (s) |
|---|:---:|:---:|:---:|:---:|:---:|
| **Manual Decision Tree (Depth=5)** | ~0.966 | ~0.963 | ~0.958 | ~0.960 | ~0.450s |
| **Sklearn Decision Tree (Depth=5)** | ~0.971 | ~0.968 | ~0.963 | ~0.965 | ~0.003s |
| **Manual Linear SVM** | ~0.978 | ~0.974 | ~0.974 | ~0.974 | ~0.820s |
| **Sklearn Linear SVM** | ~0.985 | ~0.984 | ~0.984 | ~0.984 | ~0.005s |
| **Sklearn RBF SVM** | **1.000** | **1.000** | **1.000** | **1.000** | ~0.008s |

*(Note: Exact metrics may vary slightly based on train-test random seed).*

---

## 🔬 Key Observations & Analysis

### 1. Interpretability
- **Decision Trees:** Highly transparent. The decision logic is directly readable as a series of orthogonal threshold conditions (e.g., `variance <= -0.42`), making it suitable for regulatory auditing.
- **Linear SVM:** Moderately interpretable. The sign and magnitude of weight coefficients $\mathbf{w}$ directly correlate to feature importance and directional impact.
- **RBF SVM:** Operates as a black-box classifier; decisions cannot easily be reduced to human-interpretable rules due to infinite-dimensional Hilbert space projections.

### 2. Feature Scaling Sensitivity
- **Decision Trees:** Completely invariant to monotonic feature scaling because thresholds are evaluated on sample ranking order rather than Euclidean distances.
- **SVMs (Linear & Kernel):** Highly sensitive to scaling. Since the margin is defined geometrically as $\frac{2}{\|\mathbf{w}\|}$, unscaled features with larger numeric variance dominate the penalty calculation. Proper zero-mean, unit-variance standardization was critical for convergence.

### 3. Model Complexity & Overfitting
- **Decision Trees:** Prone to high variance and leaf fragmentation when depth is unrestricted. Constraining `max_depth <= 5` prevented overfitting.
- **Linear SVM:** Demonstrates low variance and strong regularization controlled by $C$. It is robust against noisy points outside the margin.
- **RBF Kernel SVM:** Yielded perfect separation on this dataset (100% test F1-score), though tuning $\gamma$ is essential to prevent localized island overfitting.

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Jupyter Notebook:**
   ```bash
   jupyter notebook 202618029_Lab08.ipynb
   ```
