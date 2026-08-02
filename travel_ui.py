import streamlit as st
import re


def clean_text(text):

    # Remove HTML
    text = re.sub(r"<[^>]*>", "", text)

    # Clean markdown symbols
    text = text.replace("#", "")

    # Convert HTML breaks
    text = text.replace("<br>", "\n")

    return text.strip()



def show_itinerary_card(itinerary):

    itinerary = clean_text(itinerary)


    st.markdown(
        """
        <style>

        .section-card{

            background:white;
            padding:25px;
            border-radius:18px;
            border-left:6px solid #0077b6;
            margin-bottom:20px;
            box-shadow:0px 4px 15px rgba(0,0,0,0.08);

        }


        .section-title{

            color:#0077b6;
            font-size:24px;
            font-weight:bold;

        }


        .main-title{

            color:#023e8a;
            font-size:32px;
            font-weight:bold;

        }


        .text{

            color:#333;
            font-size:17px;
            line-height:1.7;

        }

        </style>
        """,
        unsafe_allow_html=True
    )


    lines = itinerary.split("\n")


    current_section = []


    for line in lines:

        line=line.strip()


        if line:

            current_section.append(line)



    # Display main card

    st.markdown(
        '<div class="section-card">',
        unsafe_allow_html=True
    )


    for item in current_section:


        if "hotel" in item.lower():

            st.markdown(
                f'<div class="section-title">🏨 {item}</div>',
                unsafe_allow_html=True
            )


        elif "food" in item.lower() or "restaurant" in item.lower():

            st.markdown(
                f'<div class="section-title">🍽️ {item}</div>',
                unsafe_allow_html=True
            )


        elif "transport" in item.lower():

            st.markdown(
                f'<div class="section-title">🚗 {item}</div>',
                unsafe_allow_html=True
            )


        elif "tip" in item.lower():

            st.markdown(
                f'<div class="section-title">💡 {item}</div>',
                unsafe_allow_html=True
            )


        elif "day" in item.lower():

            st.markdown(
                f'<div class="section-title">📅 {item}</div>',
                unsafe_allow_html=True
            )


        else:

            st.markdown(
                f'<div class="text">• {item}</div>',
                unsafe_allow_html=True
            )


    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )