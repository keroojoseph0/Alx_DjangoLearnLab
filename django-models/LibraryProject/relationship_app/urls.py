from django.urls import path
from . import views

urlpatterns = [
    path('booklist', views.list_books, name='booklist'),
    path('books', views.BookList.as_view(), name='books'),
]
