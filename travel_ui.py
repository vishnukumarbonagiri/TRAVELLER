import streamlit as st
import re


def clean_ai_text(text):

    # Remove ALL HTML tags
    text = re.sub(r"<[^>]*>", "", text)

    # Remove markdown symbols
    text = text.replace("#", "")

    # Remove extra spaces
    text = text.strip()

    return text



def show_itinerary_card(itinerary):

    itinerary = clean_ai_text(itinerary)


    st.markdown(
        """
        <style>

        .travel-card {

            background:#ffffff;
            color:#222222;
            padding:35px;
            border-radius:20px;
            border-left:8px solid #0077b6;
            font-size:18px;
            line-height:1.7;

        }


        .travel-title {

            color:#0077b6;
            font-size:32px;
            font-weight:bold;

        }


        </style>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        f"""
        <div class="travel-card">

        {itinerary.replace(chr(10), "<br>")}

        </div>
        """,
        unsafe_allow_html=True
    )