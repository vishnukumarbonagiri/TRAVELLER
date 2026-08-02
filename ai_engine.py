import os
from groq import Groq


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_itinerary(destination, days, budget, interests):

    prompt = f"""
You are a professional travel planner.

Create a travel itinerary.

STRICT RULES:
- Output ONLY normal text.
- NEVER write HTML.
- NEVER use <h1>, <h2>, <div>, <p>, style tags.
- NEVER use markdown (# symbols).
- Do not add any code formatting.

Use this format:

{destination} Travel Plan

Recommended Hotels:
- Hotel name:
- Location:
- Price:

Food Recommendations:
- Restaurant:
- Famous food:

Day 1:
Morning:
Afternoon:
Evening:

Day 2:
Morning:
Afternoon:
Evening:

Transportation:
-

Travel Tips:
-


Trip Details:
Destination: {destination}
Days: {days}
Budget: {budget}
Interests: {interests}
"""


    result = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )


    text = result.choices[0].message.content


    # remove HTML if AI still sends it
    text = text.replace("<h1>", "")
    text = text.replace("</h1>", "")
    text = text.replace("<h2>", "")
    text = text.replace("</h2>", "")
    text = text.replace("<div>", "")
    text = text.replace("</div>", "")
    text = text.replace("<p>", "")
    text = text.replace("</p>", "")


    return text