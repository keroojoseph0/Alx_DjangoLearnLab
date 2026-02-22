from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class NotificationListView(ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(
            recipient=self.request.user
        )
    
class MarkNotificationAsRead(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        notification = Notification.objects.get(
            id=pk,
            recipient=request.user
        )

        notification.is_read = True
        notification.save()

        return Response({"message": "Marked as read"})