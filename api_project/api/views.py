# Permissions in Views
# ------------------------------------------------
# By default, only authenticated users can access this view due to global settings.
# If you need role-based control, use permission_classes at the view level.
# Example: Only admins can access a certain API.

from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]