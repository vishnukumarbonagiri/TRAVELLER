import streamlit as st
import re

from weather import get_weather
from pexels import get_destination_image
from ai_engine import generate_itinerary
from pdf_generator import create_pdf
from maps import create_map_link


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="THETRAVELLER",
    page_icon="🌍",
    layout="wide"
)


# ==========================================
# CSS
# ==========================================

st.markdown("""
<style>

.block-container{
    padding-top:1rem;
}

.stButton>button{
    width:100%;
    height:50px;
    background:#0077b6;
    color:white;
    border-radius:10px;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#005f87;
}


.travel-card{

    background:white;
    color:#222;
    padding:30px;
    border-radius:20px;
    border-left:8px solid #0077b6;
    font-size:18px;
    line-height:1.7;

}

</style>
""", unsafe_allow_html=True)



# ==========================================
# CLEAN AI RESPONSE
# ==========================================

def clean_response(text):

    # remove html tags
    text = re.sub(
        r"<[^>]*>",
        "",
        text
    )

    # remove markdown
    text = text.replace("#","")

    return text.strip()



# ==========================================
# HEADER
# ==========================================

st.markdown(
"""
<h1 style='text-align:center;color:#0077b6;'>
🌍 THETRAVELLER
</h1>
""",
unsafe_allow_html=True
)


st.markdown(
"""
<p style='text-align:center;font-size:22px;'>
✈️ Your intelligent travel companion<br>
Plan smarter • Explore better • Discover more
</p>
""",
unsafe_allow_html=True
)



# ==========================================
# BANNER
# ==========================================

st.image(
    "banner2.png",
    use_container_width=True
)


st.divider()



# ==========================================
# MAIN AREA
# ==========================================

left,right = st.columns([1,2])



# ==========================================
# LEFT SIDE
# ==========================================

with left:

    st.subheader("🧳 Plan Your Trip")


    destination = st.text_input(
        "📍 Destination",
        placeholder="Dubai"
    )


    days = st.number_input(
        "📅 Number of Days",
        1,
        30,
        5
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



# ==========================================
# RIGHT SIDE
# ==========================================

with right:


    if generate:


        # IMAGE

        image = get_destination_image(destination)


        if image:

            st.image(
                image,
                caption=destination,
                use_container_width=True
            )



        # WEATHER

        weather = get_weather(destination)


        if weather:

            st.subheader("🌦 Current Weather")


            a,b,c = st.columns(3)


            a.metric(
                "🌡 Temperature",
                f"{weather['main']['temp']}°C"
            )


            b.metric(
                "💧 Humidity",
                f"{weather['main']['humidity']}%"
            )


            c.metric(
                "💨 Wind",
                f"{weather['wind']['speed']} m/s"
            )


            st.write(
                "Condition:",
                weather["weather"][0]["description"].title()
            )


            st.divider()



        # AI

        with st.spinner(
            "✈️ Creating your travel itinerary..."
        ):

            itinerary = generate_itinerary(
                destination,
                days,
                budget,
                interests
            )



        cleaned = clean_response(itinerary)



        st.subheader(
            "🧳 AI Travel Itinerary"
        )


        st.markdown(
            f"""
            <div class="travel-card">

            {cleaned.replace(chr(10),"<br>")}

            </div>
            """,
            unsafe_allow_html=True
        )



        st.divider()



        # MAP

        st.subheader(
            "🗺️ Explore Destination"
        )


        map_link = create_map_link(destination)


        st.link_button(
            "Open in Google Maps 📍",
            map_link
        )



        st.divider()



        # PDF

        pdf_file = create_pdf(cleaned)


        with open(pdf_file,"rb") as file:


            st.download_button(

                "📄 Download THETRAVELLER PDF",

                data=file,

                file_name="THETRAVELLER_itinerary.pdf",

                mime="application/pdf"

            )



        st.divider()



        # SUMMARY

        st.subheader(
            "📌 Trip Summary"
        )


        x1,x2,x3,x4 = st.columns(4)


        x1.metric(
            "📍 Destination",
            destination
        )


        x2.metric(
            "📅 Days",
            days
        )


        x3.metric(
            "💰 Budget",
            budget
        )


        x4.metric(
            "🎯 Interests",
            interests
        )