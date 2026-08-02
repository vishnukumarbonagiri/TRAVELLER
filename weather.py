import requests
import streamlit as st


OPENWEATHER_API_KEY = st.secrets["OPENWEATHER_API_KEY"]


def get_weather(city):

    if not city:
        return None

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

    return None