from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic import ListView, DetailView

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryList(DetailView):
    model = Library
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context