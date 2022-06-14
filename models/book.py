from sql_alchemy import banco


class BookModel(banco.Model):
    __tablename__= 'books'

    book_id= banco.Column(banco.String, primary_key=True)
    book_name= banco.Column(banco.String)
    book_note= banco.Column(banco.Float(precision=1))
    book_author= banco.Column(banco.String(40))
    book_type= banco.Column(banco.String(40))

    def __init__(self, book_id, book_name, book_note, book_author, book_type):
        self.book_id= book_id
        self.book_name= book_name
        self.book_note= book_note
        self.book_author= book_author
        self.book_type= book_type

    def json(self):
        return {
            'book_id': self.book_id,
            'book_name': self.book_name,
            'book_note': self.book_note,
            'book_author': self.book_author,
            'book_type': self.book_type
        }    


