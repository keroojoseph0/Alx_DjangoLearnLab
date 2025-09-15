from .models import Book, Librarian, Library, Author

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return author.books.all()  # thanks to related_name="books"
    except Author.DoesNotExist:
        return []


# 2. List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()  # ManyToManyField -> use .all()
    except Library.DoesNotExist:
        return []


# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian  # OneToOneField -> direct relation
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None