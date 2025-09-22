from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# Authentication Endpoints
# ------------------------------------------------
# We include a token authentication endpoint provided by DRF:
# POST /api/token-auth/
# Request Body: { "username": "<your_username>", "password": "<your_password>" }
# Response: { "token": "<user_token>" }
#
# This token must be used in all future API requests to prove authentication.

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
    path('api-token-auth/', views.obtain_auth_token)
]