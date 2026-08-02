import streamlit as st
import re


def clean_ai_text(text):

    # Remove unwanted html tags from AI output
    text = re.sub(r"<br\s*/?>", "\n", text)

    # Remove remaining HTML tags
    text = re.sub(r"<[^>]*>", "", text)

    # Convert markdown headings nicely
    text = text.replace("###", "")
    text = text.replace("##", "")
    text = text.replace("#", "")

    return text.strip()



def show_itinerary_card(itinerary):

    itinerary = clean_ai_text(itinerary)


    st.markdown(
        """
        <style>

        .travel-card {

            background:white;
            color:#222;
            padding:35px;
            border-radius:20px;
            border-left:8px solid #0077b6;
            box-shadow:0px 5px 20px rgba(0,0,0,0.08);
            font-size:18px;
            line-height:1.8;

        }

        .travel-card h1,
        .travel-card h2,
        .travel-card h3 {

            color:#0077b6;

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