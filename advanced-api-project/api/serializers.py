from rest_framework import serializers
from .models import Book, Author

# Author serializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

# Book serializer
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True, read_only=True)
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    def validate_publication_year(self, value):
            if value > 2025:
                raise serializers.ValidationError("Publication year cannot be in the future.")
            return value
