from posts.models import Comment, Group, Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True,
                                          required=False,
                                          default=serializers.
                                          CurrentUserDefault())

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        read_only_fields = ('author',)
        model = Post


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True,
                                          required=False,
                                          default=serializers.
                                          CurrentUserDefault())
    post = serializers.SlugRelatedField(slug_field='id', read_only=True)

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment
        read_only_fields = ('author',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group
