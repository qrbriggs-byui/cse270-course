# frontend.py
import requests

def send_greeting_request():
    url = 'http://localhost:5111/api/greet'
    response = requests.get(url)
    return response.json()    