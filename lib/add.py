from sqlalchemy.orm import sessionmaker
from main import engine, Book  

Session = sessionmaker(bind=engine)
session = Session()

def add_book(title, author, isbn, publication_date, description, publisher, language, pages_count, rating):
    new_book = Book(
        title=title,
        author=author,
        isbn=isbn,
        publication_date=publication_date,
        description=description,
        publisher=publisher,
        language=language,
        pages_count=pages_count,
        rating=rating
    )
    session.add(new_book)
    session.commit()