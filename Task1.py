from bs4 import BeautifulSoup
import requests
import pprint
import json

url= "https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in"
sample = requests.get(url)
soup = BeautifulSoup(sample.text,"html.parser")
def scrape_top_list():
    main_div=soup.find("div", class_="lister")
    tbody= main_div.find("tbody", class_="lister-list")
    tr_tag = tbody.find_all ("tr")
    
    movie_name_list=[]
    movie_position=[]
    movie_years=[]
    movie_rating=[]
    movie_url=[]
    for tr in tr_tag:
        position=tr.find("td", class_="titleColumn").get_text().strip()
        rank=''
        for i in position:
            if '.' not in i:
                rank=rank+i
            else:
                break
        movie_position.append(rank)
        name=tr.find("td", class_="titleColumn").a.get_text()
        movie_name_list.append(name)
        year=tr.find("td", class_="titleColumn").span.get_text()
        movie_years.append(year)
        rating = tr.find("td", class_="ratingColumn imdbRating").strong.get_text()
        movie_rating.append(rating)
        link=tr.find("td", class_="titleColumn").a['href']
        movie_link = "https://www.imdb.com/"+link
        movie_url.append(movie_link)
    top_movies=[]
    details={'position':'', 'name':'', 'year':'', 'rating':'', 'url':'' }
    for i in range(0, len(movie_position)):
        details['position']=int(movie_position[i])
        details['name']=str(movie_name_list[i])
        movie_years[i]=movie_years[i][1:5]
        details['year']=int(movie_years[i])
        details['rating']=float(movie_rating[i])
        details['url']=str(movie_url[i])
        top_movies.append(details)
        details={'position':'', 'name':'', 'year':'', 'rating':'', 'url':'' }
    data2 = json.dumps(top_movies, indent=4)
    with open("topMovieList.json", "w") as data:
        data.write(data2)
    return top_movies
d=scrape_top_list()
# print(d)
