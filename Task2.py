from pprint import pprint
import json
from Task1 import *

def group_by_year(movies):
    years=[]
    i=0
    while i<len(movies):
        year=movies[i]['year']
        if year not in years:
            years.append(year)
        i=i+1
    x=1
    while x<len(years):
        j=0
        while j<x:
            if years[x]<years[j]:
                years[j], years[x]=years[x], years[j]
            j=j+1
        x=x+1
    index=0
    details={}
    while index <len(years):
        y=0
        list1=[]
        while y<len(movies):
            if movies[y]['year']==years[index]:
                list1.append(movies[y])
            y=y+1
        details[years[index]]=list1
    
        index=index+1
    # pprint.pprint(details)
    allData=json.dumps(details, indent=2)
    with open("groupByYear.json", "w") as dataByYear:
        dataByYear.write(allData)
    return details
group_by_year(scrape_top_list())
