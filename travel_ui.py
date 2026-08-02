import streamlit as st
import re


def show_itinerary_card(itinerary):

    # remove html tags
    itinerary = re.sub(r"<.*?>", "", itinerary)

    # clean markdown
    itinerary = itinerary.replace("#", "")

    # fix br tags
    itinerary = itinerary.replace("<br>", "\n")

    itinerary = itinerary.strip()


    st.markdown(
        """
        <style>

        .travel-box {
            background:white;
            padding:30px;
            border-radius:20px;
            border-left:8px solid #0077b6;
            color:#222;
            font-size:18px;
            line-height:1.8;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


    with st.container():

        st.markdown(
            f"""
            <div class="travel-box">

            {itinerary}

            </div>
            """,
            unsafe_allow_html=True
        )