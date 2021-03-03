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
    index=0
    dic={}
    while index<len(listOfLanguage):
        z=0
        count=0
        while z<len(listOfLanguage):
            if listOfLanguage[index]==listOfLanguage[z]:
                count=count+1
            z=z+1
        if listOfLanguage[index] not in dic:
            dic[listOfLanguage[index]]=count
        index=index+1
    json_data=json.dumps(dic, indent=2)
    with open ("language_data.json", "w") as data_of_language:
        data_of_language.write(json_data)
    return dic
analyse_movies_language(movies_detail_list)