# Retrieve the Book Instance

## Command
```python
from myapp.models import Book
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
```

## Expected Output
```python
# The command retrieves the book and displays its attributes:
1984 George Orwell 1949
```