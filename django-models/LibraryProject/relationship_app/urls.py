from django.urls import path, include
from .views import list_books, LibraryDetailView

app_name = 'relationship_app'

urlpatterns = [
    path('', list_books, name="book_list"),
    path('library/<int:pk>', LibraryDetailView.as_view(), name = 'library_list'),
]