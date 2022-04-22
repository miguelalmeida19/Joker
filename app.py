from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/joker')
def joker():
   return render_template('joker.html', pergunta="Mas que cheiro aqui?",
                          opcao1="Espumante",
                          opcao2="Sumo de pepino",
                          opcao3="Café curto",
                          opcao4="Imperial")


if __name__ == '__main__':
   app.run()