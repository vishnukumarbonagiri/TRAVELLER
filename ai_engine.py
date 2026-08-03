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

try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except Exception:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")


client = Groq(
    api_key=GROQ_API_KEY
)



# ==========================
# CLEAN AI RESPONSE
# ==========================

def clean_itinerary(text):

    # Remove HTML
    text = text.replace("<br>", "\n")
    text = text.replace("<br/>", "\n")
    text = text.replace("<br />", "\n")


    # Remove markdown symbols
    text = text.replace("###", "")
    text = text.replace("**", "")
    text = text.replace("`", "")


    # Fix budget formatting

    text = text.replace(
        "Accommodation:",
        "\n\nAccommodation:"
    )

    text = text.replace(
        "Food:",
        "\n\nFood:"
    )

    text = text.replace(
        "Transportation:",
        "\n\nTransportation:"
    )

    text = text.replace(
        "Activities:",
        "\n\nActivities:"
    )

    text = text.replace(
        "Total:",
        "\n\nTotal:"
    )


    # Fix average spacing

    text = text.replace(
        "(avg.",
        "(avg. "
    )


    # Remove extra spaces

    lines = []

    for line in text.split("\n"):
        if line.strip():
            lines.append(line.strip())


    return "\n\n".join(lines)



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
- Never use backticks (`).
- Never wrap numbers or prices in code formatting.
- Do not create long paragraphs.
- Use headings.
- Use bullet points.
- Keep clean spacing.
- Output must be normal readable text that can be directly displayed in a travel app.



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