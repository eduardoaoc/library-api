from flask import Flask, request
from flask_restx import  Api, api 
from resource.book import Livros, Livro
from models.book import BookModel


app= Flask(__name__)
api= Api(app)

#caminho banco de dados
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///libray.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

#depois da primeira requisição cria um banco de dados para nunca iniciar sem
@app.before_first_request
def criar_banco():
    banco.create_all()

@app.route('/')
def index():
    return {'status': 'Running server.'}


api.add_resource(Livros, '/books') 
api.add_resource(Livro, '/books/<string:book_id>') 



if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
