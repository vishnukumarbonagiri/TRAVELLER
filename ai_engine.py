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

Include:

- Day-wise itinerary
- Hotel suggestions
- Food recommendations
- Transportation
- Estimated budget
- Travel tips
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