import os
import re
import requests
import streamlit as st
from dotenv import load_dotenv
from groq import Groq


# ===========================
# LOAD KEYS
# ===========================

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")


client = Groq(
    api_key=GROQ_API_KEY
)



# ===========================
# PAGE SETTINGS
# ===========================

st.set_page_config(
    page_title="THETRAVELLER",
    page_icon="🌍",
    layout="wide"
)



# ===========================
# CSS
# ===========================

st.markdown(
"""
<style>

.block-container{
    padding-top:1rem;
}


.travel-card{

    background:white;
    color:#222;
    padding:35px;
    border-radius:20px;
    border-left:8px solid #0077b6;
    font-size:18px;
    line-height:1.8;

}


.stButton button{

    background:#0077b6;
    color:white;
    width:100%;
    height:50px;
    border-radius:10px;
    font-size:18px;
    font-weight:bold;

}

</style>
""",
unsafe_allow_html=True
)



# ===========================
# HEADER
# ===========================


st.markdown(
"""
<h1 style="text-align:center;color:#0077b6;">
🌍 THETRAVELLER
</h1>

<p style="text-align:center;font-size:22px;">
✈️ Your intelligent travel companion<br>
Plan smarter • Explore better • Discover more
</p>

""",
unsafe_allow_html=True
)



# ===========================
# BANNER
# ===========================

st.image(
    "banner2.png",
    use_container_width=True
)


st.divider()



# ===========================
# CLEAN AI TEXT
# ===========================

def clean_text(text):

    # remove html
    text = re.sub(
        r"<[^>]*>",
        "",
        text
    )


    # remove markdown
    text = text.replace("#","")
    text = text.replace("*","")


    # remove extra spaces
    text = re.sub(
        r"\n\s*\n\s*\n+",
        "\n\n",
        text
    )


    return text.strip()





# ===========================
# PEXELS IMAGE
# ===========================

def get_destination_image(destination):

    url = "https://api.pexels.com/v1/search"


    headers = {

        "Authorization": PEXELS_API_KEY

    }


    params = {

        "query":destination,
        "per_page":1

    }


    response = requests.get(
        url,
        headers=headers,
        params=params
    )


    if response.status_code == 200:

        data=response.json()

        if data["photos"]:

            return data["photos"][0]["src"]["large"]


    return None





# ===========================
# INPUT AREA
# ===========================


left,right = st.columns([1,2])



with left:

    st.subheader("🧳 Plan Your Trip")


    destination = st.text_input(
        "📍 Destination",
        placeholder="Dubai"
    )


    days = st.number_input(
        "📅 Days",
        min_value=1,
        max_value=30,
        value=5
    )


    budget = st.text_input(
        "💰 Budget",
        placeholder="$2000"
    )


    interests = st.text_input(
        "🎯 Interests",
        placeholder="Food, Beaches, Museums"
    )


    generate = st.button(
        "🚀 Generate Travel Plan"
    )





# ===========================
# RESULT AREA
# ===========================


with right:


    if generate:


        if destination == "":

            st.warning(
                "Please enter destination"
            )

            st.stop()



        # IMAGE

        image = get_destination_image(
            destination
        )


        if image:

            st.image(
                image,
                caption=destination,
                use_container_width=True
            )




        # AI PROMPT

        prompt=f"""

You are a professional travel planner.

Create a travel itinerary.

RULES:
- Only plain text.
- No HTML.
- No <br>.
- No markdown.

Format:

{destination} Travel Plan


Recommended Hotels:

- Hotel name:
  Location:
  Price:


Food Recommendations:

- Restaurant:
  Famous food:


Day 1:

Morning:
-

Afternoon:
-

Evening:
-


Transportation:

-


Travel Tips:

-


Trip Details:

Destination:{destination}
Days:{days}
Budget:{budget}
Interests:{interests}

"""



        with st.spinner(
            "✈️ Creating itinerary..."
        ):


            response = client.chat.completions.create(

                model="llama-3.3-70b-versatile",

                messages=[

                    {
                    "role":"user",
                    "content":prompt
                    }

                ],

                temperature=0.2

            )



        itinerary = response.choices[0].message.content



        itinerary = clean_text(
            itinerary
        )



        st.subheader(
            "🧳 AI Travel Itinerary"
        )



        st.markdown(

            f"""

<div class="travel-card">

<pre style="
white-space:pre-wrap;
font-family:Arial;
color:#222;
font-size:18px;
">

{itinerary}

</pre>

</div>

""",

unsafe_allow_html=True

        )





        st.divider()



        st.subheader(
            "📌 Trip Summary"
        )



        a,b,c,d = st.columns(4)


        a.metric(
            "📍 Destination",
            destination
        )


        b.metric(
            "📅 Days",
            days
        )


        c.metric(
            "💰 Budget",
            budget
        )


        d.metric(
            "🎯 Interests",
            interests
        )