import streamlit as st
import pandas as pd
import joblib

model = joblib.load('model.pkl')
feature_columns = joblib.load('feature_columns.pkl')

st.set_page_config(page_title="Zomato Cost Predictor", layout="centered")
st.title("🍽️Zomato Restaurant cost predictor💸")
st.write("Predict approximate Cost for two people")

# inputs
votes = st.number_input("Votes", min_value=0, value=100)
rate = st.slider("Rating", 1.0, 5.0, 3.5, step=0.1)
num_cuisines = st.number_input("Number of Cuisines", min_value=1)
popularity_score = st.slider("Popularity Score", 0.0, 1.0, 0.5)
location = st.selectbox("Location",
                        ["BTM","Koramangala 5th Block","HSR","Indiranagar","JP Nagar",
                        "Jayanagar","Marathahalli","Whitefield", "Other"])
rest_type = st.selectbox("Reastaurant Type",
                         ["Causual Dining","Quick Bites","Cafe","Dessert Parlor",
                          "Lounge", "Other"])
online_order_ui = st.selectbox("Online Order Available?", ["NO", "Yes"])
book_table_ui = st.selectbox("Table Booking Available?", ["No", "Yes"])

online_order =1 if online_order_ui=="Yes" else 0
book_table =1 if book_table_ui=="Yes" else 0

selected_cuisines = st.multiselect(
    "Selected Cuisines",
    ["North Indian", "South Indian", "Chineese", "Italian", "Fast Food",
     "Desserts", "Biryani", "Seafood", "Pizza", "Burger", "Icecreame"]
)

can_predict = True
if len(selected_cuisines) ==0:
    st.warning("⚠️ Please select at least one cuisines")
    can_predict = False
elif len(selected_cuisines) != num_cuisines:
    st.error(f"❌ Cuisine mismatch: selected {len(selected_cuisines)}"  
            f" but number of cuisines is {num_cuisines}")
    can_predict = False
else:
    st.success("✅ Cuisine count matches")



if st.button("Predict Cost"):
    if not can_predict:
        st.warning("⚠️ Please fix the issues above before predicting")
    else:
        input_df = pd.DataFrame(
            data=[[0] * len(feature_columns)],
            columns=feature_columns
        )
        input_df.loc[0, 'votes'] = votes
        input_df.loc[0, 'rate'] = rate
        input_df.loc[0, 'num_cuisines'] = num_cuisines
        input_df.loc[0, 'popularity_score'] = popularity_score

        input_df.loc[0, 'location'] = location
        input_df.loc[0, 'rest_type'] = rest_type
        input_df.loc[0, 'online_order'] = online_order
        input_df.loc[0, 'book_table'] = book_table

        for cuisine in selected_cuisines:
            col_name = f"cuisine_{cuisine}"
            if col_name in input_df.columns:
                input_df.loc[0, col_name] = 1

        prediction = model.predict(input_df)[0]
        st.success(f"💰Estimated cost for two people:₹{int(prediction)}")