from django.urls import path
from .views import list_books, LibraryDetailView, BookList
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'relationship_app'

urlpatterns = [
    path('booklist', list_books, name='booklist'),
    path('books', BookList.as_view(), name='books'),
    path('library', LibraryDetailView.as_view(), name='library'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]
