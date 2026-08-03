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


    # Remove markdown
    text = text.replace("###", "")
    text = text.replace("**", "")
    text = text.replace("`", "")


    # Fix spacing

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


    # Fix average word

    text = text.replace(
        "(avg.",
        "(average "
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

Create a travel itinerary.


IMPORTANT RULES:

- Plain text only.
- No HTML.
- No <br>.
- No backticks.
- No markdown tables.
- No code formatting.
- Use headings.
- Use bullet points.
- Keep clean spacing.


Create this structure:


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

- Transport options


💡 TRAVEL TIPS

- Tips



💰 ESTIMATED BUDGET


Accommodation:
Amount: 
Details:


Food:
Amount:
Details:


Transportation:
Amount:
Details:


Activities:
Amount:
Details:


Total:
Amount:


STRICT BUDGET RULES:

- Amount and Details must be on separate lines.
- Never use avg.
- Never combine categories.
- Never mix currencies.
- Use the user's budget currency.
- Keep realistic costs.



TRIP DETAILS:

Destination:
{destination}

Days:
{days}

User Budget:
{budget}


User Interests:
{interests}


IMPORTANT:

- Use ONLY the user's interests.
- Do not add new interests.
- Do not assume hobbies.
- If user enters Food, only focus on food experiences.


"""


    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.1

    )


    result = response.choices[0].message.content


    result = clean_itinerary(result)


    return result