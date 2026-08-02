import urllib.parse


def create_map_link(place):

    encoded_place = urllib.parse.quote(place)

    return f"https://www.google.com/maps/search/{encoded_place}"