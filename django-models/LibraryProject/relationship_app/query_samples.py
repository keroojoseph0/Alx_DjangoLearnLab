from .models import Book, Librarian, Library, Author

book_by_auher = Book.objects.filter(auhor__name = 'keroo')
book_all = Book.objects.all()
book_in_library = Library.objects.filter(books = book_all)
library_all = Library.objects.all()
librarian_in_library = Librarian.objects.filter(library = library_all)
