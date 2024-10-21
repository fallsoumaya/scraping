from bs4 import BeautifulSoup
import requests

def soup_response(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    return soup