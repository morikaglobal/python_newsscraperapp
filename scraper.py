from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def show_news():
    news_array = []

    r1 = requests.get("https://elpais.com/elpais/inenglish.html")
    coverpage = r1.content
    soup1 = BeautifulSoup(coverpage, 'html.parser')

    coverpage_news = soup1.find_all('h2', class_='articulo-titulo')
    news_category = soup1.find_all('a', class_='enlace')

    for (a, b, c) in zip(coverpage_news,coverpage_news,news_category):
        
        data_list = {}

        data_list["title"] = a.text.replace("\n","")
        data_list["link"] = b.a["href"]
        data_list["category"] = c.text.replace("\n","")
            
        news_array.append(data_list)
        
    news_array = news_array[0:5]
        
    return render_template('index.html', news_array=news_array)

if __name__ == '__main__':
      app.run()