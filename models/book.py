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
    @classmethod
    def find_book(cls, book_id):
        #SELECT * FROM books WHERE book_id = book_id
        book= cls.query.filter_by(book_id=book_id).first()
        if book:
            return book
        return None

    def save_book(self):    
        banco.session.add(self) #adiciona o objeto ao banco
        banco.session.commit()    

    def update_book(self, book_name, book_note, book_author, book_type):
        self.book_name= book_name
        self.book_note= book_note
        self.book_author= book_author
        self.book_type= book_type

    def delete_book(self ):
        banco.session.delete(self)
        banco.session.commit()

