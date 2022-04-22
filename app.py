from flask import Flask, render_template
from random import choice
import requests
from string import ascii_uppercase
from random_words import RandomWords
import json



app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/joker')
def joker():
    string = ''.join(choice(ascii_uppercase) for i in range(4))
    string = string.lower()
    rw = RandomWords()
    word = rw.random_word()
    url = 'https://arquivo.pt/textsearch?q=' + word + "&maxItems=1&prettyPrint=true&from=20190101000000&siteSearch=http://www.publico.pt"
    print(url)
    x = requests.get(url)

    print(x.json()["response_items"])


    return render_template('joker.html', pergunta="Mas que cheiro aqui?",
                           opcao1="Espumante",
                           opcao2="Sumo de pepino",
                           opcao3="Café curto",
                           opcao4="Imperial")

if __name__ == '__main__':
    app.run()
