import click

# Mock database (for demonstration purposes)
books = [
    {"title": "Book 1", "author": "Author A"},
    {"title": "Book 2", "author": "Author B"},
    {"title": "Book 3", "author": "Author C"},
]


@click.group()
def cli():
    pass


@cli.command()
@click.argument("title")
@click.argument("author")
def add(title, author):
    """
    Add a new book.
    """
    books.append({"title": title, "author": author})
    click.echo(f"Added book: {title} by {author}")


@cli.command()
@click.argument("title")
def delete(title):
    """
    Delete a book.
    """
    for book in books:
        if book["title"] == title:
            books.remove(book)
            click.echo(f"Deleted book: {title}")
            return
    click.echo(f"Book '{title}' not found.")


@cli.command()
@click.option("--title", help="Title of the book")
@click.option("--author", help="Author of the book")
def search(title, author):
    """
    Search for books by title or author.
    """
    if title:
        found_books = [book for book in books if book["title"] == title]
        if found_books:
            click.echo(f"Books with title '{title}':")
            for book in found_books:
                click.echo(f"- {book['title']} by {book['author']}")
        else:
            click.echo(f"No books found with title '{title}'.")
    elif author:
        found_books = [book for book in books if book["author"] == author]
        if found_books:
            click.echo(f"Books by author '{author}':")
            for book in found_books:
                click.echo(f"- {book['title']} by {book['author']}")
        else:
            click.echo(f"No books found by author '{author}'.")
    else:
        click.echo("Please provide title or author for search.")


if __name__ == "__main__":
    cli()
