from importlib.resources import path
from flask_restx import Resource, reqparse, Api, api
from models.book import BookModel, bookes
from app import api, app
import sqlite3
       

#comando que faz a requisição de parametros
path_params= reqparse.RequestParser()
path_params.add_argument('book_name', type=str)
path_params.add_argument('book_note', type=float)
path_params.add_argument('author', type=str)
path_params.add_argument('book_type', type=str)
path_params.add_argument('limit', type=float)
path_params.add_argument('offset', type=float)


class Livros(Resource):
    #função que puxa os livros que foram salvos
    def get(self):                                #SELECT * FROM books  
        return {'Books': [book.json() for book in BookModel.query.all()]}

class Livro(Resource):
    #dados passados
    argumentos= reqparse.RequestParser()
    argumentos.add_argument('book_name', type=str, required=True, help="The field 'book_name' cannot be left blink.")
    argumentos.add_argument('book_note', type=float, required=True, help="The field 'book_note' cannot be left blink.")
    argumentos.add_argument('book_author', type=str)
    argumentos.add_argument('book_type', type=str)

    #pega todos os livros cadastrados
    @api.marshal_list_with(bookes)
    def get(self, book_id):
        livros= BookModel.find_book(book_id)
        if livros:
            return livros.json()
        return {'Message': 'Book not found.'} , 404

    #adiciona um novo livro
    def post(self, book_id):
        if BookModel.find_book(book_id):
            return {f"Message": "Book id '{book_id}' already exists."}, 400 #BAD REQUEST
        dados= Livro.argumentos.parse_args()
        book= BookModel(book_id, **dados)
        try:
            book.save_book()
        except:
            return {'Message':'An internal error ocurred trying to save book.'}, 500 #internal server error    
        return book.json()
      
    #fazer alterações no livro selecionado se não existir ele adiocna
    def put(self, book_id):
        dados= Livro.argumentos.parse_args()
        livro_encontrado= BookModel.find_book(book_id)
        if livro_encontrado:
            #se não existir o livro ele atualizar e cria um novo livro
           livro_encontrado.update_book(**dados) 
           livro_encontrado.save_book()
           return livro_encontrado.json(), 200
        book= BookModel(book_id, **dados)  
        try:
            book.save_book()
        except:
            return {'Message':'An internal error ocurred trying to save book.'}, 500     
        return book.json(), 201 #CREATED   
        
    #deleta o livro selecionado 
    def delete(self, book_id):
        livros= BookModel.find_book(book_id)
        if livros:
            try:
                livros.delete_book()
            except:
                return {'Message':'An internal error ocurred trying to delete book.'}, 500     
            return {'Message': 'Book Deleted.'}
        return {'Message': 'Book not found.'} , 404    
        


