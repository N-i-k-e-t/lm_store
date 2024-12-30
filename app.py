# app.py
import streamlit as st
import pandas as pd
import datetime

# Sample notebook data (replace with your actual data)
notebook_data = {
    "Notebook 1": {
        "Description": "A notebook for data science.",
        "Price": 29.99,
        "Cover Image": "https://via.placeholder.com/200x300/007BFF/FFFFFF?text=Notebook+1",
        "Book Link": "https://www.example.com/notebook1"
    },
    "Notebook 2": {
        "Description": "A notebook for machine learning.",
        "Price": 39.99,
        "Cover Image": "https://via.placeholder.com/200x300/DC3545/FFFFFF?text=Notebook+2",
        "Book Link": "https://www.example.com/notebook2"
    },
    # Add more notebooks here...
}

# Visitor counter
def view_counter():
    if "visits" not in st.session_state:
        st.session_state.visits = 1
    else:
        st.session_state.visits += 1
    return st.session_state.visits

# Visit log (basic example, consider a database for production)
visit_log = []

def log_visit():
    timestamp = datetime.datetime.now()
    visit_log.append(timestamp)


# Streamlit app
st.set_page_config(page_title="Notebook Store", page_icon=":notebook:", layout="wide")
st.title("Notebook Store")

visits = view_counter()
st.write(f"Total Visits: {visits}")
log_visit()


for title, details in notebook_data.items():
    with st.expander(title):
        st.image(details["Cover Image"], caption=title, width=200)
        st.write(details["Description"])
        st.write(f"Price: ${details['Price']:.2f}")
        st.markdown(f"[Get the Book!]({details['Book Link']})")
        st.button("Add to Cart", key=title)  # Unique key for each button