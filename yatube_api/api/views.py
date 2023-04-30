from django.shortcuts import get_object_or_404
from posts.models import Group, Post
from rest_framework import status, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, serializer):
        post = self.get_object()
        if post.author != self.request.user:
            raise PermissionDenied('Cannot change comment of another user')
        return super().perform_destroy(serializer)

    def perform_update(self, serializer):
        post = self.get_object()
        if post.author != self.request.user:
            raise PermissionDenied('Cannot change comment of another user')
        serializer.save(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        return post.comments.all()

    def perform_destroy(self, serializer):
        comment = self.get_object()
        if comment.author != self.request.user:
            raise PermissionDenied('Cannot change comment of another user')
        return super().perform_destroy(serializer)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def perform_update(self, serializer):
        comment = self.get_object()
        if comment.author != self.request.user:
            raise PermissionDenied('Cannot change comment of another user')
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def create(self, response):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
