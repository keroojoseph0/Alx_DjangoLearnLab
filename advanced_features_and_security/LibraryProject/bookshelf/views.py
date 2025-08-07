from django.shortcuts import get_object_or_404, redirect, render
from .forms import BookForm
from .forms import ExampleForm
from .models import Book
from django.contrib.auth.decorators import permission_required
# Create your views here.

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookshelf:list_books')
    else:
        form = BookForm()
    return render(request, 'bookshelf/create_book.html', {'form': form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, id):
    book = Book.objects.get(id = id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if  form.is_valid():
            form.save()
            return redirect('bookshelf:list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.delete()
        return redirect('bookshelf:list_books')
    return render(request, 'bookshelf/delete_book.html', {'book': book})

def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'bookshelf/book_list.html', context)