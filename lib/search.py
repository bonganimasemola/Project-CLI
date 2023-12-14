from sqlalchemy.orm import sessionmaker
from main import engine, Book 

Session = sessionmaker(bind=engine)
session = Session()

def search_by_title(title):
    return session.query(Book).filter(Book.title == title).all()

def search_by_author(author):
    return session.query(Book).filter(Book.author == author).all()