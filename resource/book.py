from flask_restful import Resource, Api, reqparse
import sqlite3

livros= ({'book_id':'01',
          'book_name':'O NOSSO LAR',
          'book_note': '9.5',
          'book_author':'Lincol Calabassa',
          'book_type':'Romance'})

class Livros(Resource):
    #função que puxa os livros que foram salvos
    def get(self):
        return livros
        #connection= sqlite3.connect('library.db')
        #cursor= connection.cursor()

    def post(self, book_id):
        pass

    def put(self, book_id):
        pass

    def delete(self, book_id):
        pass


