from django.urls import path
from . import views

app_name = 'bookshelf'

urlpatterns = [
    path('add/', views.add_book, name= 'add'),
    path('update/<int:id>', views.update_book, name='update'),
    path('delete/<int:id>', views.delete_book, name= 'delete'),
    path('view/', views.view_book, name='view'),
]
