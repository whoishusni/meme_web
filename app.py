from flask import Flask, render_template
import requests as rq

app = Flask('__name__')

def get_meme():
    base_url = 'https://meme-api.herokuapp.com/gimme/'
    endpoint = 'wholesomememes'
    total_memes = '3'
    response = rq.get(base_url+endpoint).json()
    title_meme = response['title']
    url_meme = response['url']
    return title_meme, url_meme

    # MASIH MAU DIPERBAIKI + 3 total memes
    # for i in response['memes']:
    #     title_meme = i['title']
    #     url_meme = i['url']
    #     return title_meme, url_meme
        
    
@app.route('/')
def index():
    title,url = get_meme()
    return render_template("index.html",title=title, url=url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)