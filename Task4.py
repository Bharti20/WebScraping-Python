from pprint import pprint
from bs4 import BeautifulSoup
import requests
import json
from Task3 import *
import os.path
from os import path
top_movies = scrape_top_list()
def scrape_movie_details(movie_url):
    
    ########### Chaching part ##############
    movie_id=""
    for id in movie_url[27:]:
        if '/' not in id:
            movie_id=movie_id+id
    file_name= movie_id+".json"
    if path.exists(file_name)==True:
        with open(file_name, "r") as  stored_all_data:
            data_convert=json.load(stored_all_data)
            return data_convert
    ############################################
    else:   
        res=requests.get(movie_url)
        soup=BeautifulSoup(res.text, "html.parser")
        movieDetails=soup.find("div", class_="title_wrapper").h1.get_text()
        movie_name=""
        for i in movieDetails:
            if '(' not in i:
                movie_name=(movie_name+i)
            else:
                break
        director_name=soup.find("div", class_="credit_summary_item").a.get_text()
        sub_div=soup.find("div", class_="subtext")
        runtime=sub_div.find('time').get_text().strip()
        runtime_hours=int(runtime[0])*60
        movie_runtime=0
        if "min" in runtime:
            runtime_minutes=int(runtime[3:].strip('min'))
            movie_runtime=runtime_hours+runtime_minutes
        else:
            movie_runtime=runtime_hours
        genre=sub_div.find_all('a')
        genre.pop()
        movie_genre=[i.get_text() for i in genre]
        div_data=soup.find("div", class_= "plot_summary")
        bio_div=div_data.find("div",class_="summary_text").get_text().strip()
        poster_data=soup.find("div",class_="poster")
        poster_image_url=poster_data.find("img")['src']

        other_details=soup.find("div", attrs={"class":"article", "id":"titleDetails"})
        div_list=other_details.find_all('div')
        for div in div_list:
            tag4=div.find_all("h4")
            for text in tag4:
                if "Language:" in text:
                    store_data=div.find_all('a')
                    movie_language=[language.get_text() for language in store_data]
                elif "Country:" in text:
                    store_data=div.find_all('a')
                    movie_country=''.join([country.get_text() for country in store_data])
        scrap_data={}
        List=[]
        scrap_data['name']=movie_name.strip()
        List.append(director_name)
        scrap_data['director']=List
        scrap_data['country']=movie_country
        scrap_data['language']=movie_language
        scrap_data['poster_image_url']=poster_image_url
        scrap_data['bio']=bio_div
        scrap_data['runtime']=movie_runtime
        scrap_data['genre']=movie_genre
        allData=json.dumps(scrap_data, indent=2)
        with open(file_name,'w') as all_data:
            all_data.write(allData)
        return scrap_data
url=top_movies[0]['url']
scrape_movie_details(url)