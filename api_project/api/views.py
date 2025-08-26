from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework  import generics
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework import permissions

# Create your views here.

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Permissions:
    # -------------------------
    # Permissions decide *what* an authenticated user can do.
    # By default, only authenticated users can access the API.
    # If you want to allow public read-only access, you can switch to:
    # 'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    #
    # Example:
    # - IsAuthenticated      → Only logged-in users with a token can access.
    # - AllowAny             → Public, no restrictions.
    # - IsAdminUser          → Only staff users (is_staff=True) can access.
    
    permission_classes = [permissions.IsAdminUser]  # Ensure that only admin users can access this view