from relationship_app.models import Author, Library


def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()  # uses related_name="books"
    return books


def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian  # thanks to related_name="librarian"