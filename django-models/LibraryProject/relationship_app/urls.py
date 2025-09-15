from django.urls import path
from .views import list_books, LibraryDetailView, BookList, signupview

app_name = 'relationship_app'

urlpatterns = [
    path('booklist', list_books, name='booklist'),
    path('books', BookList.as_view(), name='books'),
    path('library', LibraryDetailView.as_view(), name='library'),
    path('signup', signupview, name='signup'),
]
