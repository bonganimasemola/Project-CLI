from sqlalchemy.orm import sessionmaker
from main import engine, Book  

Session = sessionmaker(bind=engine)
session = Session()

def delete_book(title):
    book_to_delete = session.query(Book).filter(Book.title == title).first()
    if book_to_delete:
        session.delete(book_to_delete)
        session.commit()