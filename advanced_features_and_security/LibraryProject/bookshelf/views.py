from django.shortcuts import redirect, render
from django.contrib.auth.decorators import permission_required
from django.template.context_processors import request
from .models import Book
from .forms import BookForm

# Create your views here.

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/bookshelf/view/')
    else:
        form = BookForm()

    context = {'form': form}
    return render(request, 'bookshelf/add_book.html', context)

@permission_required('bookshelf.can_edit', raise_exception=True)
def update_book(request, id):
    book = Book.objects.get(pk = id)
    if request.method == "POST":
        form = BookForm(request.POST, instance= book)
        if form.is_valid():
            form.save()
            return redirect('/bookshelf/view/')
        
    else:
        form = BookForm(instance= book)

    context = {'form': form}
    return render(request, 'bookshelf/update_book.html', context)

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, id):
    book = Book.objects.get(pk = id)
    if request.method == "POST":
        book.delete()
        return redirect('/bookshelf/view/')
    
    return render(request, 'bookshelf/delete_book.html')

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    context =  {'books': books}

    return render(request, 'bookshelf/view_book.html', context)