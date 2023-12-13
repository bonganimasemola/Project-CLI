from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Book,Author,Genre

if __name__ == '__main__':
    engine=create_engine("sqlite:///book.db")
    Session=sessionmaker(bind=engine)
    session=Session()

    # session.query(Book).delete()
    # session.query(Author).delete()
    # session.query(Genre).delete()
    
    book1 = Book(title='The Shadow of the Wind', author='Carlos Ruiz Zafón', isbn=9780143034902, publication_date='2004-04-12', description='A mesmerizing literary thriller.', publisher='Penguin Books', language='English', pages_count=487, rating=4)
    book2 = Book(title='1984', author='George Orwell', isbn=9780451524935, publication_date='1949-06-08', description='A dystopian novel.', publisher='Signet Classic', language='English', pages_count=328, rating=5)
    book3 = Book(title='To Kill a Mockingbird', author='Harper Lee', isbn=9780061120084, publication_date='1960-07-11', description='A classic of modern American literature.', publisher='Harper Perennial Modern Classics', language='English', pages_count=336, rating=4)
    book4 = Book(title='The Great Gatsby', author='F. Scott Fitzgerald', isbn=9780743273565, publication_date='1925-04-10', description='An exploration of decadence and idealism.', publisher='Scribner', language='English', pages_count=180, rating=5)
    book5 = Book(title='Pride and Prejudice', author='Jane Austen', isbn=9780141439518, publication_date='1813-01-28', description='A romantic novel of manners.', publisher='Jungle',language='japanese',pages_count=200,rating=7)

    author1 = Author(name='Carlos Ruiz Zafón', best_seller='The Shadow of the Wind')
    author2 = Author(name='George Orwell', best_seller='1984')
    author3 = Author(name='Harper Lee', best_seller='To Kill a Mockingbird')
    author4 = Author(name='F. Scott Fitzgerald', best_seller='The Great Gatsby')
    author5 = Author(name='Jane Austen', best_seller='Pride and Prejudice')
    

    genre = Genre(name='Fantasy')
    genre = Genre(name='Mystery')
    genre = Genre(name='Romance')
    genre = Genre(name='Science Fiction')
    genre = Genre(name='Thriller')


    session.add_all([author1, author2, author3, author4, author5, book1, book2, book3, book4, book5, genre1, genre2, genre3, genre4, genre5])
    session.commit()
