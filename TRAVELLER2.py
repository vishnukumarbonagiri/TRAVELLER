import streamlit as st
from weather import get_weather
from pexels import get_destination_image
from ai_engine import generate_itinerary
from pdf_generator import create_pdf
from maps import create_map_link


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="TRAVELLER",
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

</style>
""", unsafe_allow_html=True)



# ==========================================
# BANNER
# ==========================================

st.image(
    "banner2.png",
    use_container_width=True
)


st.markdown("# 🌍 Welcome to TRAVELLER")

st.write(
    "Plan smarter. Travel better with your AI-powered travel assistant."
)

st.divider()



# ==========================================
# MAIN LAYOUT
# ==========================================

left, right = st.columns([1,2])



# ==========================================
# LEFT PANEL
# ==========================================

with left:

    st.subheader("🧳 Plan Your Trip")


    destination = st.text_input(
        "📍 Destination",
        placeholder="Paris"
    )


    days = st.number_input(
        "📅 Number of Days",
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



# ==========================================
# RIGHT PANEL
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


            w1,w2,w3 = st.columns(3)


            w1.metric(
                "🌡 Temperature",
                f"{weather['main']['temp']}°C"
            )


            w2.metric(
                "💧 Humidity",
                f"{weather['main']['humidity']}%"
            )


            w3.metric(
                "💨 Wind",
                f"{weather['wind']['speed']} m/s"
            )


            st.write(
                f"Condition: {weather['weather'][0]['description'].title()}"
            )


            st.divider()



        # AI ITINERARY

        with st.spinner("✈️ Creating your travel itinerary..."):

            itinerary = generate_itinerary(
                destination,
                days,
                budget,
                interests
            )


        st.subheader("🧳 AI Travel Itinerary")


        with st.container(border=True):

            st.markdown(itinerary)



        st.divider()



        # GOOGLE MAPS

        st.subheader("🗺️ Explore Destination")


        map_link = create_map_link(destination)


        st.link_button(
            "Open in Google Maps 📍",
            map_link
        )



        st.divider()



        # PDF DOWNLOAD

        pdf_file = create_pdf(itinerary)


        with open(pdf_file,"rb") as file:

            st.download_button(

                label="📄 Download Itinerary PDF",

                data=file,

                file_name="TRAVELLER_itinerary.pdf",

                mime="application/pdf"

            )



        st.divider()



        # SUMMARY

        st.subheader("📌 Trip Summary")


        c1,c2,c3,c4 = st.columns(4)


        c1.metric(
            "📍 Destination",
            destination
        )


        c2.metric(
            "📅 Days",
            days
        )


        c3.metric(
            "💰 Budget",
            budget
        )


        c4.metric(
            "🎯 Interests",
            interests
        )