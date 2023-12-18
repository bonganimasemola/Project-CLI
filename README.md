# Book Manager Project Documentation

## Problem Statement

Managing a collection of books can be a challenging task, especially as the collection grows. Keeping track of book details, such as titles, authors, and publication dates, manually can lead to errors and inefficiencies. There is a need for a tool that allows users to efficiently manage their book collections, enabling tasks such as adding new books, deleting books, and searching for specific books.

## Solution

The proposed solution is to develop a Command Line Interface (CLI) application for book management. The application will leverage the power of SQLAlchemy for the backend, providing a robust and efficient way to interact with a database to store and retrieve book information. The front end of the application will be built using Python, offering a user-friendly CLI for seamless interaction.

## Features:

1. Add Books: Users can add new books to the collection by providing details such as title, author, publication date, and any additional relevant information.

2. Delete Books: The application allows users to remove books from the collection, helping to keep the database up-to-date.

3. Search Books: Users can search for books based on various criteria, such as title, author, or publication date, making it easy to find specific books within the collection.

## Setup

### Clone the Repository

1.  Clone the repository using Git:
    
    bashCopy code
    
    `git clone https://github.com/your-username/book-manager.git` 
    

### Installation

#### Prerequisites

-   Python 3.x
-   Pip (Python package installer)
-   SQLite or an alternate SQL database

#### Steps

1.  Navigate to the project directory:
    
    
    `cd book-manager` 
    
2.  Create a virtual environment (optional but recommended):
    
    
    `python -m venv venv` 
    
3.  Activate the virtual environment (if created):
    
    -   Windows:
        
       
        
        `venv\Scripts\activate` 
        
    -   macOS and Linux:
        
      
        
        `source venv/bin/activate` 
        
4.  Install project dependencies:
    
    
    
    `pip install -r requirements.txt` 
    
5.  Create the initial database and seed data:
    
 
    
    `python seed.py` 
    

## File Structure


`
book-manager/
│
├── alembic.ini
├── book.db
├── book_manager.py
├── database/
│   ├── book_manager.db
│   ├── temp_db.db
│   └── tempfile.sql
├── main.py
├── migrations/
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions/
│       ├── 014a007cc6b4_retry.py
│       ├── 364d1300f164_another_retry.py
│       ├── 73c0d59701a0_retry.py
│       └── a3dfa8d76a57_first_atempt_in_table_insertion_with_no_.py
├── __pycache__/
│   └── main.cpython-310.pyc
└── seed.py
` 

## Usage

### Commands

#### Adding a Book

To add a book to the database, use the following command:



`python book_manager.py add "Title of the Book" "Author Name" "Genre Name"` 

#### Deleting a Book

To delete a book from the database, use the following command:



`python book_manager.py delete "Title of the Book"` 

#### Searching for Books

To search for books by title or author, use the following command:



`python book_manager.py search "Search Term"` 

## Future Considerations

As the project evolves, several features and improvements can be considered for future development:

1. User Authentication: Implement user authentication to ensure that only authorized users can manage the book collection.

2. Advanced Search Options: Enhance the search functionality to support more advanced queries, such as searching for books within a specific genre or by a particular author.

3. Data Validation: Implement robust data validation mechanisms to ensure that the entered information is accurate and follows a predefined structure.

4. Export/Import Functionality: Allow users to export their book collection to a file and import it back, facilitating data backup and migration.

## Minimum Viable Product (MVP)

The Minimum Viable Product for the Book Manager application will include the following core features:

1. CLI for basic interaction.
2. Add, delete, and search functionality.
3. Backend powered by SQLAlchemy for data storage and retrieval.

## Technologies

### Backend:

SQLAlchemy: To interact with the database and manage book-related data.
Python: The primary language for backend development, providing a powerful and flexible environment.

### Frontend:

-Python/CLI: Building a command line interface for user interaction.

## Conclusion

The Book Manager project aims to provide a simple yet effective solution for managing book collections. By leveraging the capabilities of SQLAlchemy and Python, the application will offer users a seamless experience for adding, deleting, and searching for books in their collections. As the project progresses, additional features can be incorporated to enhance functionality and user experience.


# Author(s)/ Coders(s):
  Conrad Kambi https://github.com/conokisekai
  Jim Otieno https://github.com/jimotieno475
  Stanley Kimambo https://github.com/SkimZconceited
  bonganimasemola https://github.com/bonganimasemola
