import streamlit as st
import re

from ai_engine import generate_itinerary
from pexels import get_destination_image
from weather import get_weather
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

background: linear-gradient(180deg, #ffffff, #f8fbff);
color:#222;
padding:30px;
border-radius:18px;
border:1px solid #dbeafe;
box-shadow:0px 6px 18px rgba(0,0,0,0.08);
font-size:18px;
line-height:1.9;
margin-bottom:20px;

}

</style>
""",
unsafe_allow_html=True
)



# ==========================
# CLEAN AI RESPONSE
# ==========================

def clean_ai_text(text):

    import re

    # Remove HTML
    text = re.sub(r"<[^>]+>", "", text)

    # Remove markdown symbols
    text = text.replace("###", "")
    text = text.replace("**", "")
    text = text.replace("`", "")

    # Add spacing before budget sections
    sections = [
        "Accommodation:",
        "Food:",
        "Transportation:",
        "Activities:",
        "Total:",
        "Trip Details:"
    ]

    for section in sections:
        text = text.replace(
            section,
            "\n\n" + section
        )

    # Fix bullet spacing
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



st.markdown(
"""
<h2 style="text-align:center;color:#0077b6;">
✨ Why Choose THETRAVELLER?
</h2>

<p style="text-align:center;font-size:18px;color:gray;">
Everything you need to plan your perfect trip in one place.
</p>
""",
unsafe_allow_html=True
)



c1,c2,c3 = st.columns(3)


with c1:

    st.info("""
### 🤖 AI Travel Planner

Generate personalized itineraries
based on your interests,
budget and trip duration.
""")


with c2:

    st.info("""
### 🌦 Live Weather

Know the current weather
before planning your trip.
""")


with c3:

    st.info("""
### 📄 Instant PDF

Download your travel plan
as a beautiful PDF.
""")


st.divider()



# ==========================
# MAIN LAYOUT
# ==========================

left,right = st.columns([1,2])



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


        # ==========================
        # DESTINATION IMAGE
        # ==========================

        image = get_destination_image(
            destination
        )


        if image:

            st.image(
                image,
                caption=destination,
                use_container_width=True
            )



        # ==========================
        # WEATHER
        # ==========================

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



        # ==========================
        # AI ITINERARY
        # ==========================

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



        st.subheader(
            "🧳 Your Personalized Travel Plan"
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



        # ==========================
        # GOOGLE MAP
        # ==========================

        st.subheader(
            "🗺️ Explore Destination"
        )


        map_url = (
            f"https://www.google.com/maps?q={destination}&output=embed"
        )


        st.components.v1.html(
            f"""
            <iframe
                src="{map_url}"
                width="100%"
                height="450"
                style="border:0;border-radius:15px;"
                allowfullscreen=""
                loading="lazy">
            </iframe>
            """,
            height=450
        )



        st.divider()



        # ==========================
        # PDF DOWNLOAD
        # ==========================

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



        # ==========================
        # SUMMARY
        # ==========================

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