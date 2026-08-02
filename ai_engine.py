import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq


# ==========================
# LOAD ENVIRONMENT
# ==========================

load_dotenv()


# ==========================
# GET GROQ API KEY
# ==========================

if "GROQ_API_KEY" in st.secrets:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
else:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")


client = Groq(
    api_key=GROQ_API_KEY
)



# ==========================
# CLEAN AI RESPONSE
# ==========================

def clean_itinerary(text):

    # Remove HTML tags
    text = text.replace("<br>", "\n")
    text = text.replace("<br/>", "\n")
    text = text.replace("<br />", "\n")


    # Fix spacing problems

    text = text.replace(
        "(avg.",
        "(avg. "
    )


    text = text.replace(
        "per night",
        " per night"
    )


    text = text.replace(
        "per day",
        " per day"
    )


    # Remove extra spaces

    text = "\n".join(
        line.strip()
        for line in text.split("\n")
    )


    return text.strip()



# ==========================
# GENERATE ITINERARY
# ==========================

def generate_itinerary(destination, days, budget, interests):


    prompt = f"""

You are a professional travel planner.

Create a detailed travel itinerary.

IMPORTANT RULES:

- Plain text only.
- Never use HTML.
- Never use <br>.
- Do not create long paragraphs.
- Use headings.
- Use bullet points.
- Keep clean spacing.


FORMAT:


🌍 {destination} Travel Plan


🏨 RECOMMENDED HOTELS

Hotel Name:
Location:
Price:


🍴 FOOD RECOMMENDATIONS

Restaurant:
Famous Food:


📅 DAY 1

Morning:
- Activity

Afternoon:
- Activity

Evening:
- Activity



📅 DAY 2

Morning:
- Activity

Afternoon:
- Activity

Evening:
- Activity



📅 DAY 3

Morning:
- Activity

Afternoon:
- Activity

Evening:
- Activity



🚗 TRANSPORTATION

-


💡 TRAVEL TIPS

-


💰 ESTIMATED BUDGET

Accommodation:
Food:
Transportation:
Activities:
Total:


Trip Details:

Destination: {destination}
Days: {days}
Budget: {budget}
Interests: {interests}


"""


    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0

    )


    result = response.choices[0].message.content


    # Apply formatting cleanup

    result = clean_itinerary(result)


    return result