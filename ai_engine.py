import os
from dotenv import load_dotenv
from groq import Groq


# ==========================
# LOAD ENV
# ==========================

load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)



# ==========================
# GENERATE ITINERARY
# ==========================

def generate_itinerary(destination, days, budget, interests):


    prompt = f"""

You are a professional travel planner.

Create a detailed travel itinerary.

IMPORTANT RULES:

- Plain text only.
- Do NOT use HTML.
- Do NOT use <br>.
- Do NOT create long paragraphs.
- Use clear line breaks.
- Use headings.
- Use bullet points.


FORMAT EXACTLY:


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
- 

Afternoon:
-

Evening:
-


📅 DAY 2

Morning:
-

Afternoon:
-

Evening:
-


📅 DAY 3

Morning:
-

Afternoon:
-

Evening:
-


🚗 TRANSPORTATION

-




💡 TRAVEL TIPS

-




💰 ESTIMATED BUDGET

-




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


    return result