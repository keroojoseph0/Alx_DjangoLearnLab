from django.urls import path, include
from . import views

app_name = 'relationship_app'

urlpatterns = [
    path('', views.book_list, name="book_list"),
    path('library/<int:pk>', views.LibraryList.as_view(), name = 'library_list'),
]