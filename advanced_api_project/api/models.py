from django.db import models

# Create your models here.


class Author(models.Model):

    """
    Author model representing a book author.
    
    Attributes:
        name (CharField): The full name of the author (max 100 characters)
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):

    """
    Book model representing a published book.
    
    Attributes:
        title (CharField): The title of the book (max 200 characters)
        publication_year (IntegerField): The year the book was published
        author (ForeignKey): Reference to the Author who wrote the book
                             Implements a one-to-many relationship (Author → Books)
    """
     
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
    
    class Meta:
        unique_together = ['title', 'author']