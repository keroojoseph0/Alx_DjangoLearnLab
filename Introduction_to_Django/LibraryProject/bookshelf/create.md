# Create a Book Instance

## Command
```python
from myapp.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

## Expected Output
```python
# The command creates a Book instance with the specified attributes.
# No direct output is displayed in the shell, but the book is saved to the database.
# You can verify by printing the object:
print(book)
# Expected: <Book: 1984 by George Orwell (1949)>
```