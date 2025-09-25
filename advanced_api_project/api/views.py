"""
Book API Views Configuration
This module provides CRUD operations for Book model using Django REST Framework's generic views.
Includes advanced filtering, search, ordering, and custom business logic.
"""


from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from rest_framework import filters, permissions
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class BookListView(ListView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'author', 'publication_year']

class BookDetailView(DetailView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookCreateView(CreateView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def  perform_create(self, serializer):
        serializer.save(onwer = self.request.user)

class BookUpdateView(UpdateView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()
class BookDeleteView(DeleteView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]