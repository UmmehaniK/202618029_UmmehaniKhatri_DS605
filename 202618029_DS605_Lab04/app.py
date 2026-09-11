import streamlit as st
import pandas as pd
import joblib
import os


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Airbnb Price Prediction",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Main title */
.main-title {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #666666;
    margin-bottom: 25px;
}

/* Cards */
.metric-card {
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #dddddd;
    background-color: #ffffff;
    text-align: center;
}

.metric-number {
    font-size: 30px;
    font-weight: 700;
}

.metric-label {
    font-size: 15px;
    color: #666666;
}

/* Prediction result */
.prediction-box {
    padding: 30px;
    border-radius: 15px;
    border: 2px solid #333333;
    text-align: center;
    margin-top: 25px;
}

.prediction-price {
    font-size: 48px;
    font-weight: 700;
}

.prediction-label {
    font-size: 18px;
}

/* Section headings */
.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-top: 10px;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    model = joblib.load("airbnb_price_model.pkl")
    preprocessor = joblib.load("airbnb_preprocessor.pkl")

    return model, preprocessor


try:

    model, preprocessor = load_model()
    model_loaded = True

except Exception as e:

    model_loaded = False
    st.error("Unable to load the saved model files.")
    st.exception(e)


# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

st.sidebar.title("🏠 Airbnb ML")

st.sidebar.write("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Home",
        "💰 Price Prediction",
        "📊 Model Analysis"
    ]
)

st.sidebar.divider()

st.sidebar.caption(
    "DS605 Fundamentals of Machine Learning"
)

st.sidebar.caption(
    "Airbnb Price Prediction Project"
)


# ============================================================
# HOME PAGE
# ============================================================

if page == "🏠 Home":

    st.markdown(
        '<div class="main-title">🏠 Airbnb Price Prediction</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'An end-to-end machine learning application for estimating '
        'Airbnb nightly prices in New York City.'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    # Introduction
    st.markdown(
        '<div class="section-title">About the Project</div>',
        unsafe_allow_html=True
    )

    st.write(
        """
        This project uses the New York City Airbnb Open Data dataset to
        develop a machine learning model for predicting the estimated
        nightly price of an Airbnb listing.

        The complete workflow includes data cleaning, missing-value
        handling, outlier treatment, feature selection, preprocessing,
        regression model comparison, hyperparameter tuning, and model
        evaluation.
        """
    )

    st.divider()

    # Project statistics
    st.markdown(
        '<div class="section-title">📈 Project Statistics</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Original Listings",
            "48,895"
        )

    with col2:
        st.metric(
            "Final Listings",
            "45,912"
        )

    with col3:
        st.metric(
            "Selected Features",
            "10"
        )

    with col4:
        st.metric(
            "Final Model",
            "Random Forest"
        )

    st.divider()

    # Model performance
    st.markdown(
        '<div class="section-title">🎯 Final Model Performance</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "MAE",
            "$31.54"
        )

    with col2:

        st.metric(
            "RMSE",
            "$43.89"
        )

    with col3:

        st.metric(
            "R² Score",
            "0.575"
        )

    st.divider()

    st.info(
        "Use the Price Prediction page from the sidebar to estimate "
        "the nightly price of a listing."
    )


# ============================================================
# PRICE PREDICTION PAGE
# ============================================================

elif page == "💰 Price Prediction":

    st.markdown(
        '<div class="main-title">💰 Airbnb Price Prediction</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Enter the listing characteristics below to estimate the nightly price.'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        '<div class="section-title">📍 Location Information</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        neighbourhood_group = st.selectbox(
            "Neighbourhood Group",
            [
                "Bronx",
                "Brooklyn",
                "Manhattan",
                "Queens",
                "Staten Island"
            ]
        )

    with col2:

        neighbourhood = st.text_input(
            "Neighbourhood",
            value="Midtown",
            help="Enter the NYC neighbourhood."
        )

    col1, col2 = st.columns(2)

    with col1:

        latitude = st.number_input(
            "Latitude",
            value=40.7549,
            format="%.4f"
        )

    with col2:

        longitude = st.number_input(
            "Longitude",
            value=-73.9840,
            format="%.4f"
        )

    st.divider()

    st.markdown(
        '<div class="section-title">🏠 Property Information</div>',
        unsafe_allow_html=True
    )

    room_type = st.selectbox(
        "Room Type",
        [
            "Entire home/apt",
            "Private room",
            "Shared room"
        ]
    )

    st.divider()

    st.markdown(
        '<div class="section-title">📊 Listing Information</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        minimum_nights = st.number_input(
            "Minimum Nights",
            min_value=1,
            value=2,
            step=1
        )

        number_of_reviews = st.number_input(
            "Number of Reviews",
            min_value=0,
            value=50,
            step=1
        )

        reviews_per_month = st.number_input(
            "Reviews per Month",
            min_value=0.0,
            value=2.5,
            step=0.1
        )

    with col2:

        calculated_host_listings_count = st.number_input(
            "Host Listings Count",
            min_value=1,
            value=3,
            step=1
        )

        availability_365 = st.number_input(
            "Availability (365 Days)",
            min_value=0,
            max_value=365,
            value=200,
            step=1
        )

    st.divider()

    # Prediction button

    predict_button = st.button(
        "💰 Predict Nightly Price",
        use_container_width=True
    )

    if predict_button:

        if not model_loaded:

            st.error(
                "Model files could not be loaded."
            )

        else:

            # Create input dataframe
            input_data = pd.DataFrame({

                "neighbourhood_group": [
                    neighbourhood_group
                ],

                "neighbourhood": [
                    neighbourhood
                ],

                "latitude": [
                    latitude
                ],

                "longitude": [
                    longitude
                ],

                "room_type": [
                    room_type
                ],

                "minimum_nights": [
                    minimum_nights
                ],

                "number_of_reviews": [
                    number_of_reviews
                ],

                "reviews_per_month": [
                    reviews_per_month
                ],

                "calculated_host_listings_count": [
                    calculated_host_listings_count
                ],

                "availability_365": [
                    availability_365
                ]
            })

            try:

                # Apply saved preprocessing
                processed_data = preprocessor.transform(
                    input_data
                )

                # Predict price
                prediction = model.predict(
                    processed_data
                )[0]

                prediction = max(0, prediction)

                st.markdown(
                    f"""
                    <div class="prediction-box">

                        <div class="prediction-label">
                            Estimated Nightly Price
                        </div>

                        <div class="prediction-price">
                            ${prediction:.2f}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.success(
                    "Prediction generated successfully!"
                )

                st.caption(
                    "The prediction is generated using the trained "
                    "Random Forest regression model."
                )

                # Show input summary
                with st.expander("View Input Details"):

                    st.dataframe(
                        input_data,
                        use_container_width=True
                    )

            except Exception as e:

                st.error(
                    "An error occurred while generating the prediction."
                )

                st.exception(e)


# ============================================================
# MODEL ANALYSIS PAGE
# ============================================================

elif page == "📊 Model Analysis":

    st.markdown(
        '<div class="main-title">📊 Model Analysis</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Performance comparison and evaluation of the regression models.'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    # Model comparison table

    st.markdown(
        '<div class="section-title">🤖 Model Comparison</div>',
        unsafe_allow_html=True
    )

    comparison_data = pd.DataFrame({

        "Model": [
            "Linear Regression",
            "Ridge Regression",
            "Random Forest",
            "Tuned Random Forest"
        ],

        "MAE": [
            34.076,
            34.047,
            31.539,
            None
        ],

        "RMSE": [
            46.426675,
            46.398330,
            43.886839,
            44.727040
        ],

        "R² Score": [
            0.523986,
            0.524567,
            0.574643,
            0.558201
        ]
    })

    st.dataframe(
        comparison_data,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # Best model
    st.markdown(
        '<div class="section-title">🏆 Selected Model</div>',
        unsafe_allow_html=True
    )

    st.success(
        """
        Random Forest was selected as the final model because it achieved
        the best test-set performance among the evaluated models, with the
        lowest RMSE and highest R² score.
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "MAE",
            "31.54"
        )

    with col2:

        st.metric(
            "RMSE",
            "43.89"
        )

    with col3:

        st.metric(
            "R² Score",
            "0.575"
        )

    st.divider()

    # Actual vs Predicted plot

    st.markdown(
        '<div class="section-title">📈 Actual vs Predicted</div>',
        unsafe_allow_html=True
    )

    if os.path.exists("actual_vs_predicted.png"):

        st.image(
            "actual_vs_predicted.png",
            caption="Actual vs Predicted Airbnb Prices",
            use_container_width=True
        )

    else:

        st.warning(
            "actual_vs_predicted.png was not found in the project folder."
        )

    st.divider()

    # Features
    st.markdown(
        '<div class="section-title">🔍 Features Used by the Model</div>',
        unsafe_allow_html=True
    )

    features = [
        "neighbourhood_group",
        "neighbourhood",
        "latitude",
        "longitude",
        "room_type",
        "minimum_nights",
        "number_of_reviews",
        "reviews_per_month",
        "calculated_host_listings_count",
        "availability_365"
    ]

    feature_df = pd.DataFrame({
        "No.": range(1, 11),
        "Feature": features
    })

    st.dataframe(
        feature_df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # Limitations

    st.markdown(
        '<div class="section-title">⚠️ Limitations</div>',
        unsafe_allow_html=True
    )

    st.write(
        """
        • The model is trained on historical New York City Airbnb data.

        • Airbnb prices can vary because of factors such as season,
          demand, amenities, events, and property quality.

        • Extreme price values were removed during preprocessing.

        • The model provides an estimated price rather than a guaranteed
          market price.

        • The model is designed for the characteristics represented in
          the training dataset.
        """
    )

    st.divider()

    st.caption(
        "DS605 Fundamentals of Machine Learning | "
        "End-to-End Airbnb Price Prediction Project"
    )
