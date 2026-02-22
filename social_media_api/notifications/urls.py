from django.urls import path
from .views import NotificationListView, MarkNotificationAsRead


app_name = 'notifications'

urlpatterns = [
    path("notifications/", NotificationListView.as_view()),
    path("notifications/<int:pk>/read/", MarkNotificationAsRead.as_view()),
]