import urllib.request, json
from .models import Quote

api_key = None
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config['QUOTE_API_KEY']
    base_url_key = app.config['QUOTE_API_BASE_URL']