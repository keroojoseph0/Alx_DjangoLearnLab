from django.urls import path, include
from . import views

app_name = 'api'

urlpatterns = [
    path('books/', views.BookList.as_view(), name='book-list'),  # Maps to the BookList view
]
