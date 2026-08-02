import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_itinerary(destination, days, budget, interests):

    prompt = f"""
Create a detailed travel itinerary.

Destination: {destination}
Days: {days}
Budget: {budget}
Interests: {interests}

Include the following format:

🗓️ Day-wise itinerary

For each day include:

## Day 1
🏛️ Attractions:
- Places to visit

🍽️ Food:
- Restaurants and local dishes

🏨 Hotel:
- Hotel suggestions

🚗 Transportation:
- How to move around


Also include:

💰 Estimated Budget

💡 Travel Tips
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