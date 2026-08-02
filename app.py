import streamlit as st
import re

from ai_engine import generate_itinerary
from pexels import get_destination_image
from weather import get_weather
from maps import create_map_link
from pdf_generator import create_pdf


# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="THETRAVELLER",
    page_icon="🌍",
    layout="wide"
)


# ==========================
# CSS
# ==========================

st.markdown(
"""
<style>

.travel-card {

background:white;
color:#222;
padding:35px;
border-radius:20px;
border-left:8px solid #0077b6;
font-size:18px;
line-height:1.8;

}

</style>
""",
unsafe_allow_html=True
)



# ==========================
# CLEAN AI RESPONSE
# ==========================

def clean_ai_text(text):

    # Convert HTML breaks into real line breaks
    text = re.sub(
        r"<br\s*/?>",
        "\n",
        text,
        flags=re.IGNORECASE
    )


    # Remove remaining HTML tags
    text = re.sub(
        r"<[^>]+>",
        "",
        text
    )


    # Remove markdown symbols
    text = text.replace(
        "###",
        ""
    )

    text = text.replace(
        "**",
        ""
    )


    # Remove extra empty lines
    text = re.sub(
        r"\n\s*\n\s*\n+",
        "\n\n",
        text
    )


    return text.strip()



# ==========================
# HEADER
# ==========================


st.markdown(
"""
<h1 style="text-align:center;color:#0077b6;">
🌍 THETRAVELLER
</h1>

<p style="text-align:center;font-size:20px;">
✈️ Your Intelligent Travel Companion
<br>
Plan smarter • Explore better • Discover more
</p>

""",
unsafe_allow_html=True
)



st.image(
    "banner2.png",
    use_container_width=True
)


st.divider()



# ==========================
# MAIN LAYOUT
# ==========================

left, right = st.columns([1,2])



# ==========================
# LEFT FORM
# ==========================

with left:


    st.subheader(
        "🧳 Plan Your Trip"
    )


    destination = st.text_input(
        "📍 Destination",
        placeholder="Paris"
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
        placeholder="Food, Museums, Beaches"
    )


    generate = st.button(
        "🚀 Generate Travel Plan"
    )




# ==========================
# RIGHT OUTPUT
# ==========================

with right:


    if generate:


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



        # WEATHER

        weather = get_weather(
            destination
        )


        if weather:


            st.subheader(
                "🌦 Weather"
            )


            c1,c2,c3 = st.columns(3)


            c1.metric(
                "🌡 Temperature",
                f"{weather['main']['temp']}°C"
            )


            c2.metric(
                "💧 Humidity",
                f"{weather['main']['humidity']}%"
            )


            c3.metric(
                "💨 Wind",
                f"{weather['wind']['speed']} m/s"
            )


            st.divider()



        # AI GENERATION

        with st.spinner(
            "✈️ Creating your itinerary..."
        ):


            raw_itinerary = generate_itinerary(
                destination,
                days,
                budget,
                interests
            )



        itinerary = clean_ai_text(
            raw_itinerary
        )



        # DISPLAY


        st.subheader(
            "🧳 AI Travel Itinerary"
        )


        st.markdown(
            f"""
<div class="travel-card">

{itinerary}

</div>
""",
            unsafe_allow_html=True
        )



        st.divider()



        # MAP


        st.subheader(
            "🗺️ Explore Destination"
        )


        map_link = create_map_link(
            destination
        )


        st.link_button(
            "Open Google Maps 📍",
            map_link
        )



        st.divider()



        # PDF


        pdf_file = create_pdf(
            itinerary
        )


        with open(pdf_file,"rb") as file:


            st.download_button(

                label="📄 Download THETRAVELLER PDF",

                data=file,

                file_name="THETRAVELLER_plan.pdf",

                mime="application/pdf"

            )



        st.divider()



        # SUMMARY


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