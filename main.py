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
    # updated
    coverpage_news = soup1.find_all('h2', class_='c_t')

    # out of date
    # coverpage_news = soup1.find_all('h2', class_='headline')
    # news_byline = soup1.find_all('a', class_='author')
    print(len(coverpage_news))

    for (a, b) in zip(coverpage_news,coverpage_news):
        
        data_list = {}

        data_list["title"] = a.text #.replace("\n","")
        # url = "https://english.elpais.com"
        data_list["link"] = b.a["href"]
        print(data_list["link"])
            
        news_array.append(data_list)
        
    news_array = news_array[0:5]
        
    return render_template('index.html', news_array=news_array)

if __name__ == '__main__':
      app.run()