import os
from ..models import Market, Logo


CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


def create_market(**variable_data):
    if 'country' not in variable_data:
        variable_data['country'] = 'uk'
    if 'name' not in variable_data:
        variable_data['name'] = "Amazon"
    market = Market(**variable_data)
    market.save()
    return market


def create_logo(**variable_data):
    if 'name' not in variable_data:
        variable_data['name'] = 'logo'
    if '_encoded_data' not in variable_data:
        variable_data['_encoded_data'] = (
            'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HA'
            'wCAAAAC0lEQVR4nGP6LwkAAiABG+faPgsAAAAASUVORK5CYII=')
    logo = Logo(**variable_data)
    logo.save()
    return logo


def load_sample_png():
    f = open("{}/png/sample.png".format(CURRENT_DIRECTORY), "rb")
    return f
