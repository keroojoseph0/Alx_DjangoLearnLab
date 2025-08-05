from django.shortcuts import get_object_or_404, redirect, render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test, permission_required
from .utils import is_admin, is_librarian, is_member
from .forms import BookForm

def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.userprofile.role = 'Member'
            user.userprofile.save()
            login(request, user)  # log the user in after registration
            return redirect('relationship:book_list')  # replace 'home' with the name of your landing page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {})

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {})

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {})

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relationship:book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_create.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def update_book(request, id):
    book = Book.objects.get(id = id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if  form.is_valid():
            form.save()
            return redirect('relationship:book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_update.html', {'form': form})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.delete()
        return redirect('relationship:book_list')
    return render(request, 'relationship_app/book_delete.html', {'book': book})