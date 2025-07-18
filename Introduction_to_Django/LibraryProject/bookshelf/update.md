# Update the Book Title

## Command
```python
from myapp.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
```

## Expected Output
```python
# The command updates the book title and saves it to the database.
# Printing the title confirms the update:
Nineteen Eighty-Four
```