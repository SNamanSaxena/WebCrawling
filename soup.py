#!/usr/bin/env python3
import sys
import json
from bs4 import BeautifulSoup
from urllib.request import urlopen

URL =sys.argv[1]
count =int(sys.argv[2])
data = []
domain = "https://www.imdb.com"

page=urlopen(URL)
soup = BeautifulSoup(page.read(), 'html.parser')
table = soup.findChildren('table',{"class":"chart full-width"})[0]
tablebody = table.findChildren(['tbody'])[0]
rows = tablebody.find_all(['tr'])

movieList = []
for row in rows:
    movie = {}
    if count == 0:
        break
    col = row.find('td',{"class":"titleColumn"})
    title = col.find('a').text.strip()
    year = col.find('span').text.strip()
    year = year.replace('(',"")
    year = year.replace(')',"")
    rating = row.find('td',{"class":"ratingColumn"}).text.strip()
    link = col.find('a').get('href')
    soup = BeautifulSoup(urlopen(domain + link).read(), 'html.parser')
    summary = soup.find('div',{"class":"summary_text"})
    eleList = soup.find('div',{"class":"subtext"})
    duration = eleList.find('time').text.strip()
    genres = [ele.text.strip() for ele in eleList.find_all('a')]
    movie['title']=title
    movie['movie_release_year']=year
    movie['imdb_rating']=rating
    movie['summary']=summary.text.strip()
    movie['genre']=','.join(genres[0:len(genres)-1])
    movie['duration']=duration
    json_data = json.dumps(movie)
    movieList.append(json_data)
    count = count-1;
    
sys.exit(movieList)