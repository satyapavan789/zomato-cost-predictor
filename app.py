import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")

st.set_page_config(page_title="🍽️Zomato Cost Predictor", layout="centered")

st.title("🍽️ Zomato Restaurant Cost Predictor")
st.write("Predict approximate cost for two people")

ALL_CUISINES = [
    "Bakery", "Beverages", "Cafe", "Chinese", "Continental",
    "Desserts", "Fast Food", "Italian", "North Indian",
    "Pizza", "Seafood", "Street Food"
]

LOCATIONS = [
    "BTM", "Koramangala 5th Block", "HSR", "Indiranagar",
    "JP Nagar", "Jayanagar", "Marathahalli", "Whitefield", "Other"
]

REST_TYPES = [
    "Casual Dining", "Quick Bites", "Cafe",
    "Dessert Parlor", "Lounge", "Other"
]

votes = st.number_input("Votes", min_value=0, value=100)
rate = st.slider("Rating", min_value=1.0, max_value=5.0, value=4.0, step=0.1)
popularity_score = st.slider("Popularity Score", 0.0, 1.0, 0.5)

selected_cuisines = st.multiselect("Select Cuisines", ALL_CUISINES)
num_cuisines = st.number_input("Number of Cuisines", min_value=1, value=len(selected_cuisines))

location = st.selectbox("Location", LOCATIONS)
rest_type = st.selectbox("Restaurant Type", REST_TYPES)

online_order = st.selectbox("Online Order Available?", ["No", "Yes"])
book_table = st.selectbox("Table Booking Available?", ["No", "Yes"])

error = False

if len(selected_cuisines) == 0:
    st.error("❌ Please select at least one cuisine")
    error = True

if num_cuisines != len(selected_cuisines):
    st.error("❌ Number of cuisines must match selected cuisines")
    error = True

if st.button("Predict Cost") and not error:

    
    online_order = 1 if online_order == "Yes" else 0
    book_table = 1 if book_table == "Yes" else 0

    
    is_high_cost = 1 if rate >= 4.0 else 0
    cuisine_rating_interaction = rate * num_cuisines

    
    input_data = {
        "votes": votes,
        "rate": rate,
        "num_cuisines": num_cuisines,
        "popularity_score": popularity_score,
        "is_high_cost": is_high_cost,
        "cuisine_rating_interaction": cuisine_rating_interaction,
        "location": location,
        "rest_type": rest_type,
        "online_order": online_order,
        "book_table": book_table,
    }

    
    for cuisine in ALL_CUISINES:
        input_data[f"cuisine_{cuisine}"] = 1 if cuisine in selected_cuisines else 0

    
    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)[0]

    st.success(f"💰 Estimated Cost for Two People: ₹ {int(prediction)}")
