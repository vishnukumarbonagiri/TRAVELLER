import os
from groq import Groq
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_itinerary(destination, days, budget, interests):

    prompt = f"""
Create a beautiful travel itinerary.

Use Markdown formatting.
Use headings, emojis, and clear sections.

Trip Details:

📍 Destination: {destination}

📅 Number of Days: {days}

💰 Budget: {budget}

🎯 Interests: {interests}


Create the itinerary in this format:


# 🗓️ Day 1

## 🏛️ Attractions
- Places to visit
- Things to experience


## 🍽️ Food
- Restaurants
- Local dishes to try


## 🏨 Hotel
- Hotel suggestions
- Area to stay


## 🚗 Transportation
- How to move around


Repeat the same format for all days.


Also include:


# 💰 Estimated Budget

Provide approximate costs for:
- Hotels
- Food
- Transportation
- Activities


# 💡 Travel Tips

Include:
- Safety tips
- Best time to visit
- Local advice
- Things to avoid

Make it detailed, practical, and easy for a traveler to follow.
"""


    response = client.chat.completions.create(

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        model="llama-3.3-70b-versatile"

    )


    return response.choices[0].message.content