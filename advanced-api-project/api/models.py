from django.db import models

# Author model
# Purpose: Represents an author who writes books. Stores basic information about the author.
# Usage: Used to associate books with their respective authors via a foreign key relationship.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# Book model
# Purpose: Represents a book written by an author. Stores details like title, publication year, and author.
# Usage: Used to store book data and link each book to an author through a foreign key.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title