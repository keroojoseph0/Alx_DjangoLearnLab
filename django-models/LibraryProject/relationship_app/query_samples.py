from .models import Book, Librarian, Library, Author

authors = Author.objects.all()
book_by_auher = authors.books.alll()

librarys = Library.objects.all()
book_in_library = librarys.books.all()


librarian_in_library = librarys.librarian
