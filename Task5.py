from pprint import pprint
from bs4 import BeautifulSoup
import requests
import json
from Task4 import *

top_movies = scrape_top_list()
def get_movie_list_details(movie_list):
    listOfUrl=[]
    scrapMoviesList10=[]
    i=0
    while i<len(movie_list):
       listOfUrl.append(movie_list[i]['url'])
       scrap_data=scrape_movie_details(listOfUrl[i])
       scrapMoviesList10.append(scrap_data)
       i=i+1
    return scrapMoviesList10
get_movie_list_details(top_movies[:178])

    