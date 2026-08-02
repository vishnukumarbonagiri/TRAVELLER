import streamlit as st


def show_itinerary_card(itinerary):


    st.markdown(
    """
    <style>

    .travel-card{

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


    st.markdown(

    f"""
    <div class="travel-card">

    {itinerary.replace("\n","<br>")}

    </div>
    """,

    unsafe_allow_html=True

    )