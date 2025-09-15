from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic import ListView
from django.views.generic.detail import DetailView


# Create your views here.

def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


class BookList(ListView):
    model = Library
    queryset = Library.objects.all()
    template_name = 'relationship_app/list_books.html'
    context_object_name = 'books'

class LibraryDetailView(DetailView):
    model = Library
    context_object_name = 'library'
    queryset = Library.objects.all()
    template_name = 'relationship_app/library_detail.html'
