from math import perm
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .serializers import ProfileSerializer, RegisterSerializer, LoginSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action

# Create your views here.

class SignupView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})

        return Response({"error": "Invalid credentials"}, status=400)
    


class ProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user


    @action(detail=True, methods=['post'])
    def follow(self, request, pk=None):
        follow_user = self.get_object()
        if follow_user == request.user:
            return Response({"error": "You cannot follow yourself"}, status=400)
        
        request.user.following.add(follow_user)
        return Response({"status": f"You are now following {follow_user.username}"})
    
    @action(detail=True, methods=['post'])
    def unfollow(self, request, pk=None):
        user_to_unfollow = self.get_object()
        if user_to_unfollow == request.user:
            return Response({"error": "You cannot unfollow yourself"}, status=400)
        
        request.user.following.remove(user_to_unfollow)
        return Response({"status": f"You have unfollowed {user_to_unfollow.username}"})


