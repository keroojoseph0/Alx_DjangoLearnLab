from django.urls import path, include
from . import views
from bookshelf.views import list_books

app_name = 'bookshelf'

urlpatterns = [
    path('', views.book_list, name = 'list_books'),
    path('add_book/', views.create_book, name = 'add'),
    path('edit_book/<int:id>', views.edit_book, name = 'update'),
    path('delete/<int:id>', views.delete_book, name = 'delete'),
]
