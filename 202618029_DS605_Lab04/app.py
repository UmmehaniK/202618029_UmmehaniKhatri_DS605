import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Airbnb Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# --------------------------------------------------
# Load Model
# --------------------------------------------------

@st.cache_resource
def load_model():
    model = joblib.load("airbnb_price_model.pkl")
    return model


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("🏠 Airbnb Price Prediction")
st.markdown(
    "Enter the details of an Airbnb listing to estimate its nightly price."
)

st.divider()

# --------------------------------------------------
# Input Section
# --------------------------------------------------

st.subheader("📋 Listing Information")

col1, col2 = st.columns(2)

with col1:

    neighbourhood_group = st.selectbox(
        "Neighbourhood Group",
        [
            "Brooklyn",
            "Manhattan",
            "Queens",
            "Staten Island",
            "Bronx"
        ]
    )

    room_type = st.selectbox(
        "Room Type",
        [
            "Entire home/apt",
            "Private room",
            "Shared room"
        ]
    )

    minimum_nights = st.number_input(
        "Minimum Nights",
        min_value=1,
        max_value=365,
        value=1
    )

    number_of_reviews = st.number_input(
        "Number of Reviews",
        min_value=0,
        value=10
    )

with col2:

    latitude = st.number_input(
        "Latitude",
        value=40.7128,
        format="%.6f"
    )

    longitude = st.number_input(
        "Longitude",
        value=-74.0060,
        format="%.6f"
    )

    reviews_per_month = st.number_input(
        "Reviews per Month",
        min_value=0.0,
        value=1.0,
        format="%.2f"
    )

    availability_365 = st.number_input(
        "Availability (365 days)",
        min_value=0,
        max_value=365,
        value=100
    )

# --------------------------------------------------
# Prediction
# --------------------------------------------------

st.divider()

if st.button("💰 Predict Airbnb Price", use_container_width=True):

    try:

        model = load_model()

        input_data = pd.DataFrame({
            "neighbourhood_group": [neighbourhood_group],
            "room_type": [room_type],
            "minimum_nights": [minimum_nights],
            "number_of_reviews": [number_of_reviews],
            "latitude": [latitude],
            "longitude": [longitude],
            "reviews_per_month": [reviews_per_month],
            "availability_365": [availability_365]
        })

        prediction = model.predict(input_data)[0]

        prediction = max(0, prediction)

        st.success(
            f"🏠 Estimated Nightly Price: **${prediction:.2f}**"
        )

    except Exception as e:

        st.error(
            "The prediction model could not be loaded or the input format "
            "does not match the trained model."
        )

        st.info(
            "We will connect this application to the final trained "
            "preprocessing pipeline and model after completing the notebook."
        )

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "DS605 - Fundamentals of Machine Learning | "
    "End-to-End Airbnb Price Prediction"
)