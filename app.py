import os
import requests
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# ===========================
# Load API Keys
# ===========================
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

# ===========================
# Page Settings
# ===========================
st.set_page_config(
    page_title="TRAVELLER",
    page_icon="🌍",
    layout="wide"
)

# ===========================
# Banner
# ===========================
st.image("banner2.png", use_container_width=True)

# ===========================
# Pexels Image Function
# ===========================
def get_destination_image(destination):
    url = "https://api.pexels.com/v1/search"

    headers = {
        "Authorization": PEXELS_API_KEY
    }

    params = {
        "query": destination,
        "per_page": 1
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()

        if data["photos"]:
            return data["photos"][0]["src"]["large"]

    return None

# ===========================
# Sidebar
# ===========================
with st.sidebar:

    st.header("🧳 Trip Details")

    destination = st.text_input("📍 Destination")

    days = st.number_input(
        "📅 Number of Days",
        min_value=1,
        max_value=30,
        value=5
    )

    budget = st.text_input("💰 Budget")

    interests = st.text_input("🎯 Interests")

    generate = st.button("🚀 Generate Travel Plan")

st.divider()

if generate:
    image = get_destination_image(destination)

    if image:
        st.image(image, caption=destination, use_container_width=True)

col1, col2 = st.columns([2, 1])

# ===========================
# Main Layout
# ===========================
col1, col2 = st.columns([2, 1])

# ===========================
# Generate Plan
# ===========================
if generate:

    prompt = f"""
Create a detailed travel itinerary.

Destination: {destination}
Days: {days}
Budget: {budget}
Interests: {interests}

Include:
- Day-wise itinerary
- Hotel suggestions
- Food recommendations
- Transportation
- Estimated budget
- Travel tips
"""

    with st.spinner("Creating your itinerary..."):

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama-3.3-70b-versatile"
        )

    # LEFT COLUMN
        st.subheader("🧳 Your AI Travel Itinerary")

        st.write(chat_completion.choices[0].message.content)

    # RIGHT COLUMN
    with col2:

        st.subheader("📌 Trip Summary")

        st.success(f"""
📍 Destination: {destination}

📅 Days: {days}

💰 Budget: {budget}

🎯 Interests: {interests}
""")