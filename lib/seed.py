from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Book, Author, Genre

if __name__ == '__main__':
    engine = create_engine("sqlite:///book.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Delete existing records before any insertion
    session.query(Book).delete()
    session.query(Author).delete()
    session.query(Genre).delete()

    # Create instances for each class
    books = [
        Book(title='The Great Gatsby', isbn=9780743273565,
             publication_date='1925-04-10', description='Classic novel about the American Dream',
             publisher='Scribner', language='English', pages_count=180, rating=4),

        Book(title='To Kill a Mockingbird', isbn=9780061120084,
             publication_date='1960-07-11', description='Powerful story on racial injustice',
             publisher='Harper Perennial Modern Classics', language='English', pages_count=281, rating=5),

        Book(title='1984', isbn=9780451524935,
             publication_date='1949-06-08', description='Dystopian vision of a totalitarian future',
             publisher='Signet Classics', language='English', pages_count=328, rating=4),

        Book(title='Pride and Prejudice', isbn=9780141439518,
             publication_date='1813-01-28', description='Classic romance novel',
             publisher='Penguin Classics', language='English', pages_count=279, rating=4),

        Book(title='The Catcher in the Rye', isbn=9780316769488,
             publication_date='1951-07-16', description='Coming-of-age novel',
             publisher='Back Bay Books', language='English', pages_count=224, rating=3)
    ]

    authors = [
        Author(name='F. Scott Fitzgerald', best_seller='The Great Gatsby'),
        Author(name='Harper Lee', best_seller='To Kill a Mockingbird'),
        Author(name='George Orwell', best_seller='1984'),
        Author(name='Jane Austen', best_seller='Pride and Prejudice'),
        Author(name='J.D. Salinger', best_seller='The Catcher in the Rye')
    ]

    genres = [
        Genre(name='Fiction'),
        Genre(name='Classic'),
        Genre(name='Dystopian'),
        Genre(name='Romance'),
        Genre(name='Coming-of-age')
    ]

    # Add instances to the session
    session.add_all(books + authors + genres)

    # Commit the changes
    session.commit()
    
    for i in range(5):
        books[i].author = authors[i]
        books[i].genre = genres[i]


    session.commit()