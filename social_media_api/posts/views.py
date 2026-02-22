from calendar import c
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType


from posts.models import Like


# Create your views here.

class PostPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class CommentPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['content']
    pagination_class = PostPagination


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['content']
    pagination_class = CommentPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class FeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['content']
    pagination_class = PostPagination

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')


class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like, created = Like.objects.get_or_create(post=post, user=request.user)

        if not created:
            return Response(
                {"message": "You already liked this post."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create Notification
        if post.author != request.user:
            post_type = ContentType.objects.get_for_model(Post)

            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked",
                content_type=post_type,
                object_id=post.id
            )

        return Response({"message": "Post liked successfully."})



class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)

        like = Like.objects.filter(
            user=request.user,
            post=post
        ).first()

        if not like:
            return Response(
                {"message": "You have not liked this post."},
                status=status.HTTP_400_BAD_REQUEST
            )

        like.delete()

        return Response({"message": "Post unliked successfully."})
