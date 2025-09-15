from relationship_app.models import Author, Library, Book


def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books


def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian  # thanks to related_name="librarian"