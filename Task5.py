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
    all_scrap_data=json.dumps(scrapMoviesList10,indent=2)
    with open("scrap_data_of_10.json", "w") as stored_data:
        stored_data.write(all_scrap_data)
    return scrapMoviesList10
get_movie_list_details(top_movies[:10])

# j=0
    # list_of_count=[]
    # while j<len(movies_list):
    #     index=0
    #     count=0
    #     while index<len(movies_list):
    #         if movies_list[j]==movies_list[index]:
    #             count=count+1
    #         index=index+1
    #     if movies_list[j] not in list_of_count:
    #         list_of_count.append(movies_list[j])
    #         list_of_count.append(count)
    #     j=j+1
    # print(list_of_count)
    # language=["Bengali",'Malayalam', 'Hindi','Tamil', 'Marathi','Malayalam']
    # x=0
    # y=0
    # dic={}
    # while x<len(list_of_count):
    #     if (type(list_of_count[x]))==int:
    #         dic[language[y]]=list_of_count[x]
    #         y=y+1
    #     x=x+1
    # print(dic)