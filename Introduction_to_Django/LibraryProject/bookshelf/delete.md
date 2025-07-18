# Delete the Book Instance

## Command
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
print(Book.objects.all())
```

## Expected Output
```python
# The command deletes the book from the database.
# Retrieving all books confirms the deletion:
<QuerySet []>
```
