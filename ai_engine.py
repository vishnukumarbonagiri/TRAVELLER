import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)



def format_itinerary(text):

    # Force line breaks after important sections

    sections = [
        "🌍",
        "🏨",
        "🍴",
        "📅",
        "🚗",
        "💡",
        "💰",
        "Trip Details"
    ]


    for section in sections:
        text = text.replace(
            section,
            "\n\n" + section
        )


    # Fix common labels

    text = text.replace(
        "Morning:",
        "\nMorning:"
    )

    text = text.replace(
        "Afternoon:",
        "\nAfternoon:"
    )

    text = text.replace(
        "Evening:",
        "\nEvening:"
    )


    return text.strip()



def generate_itinerary(destination, days, budget, interests):


    prompt = f"""

You are a professional travel planner.

Create a travel itinerary.

RULES:

- Plain text only.
- Use many line breaks.
- Never create a paragraph.
- Use headings.
- Use bullet points.

Format:

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
                "role":"user",
                "content":prompt
            }
        ],

        temperature=0

    )


    result = response.choices[0].message.content


    # IMPORTANT FIX
    result = format_itinerary(result)


    return result