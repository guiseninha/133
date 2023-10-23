# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Guilherme" # escreva seu nome
    idade = "14" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/pai")
def home():

    nome = "Pai" # escreva seu nome
    idade = "42" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)
# defina a rota para a página da mãe
@app.route("/mãe")
def home():

    nome = "Mãe" # escreva seu nome
    idade = "44" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)
# defina a rota para a página do amigo
@app.route("/amigo")
def home():

    nome = "Amigo" # escreva seu nome
    idade = "14" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)







# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
