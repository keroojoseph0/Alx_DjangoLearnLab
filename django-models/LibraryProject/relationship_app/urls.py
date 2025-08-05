from django.urls import path, include
from .views import list_books, LibraryDetailView, register
from django.contrib.auth import views as auth_views

app_name = 'relationship_app'

urlpatterns = [
    path('', list_books, name="book_list"),
    path('library/<int:pk>', LibraryDetailView.as_view(), name = 'library_list'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),
]