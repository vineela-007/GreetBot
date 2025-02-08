import streamlit as st
import pandas as pd
import random
import datetime

# Load the dataset
file_path = "data/cheer_up_quotes.csv"
df = pd.read_csv(file_path)

# Function to determine the greeting based on time
def get_greeting():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return "Good morning"
    elif current_hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

# Streamlit App
st.title("Cheer Up!!! 💡")

# User input for name
name = st.text_input("Enter your name:")

if name:
    greeting = get_greeting()
    st.write(f"{greeting}, {name}!")
    
    # Button to generate a random quote
    if st.button("Get Inspired!"):
        quote = random.choice(df["Quote"].tolist())
        st.success(quote)
