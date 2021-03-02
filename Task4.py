from pprint import pprint
from bs4 import BeautifulSoup
import requests
import json
from Task3 import *

def scrape_movie_details(movie_url):
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
    runtime_hours=int(runtime[0])
    minutes=int(runtime[3:4])
    total_runtime=runtime_hours*60+minutes
    genre=sub_div.find('a').get_text().strip()
    div_data=soup.find("div", class_= "plot_summary")
    bio_div=div_data.find("div",class_="summary_text").get_text().strip()
    poster_data=soup.find("div",class_="poster")
    poster_image_url=poster_data.find("img")['src']
    other_details=soup.find("div", class_="article", id="titleDetails")
    country_name=other_details.find("div", class_="txt-block").a.get_text()
    language=other_details.find_all("div", class_="txt-block")
    for i in  language:
        z=i.get_text()
        count=0
        string=""
        if "Language:" in z:
            for x in z.strip():
                count=count+1
                if count>10:
                    string=string+x
            break
    scrap_data={}
    genre_list=[]
    List=[]
    scrap_data['name']=movie_name.strip()
    List.append(director_name)
    scrap_data['director']=List
    scrap_data['country']=country_name
    scrap_data['language']=string
    scrap_data['poster_image_url']=poster_image_url
    scrap_data['bio']=bio_div
    scrap_data['runtime']=total_runtime
    genre_list.append(genre)
    scrap_data['genre']=genre_list
    allData=json.dumps(scrap_data, indent=2)
    with open('scrapMovieDetails.json','w') as all_data:
        all_data.write(allData)
    return scrap_data
scrape_movie_details("https://www.imdb.com/title/tt0048473/")