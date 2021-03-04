from pprint import pprint
import json
from Task2 import *

def group_by_decade(movies):
    movies_by_year=group_by_year(movies)
    listOfDecade=[]
    movieDic={}
    for i in movies_by_year:
        modules = i%10
        year= i-modules
        if year not in listOfDecade:
            listOfDecade.append(year)
    for index in listOfDecade:
        movieDic[index]=[]
    for index in movieDic:
        decade10 = index + 9
        for x in movies_by_year:
            if x<=decade10 and x>=index:
                for j in movies_by_year[x]:
                    movieDic[index].append(j)
    # data=json.dumps(movieDic, indent=2)
    # with open("decadeData.json", "w") as convertToJson:
    #     convertToJson.write(data)
group_by_decade(scrape_top_list())
