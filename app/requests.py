import urllib.request, json
from .models import Tale
import requests, json

base_url = None


def configure_request(app):
    global base_url
    base_url = app.config['BASE_URL']

def  requests():
    request = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    quotes = request.json()


    return quotes
