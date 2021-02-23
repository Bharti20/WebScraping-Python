from pprint import pprint
import requests
import json
from Task2 import *

url = "https://www.imdb.com//title/tt0048473/"
res=requests.get(url)
dataInText=res.text
print(dataInText)

# def scrape_movie_details(movie_url):
