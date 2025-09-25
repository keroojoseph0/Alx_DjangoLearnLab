"""
Serializers for the API application.

This module defines serializers that handle conversion between 
Author/Book model instances and JSON data, including validation
and relationship handling.
"""

from rest_framework import serializers
from .models import Book, Author
from django.utils import timezone

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', ]

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many = True, read_only = True)

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    def validate_publication_year(self, value):
        current_year = timezone.now().year

        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future. Current year is {current_year}."
            )
        return value
