import os
import requests
from dotenv import load_dotenv

load_dotenv()

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")


def get_destination_image(destination):

    if not destination:
        return None

    url = "https://api.pexels.com/v1/search"

    headers = {
        "Authorization": PEXELS_API_KEY
    }

    params = {
        "query": destination,
        "per_page": 1
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    if response.status_code == 200:

        data = response.json()

        if data["photos"]:
            return data["photos"][0]["src"]["large"]

    return None