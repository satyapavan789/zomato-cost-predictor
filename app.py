import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="🍽️Zomato Cost Predictor",
    layout="centered"
)

st.title("🍽️ Zomato Restaurant Cost Predictor")
st.write("Predict approximate cost for two people")

model = joblib.load('model.pkl')

st.subheader("Restaurant Details")

votes = st.number_input("Votes", min_value=0, step=1)

rate = st.slider(
    "Rating",
    min_value=1.0,
    max_value=5.0,
    value=4.0,
    step=0.1
)

num_cuisines = st.number_input(
    "Number of Cuisines",
    min_value=1,
    max_value=10,
    value=2,
    step=1
)

popularity_score = st.slider(
    "Popularity Score",
    min_value=0.0,
    max_value=1.0,
    value=0.5,
    step=0.05
)

location = st.selectbox(
    "Location",
    ["BTM", "Koramangala 5th Block", "HSR", "Indiranagar", "JP Nagar", "Other"]
)

rest_type = st.selectbox(
    "Restaurant Type",
    ["Casual Dining", "Quick Bites", "Cafe", "Dessert Parlor", "Fine Dining", "Lounge", "Other"]
)

online_order = st.selectbox("Online Order Available?", ["Yes", "No"])
book_table = st.selectbox("Table Booking Available?", ["Yes", "No"])

online_order = 1 if online_order == "Yes" else 0
book_table = 1 if book_table == "Yes" else 0

is_high_cost = 1 if (rate >= 4.0 and votes > 100) else 0

if st.button("Predict Cost 💰"):

    input_df = pd.DataFrame([{
        "votes": votes,
        "rate": rate,
        "num_cuisines": num_cuisines,
        "popularity_score": popularity_score,
        "is_high_cost": is_high_cost,
        "location": location,
        "rest_type": rest_type,
        "online_order": online_order,
        "book_table": book_table
    }])

    try:
        prediction = model.predict(input_df)[0]
        st.success(f"💰 Estimated Cost for Two: ₹{int(prediction)}")

    except Exception as e:
        st.error("⚠️ Prediction failed")
        st.exception(e)
