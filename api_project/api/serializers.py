from django.forms import fields
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.Serializer):
    class Meta:
        models = Book
        fields = '__all__'