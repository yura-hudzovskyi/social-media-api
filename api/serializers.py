from rest_framework import serializers

from api.models import Post, Hashtag


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ("id", "name")


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "message", "created_at", "hashtags", "user")
        read_only_fields = ("created_at", "user")
