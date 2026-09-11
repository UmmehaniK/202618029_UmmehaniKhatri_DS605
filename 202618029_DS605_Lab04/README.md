# DS605 Lab 04 -- End-to-End Airbnb Price Prediction

## Student Information

**Name:** Ummehani Khatri\
**Student ID:** 202618029\
**Course:** DS605 -- Fundamentals of Machine Learning\
**Lab:** Lab Assignment 04

------------------------------------------------------------------------

## Project Title

**Airbnb Price Prediction using Machine Learning**

This project develops an end-to-end machine learning system to estimate
the nightly price of an Airbnb listing in New York City. The project
covers data analysis, data cleaning, preprocessing, feature selection,
regression model comparison, hyperparameter tuning, model evaluation,
model saving, and deployment through a Streamlit web application.

------------------------------------------------------------------------

## Dataset

The project uses the **New York City Airbnb Open Data** dataset
(`AB_NYC_2019.csv`).

The original dataset contains:

-   **48,895 listings**
-   **16 columns**
-   Airbnb listing information from New York City

The target variable for prediction is:

**`price`** -- the nightly price of the Airbnb listing.

------------------------------------------------------------------------

## Project Objectives

The main objectives of this project are:

1.  Analyze the Airbnb dataset.
2.  Handle missing values and unnecessary columns.
3.  Detect and remove extreme price outliers.
4.  Select meaningful features for machine learning.
5.  Apply suitable preprocessing techniques.
6.  Compare multiple regression models.
7.  Tune the Random Forest model using hyperparameter search.
8.  Evaluate models using MAE, RMSE, and R².
9.  Save the final trained model and preprocessing workflow.
10. Build a Streamlit application for interactive price prediction.

------------------------------------------------------------------------

# 1. Data Cleaning and Preprocessing

Several preprocessing steps were performed before model training.

### Missing Values

The dataset contained missing values in columns such as:

-   `last_review`
-   `reviews_per_month`
-   `host_name`
-   `name`

The following decisions were made:

-   Missing `reviews_per_month` values were replaced with **0**.
-   Missing `name` values were replaced with **"Unknown"**.
-   Missing `host_name` values were replaced with **"Unknown"**.
-   `last_review` was removed because it was not selected as a model
    feature.

### Unnecessary Columns

The following columns were removed:

-   `id`
-   `host_id`
-   `last_review`
-   `name`
-   `host_name`

The IDs were not useful for predicting price, while name and host-name
information was not used in the final model.

### Zero Prices

Listings with:

``` text
price = 0
```

were removed because zero does not represent a valid nightly Airbnb
price.

### Outlier Treatment

The IQR method was used to identify extreme price values.

The calculated values were:

-   Q1 = **69**
-   Q3 = **175**
-   IQR = **106**
-   Upper bound = **334**

A total of **2,972 outlier listings** were removed.

After cleaning and outlier treatment, the final dataset contained:

**45,912 listings**

------------------------------------------------------------------------

# 2. Features Used for Prediction

The final model uses 10 features:

    No. Feature
  ----- ----------------------------------
      1 `neighbourhood_group`
      2 `neighbourhood`
      3 `latitude`
      4 `longitude`
      5 `room_type`
      6 `minimum_nights`
      7 `number_of_reviews`
      8 `reviews_per_month`
      9 `calculated_host_listings_count`
     10 `availability_365`

### Target Variable

``` text
price
```

------------------------------------------------------------------------

# 3. Data Preprocessing

The dataset contains both categorical and numerical features.

### Categorical Features

The following features were encoded using **OneHotEncoder**:

-   `neighbourhood_group`
-   `neighbourhood`
-   `room_type`

`handle_unknown="ignore"` was used so that the application can handle
unseen categorical values without failing during transformation.

### Numerical Features

The following numerical features were standardized using
**StandardScaler**:

-   `latitude`
-   `longitude`
-   `minimum_nights`
-   `number_of_reviews`
-   `reviews_per_month`
-   `calculated_host_listings_count`
-   `availability_365`

The preprocessing workflow was fitted on the training data and then
applied to the test data.

------------------------------------------------------------------------

# 4. Train-Test Split

The cleaned data was divided into training and testing sets using:

-   **80% Training Data**
-   **20% Testing Data**
-   `random_state = 42`

This allowed the final model to be evaluated on data that was not used
during training.

------------------------------------------------------------------------

# 5. Machine Learning Models

Three main regression approaches were compared:

### 1. Linear Regression

A basic linear regression model was used as a baseline.

### 2. Ridge Regression

Ridge Regression was tested to introduce regularization and reduce the
effect of potential multicollinearity.

### 3. Random Forest Regressor

Random Forest was used because it can model nonlinear relationships
between listing characteristics and price.

The initial Random Forest configuration included:

``` text
n_estimators = 50
max_depth = 20
min_samples_leaf = 2
random_state = 42
n_jobs = -1
```

------------------------------------------------------------------------

# 6. Model Comparison

The evaluated models produced the following test-set results:

  Model                          MAE            RMSE       R² Score
  --------------------- ------------ --------------- --------------
  Linear Regression           34.076       46.426675       0.523986
  Ridge Regression            34.047       46.398330       0.524567
  Random Forest           **31.539**   **43.886839**   **0.574643**
  Tuned Random Forest            ---       44.727040       0.558201

The **Random Forest Regressor** achieved the best test-set performance
among the evaluated models.

It had:

-   The lowest RMSE
-   The lowest reported MAE
-   The highest R² score

Therefore, the original Random Forest model was selected as the final
model.

------------------------------------------------------------------------

# 7. Final Model Performance

### Final Model

**Random Forest Regressor**

### Test Performance

``` text
MAE      : 31.539
RMSE     : 43.886839
R² Score : 0.574643
```

The R² score of approximately **0.575** indicates that the model
explains a substantial portion of the variation in Airbnb prices, while
other factors not included in the dataset still contribute to price
differences.

------------------------------------------------------------------------

# 8. Hyperparameter Tuning

RandomizedSearchCV was used to search for improved Random Forest
hyperparameters.

The tuning process used:

-   **3-fold cross-validation**
-   **5 candidate parameter combinations**

The tuned model achieved a test RMSE of:

``` text
44.727040
```

and an R² score of:

``` text
0.558201
```

Since the tuned model did not improve the test performance compared with
the original Random Forest, the original Random Forest was retained as
the final model.

------------------------------------------------------------------------

# 9. Model Evaluation Visualizations

The project includes visual analysis such as:

-   Price distribution before cleaning
-   Price distribution after cleaning
-   Price boxplot
-   Actual vs Predicted price plot
-   Residual analysis
-   Feature importance
-   Model comparison charts

The main saved visualization is:

``` text
actual_vs_predicted.png
```

This visualization compares the actual Airbnb prices from the test set
with the prices predicted by the final Random Forest model.

------------------------------------------------------------------------

# 10. Saved Model Files

The trained model and preprocessing workflow were saved using `joblib`.

### Model

``` text
airbnb_price_model.pkl
```

### Preprocessor

``` text
airbnb_preprocessor.pkl
```

These files allow the trained machine learning system to be reused
without retraining the model every time the Streamlit application
starts.

------------------------------------------------------------------------

# 11. Streamlit Application

A Streamlit web application was developed to provide an interactive
interface for Airbnb price prediction.

The application contains three main sections:

### 🏠 Home

Provides:

-   Project introduction
-   Dataset information
-   Project statistics
-   Final model performance
-   Navigation to other sections

### 💰 Price Prediction

The user can enter:

-   Neighbourhood Group
-   Neighbourhood
-   Latitude
-   Longitude
-   Room Type
-   Minimum Nights
-   Number of Reviews
-   Reviews per Month
-   Host Listings Count
-   Availability

The application then applies the saved preprocessing workflow and sends
the processed input to the saved Random Forest model.

The output is the:

**Estimated Nightly Airbnb Price**

### 📊 Model Analysis

Provides:

-   Model comparison
-   Final model metrics
-   Actual vs Predicted visualization
-   Features used by the model
-   Project limitations

------------------------------------------------------------------------

# 12. Technologies Used

The project was developed using:

-   **Python**
-   **Jupyter Notebook**
-   **Pandas**
-   **NumPy**
-   **Matplotlib**
-   **Seaborn**
-   **Scikit-learn**
-   **Joblib**
-   **Streamlit**
-   **GitHub**

------------------------------------------------------------------------

# 13. Project Structure

``` text
DS605_Lab4_Airbnb_Price_Prediction/
│
├── app.py
├── DS605_Lab4_Airbnb_Price_Prediction.ipynb
├── airbnb_price_model.pkl
├── airbnb_preprocessor.pkl
├── actual_vs_predicted.png
├── requirements.txt
└── README.md
```

------------------------------------------------------------------------

# 14. How to Run the Project Locally

## Step 1: Create and activate the virtual environment

``` bash
python -m venv .venv
```

On Windows PowerShell:

``` powershell
.venv\Scripts\Activate.ps1
```

## Step 2: Install dependencies

``` bash
pip install -r requirements.txt
```

## Step 3: Run the Streamlit application

``` bash
python -m streamlit run app.py
```

The application will open in the browser.

------------------------------------------------------------------------

# 15. Limitations

The project has several limitations:

-   The model is trained on historical New York City Airbnb data.
-   Airbnb prices can vary because of seasonality, demand, events,
    amenities, and property quality.
-   Extreme price values were removed using the IQR method.
-   Removing outliers means the model is not designed to represent the
    excluded extreme-price listings.
-   The model provides an estimated price rather than a guaranteed
    market price.
-   Some potentially useful information, such as amenities and textual
    listing information, was not included in the final feature set.
-   The model is specifically based on the characteristics represented
    in the New York City dataset.

------------------------------------------------------------------------

# 16. Conclusion

This project demonstrates a complete end-to-end machine learning
workflow for Airbnb price prediction.

The process started with exploratory analysis of the New York City
Airbnb dataset and continued through data cleaning, missing-value
treatment, outlier handling, feature selection, preprocessing,
train-test splitting, model comparison, hyperparameter tuning,
evaluation, and model persistence.

Three regression approaches were evaluated. The Random Forest Regressor
achieved the best test-set performance, with an MAE of approximately
**31.54**, RMSE of approximately **43.89**, and R² of approximately
**0.575**.

The final Random Forest model and preprocessing workflow were saved
using Joblib and integrated into a Streamlit application. The
application allows users to enter Airbnb listing characteristics and
receive an estimated nightly price.

------------------------------------------------------------------------

## Author

**Ummehani Khatri**\
**Student ID: 202618029**\
**DS605 -- Fundamentals of Machine Learning**\
**Lab Assignment 04**
