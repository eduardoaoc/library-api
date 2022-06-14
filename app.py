from flask import Flask
from flask_restful import  Api
from resource.book import Livros
from models.book import BookModel

app= Flask(__name__)

#caminho banco de dados
app.config['SQLACHEMY_DATABASE_URI']= 'sqlite:///libray.db'


api= Api(app)

#depois da primeira requisição cria um banco de dados para nunca iniciar sem
@app.before_first_request
def criar_banco():
    banco.create_all()

@app.route('/')
def index():
    return {'status': 'Running server.'}

api.add_resource(Livros, '/books') 

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
