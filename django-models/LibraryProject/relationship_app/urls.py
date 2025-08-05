from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'relationship_app'

urlpatterns = [
    path('', views.list_books, name="book_list"),
    path('library/<int:pk>', views.LibraryDetailView.as_view(), name = 'library_list'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),

    path('add/', views.add_book, name = 'add'),
    path('update/<int:id>', views.update_book, name = 'update'),
    path('delete/<int:id>', views.delete_book, name = 'delete'),
]