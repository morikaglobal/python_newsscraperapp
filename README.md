# News Scraper App using Python

News Scraper App using Python and Beautiful Soup and Flask to scrape the latest news articles from a live news site

<a href="https://python-newsscraperapp.an.r.appspot.com/" target="_blank">View Demo</a>

## About the Project

![About the Project](images/newsscraperapp.png)

This single-page web app scrapes live news site of El Paris using Beautiful Soup then the scraped data will be filtered, cleaned and displayedin the list below on this site using Flask and deployed on Google App Engine.

Built with:

- Python
- Beautiful Soup
- Flask with Jinja template

## Getting Started

Everytime my news scraper app website built with Flask gets loaded, the live news site El Paris English site (in the pic below) gets scraped with Python library Beautiful Soup.

![Getting Started](images/elparis.png)

```python
import requests
from bs4 import BeautifulSoup

r1 = requests.get("https://elpais.com/elpais/inenglish.html")
coverpage = r1.content

soup1 = BeautifulSoup(coverpage, 'html5lib')

coverpage_news = soup1.find_all('h2', class_='articulo-titulo')
```
the code above returns the raw data of all the news articles that is currently displayed on the site as follows:

![Getting Started](images/code1.png)

From the data above, I cleaned the data and extracted the title and the link of each articles currently displayed, then I did the same for different section of the web to scrape the news category of each news article.

Then using Flask and Jinja templates, I extract the data of the latest top 5 news articles and get them displayed on my news scraper app.

## Updates in April 2023

I noticed that my app was no longer scraping the news data in April 2023,
as the website my app was scraping had changes in its landing page HTML.

I made the updates to my code as below so that my app can scrape the news data as before, and my app no longer displays category title for the article as the original news website no longer displays category for every news article.

```python
import requests
from bs4 import BeautifulSoup

r1 = requests.get("https://elpais.com/elpais/inenglish.html")
coverpage = r1.content

soup1 = BeautifulSoup(coverpage, 'html5lib')

coverpage_news = soup1.find_all('h2', class_='c_t')
```


