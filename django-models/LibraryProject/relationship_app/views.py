from django.shortcuts import render
from .models import Book, Library
from django.views.generic import ListView, DetailView


# Create your views here.

def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'list_books.html', context)


class BookList(ListView):
    model = Library
    queryset = Library.books.all()
    template_name = 'list_books.html'
    context_object_name = 'books'

class LibraryDetailView(DetailView):
    model = Library
    context_object_name = 'library'
    queryset = Library.objects.all()
    template_name = 'library_detail.html'
