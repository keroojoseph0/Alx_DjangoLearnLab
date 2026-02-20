from django.urls import path
from .views import LoginView, ProfileView, SignupView

app_name = 'accounts'


urlpatterns = [
    path('register/', SignupView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('users/<int:user_id>/follow/', ProfileView.as_view(), name='follow'),
    path('users/<int:user_id>/unfollow/', ProfileView.as_view(), name='unfollow'),
]