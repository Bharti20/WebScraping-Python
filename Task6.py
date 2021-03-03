from pprint import pprint
from bs4 import BeautifulSoup
import requests
import json
from Task5 import *

top_movies = scrape_top_list()
movies_detail_list = get_movie_list_details(top_movies[:10])

def analyse_movies_language(movies_list):
    i=0
    listOfLanguage=[]
    while i<len(movies_list):
        store=movies_list[i]["language"]
        j=0
        while j<len(store):
            listOfLanguage.append(store[j])
            j=j+1
        i=i+1
    print(listOfLanguage)
    index=0
    dic={}
    while index<len(listOfLanguage):
        z=0
        count=0
        while z<len(listOfLanguage):
            if listOfLanguage[index]==listOfLanguage[j]:
                count=count+1
            z=z+1
        if listOfLanguage[index] not in dic:
            dic[listOfLanguage[index]]=count
        index=index+1
    print(dic)  
analyse_movies_language(movies_detail_list)