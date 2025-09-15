from django.shortcuts import redirect, render
from .models import Book
from .models import Library
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .forms import SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm



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

def signupview(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('/relationship/books')
    else:
       form = SignupForm()
    
    context = {'form': form}
    return render(request, 'regisration/register.html', context)