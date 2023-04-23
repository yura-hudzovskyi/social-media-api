from rest_framework import viewsets

from api.models import Post, Hashtag
from api.serializers import PostSerializer, HashtagSerializer


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all().prefetch_related("hashtags")

        hashtags = self.request.query_params.get("hashtags", None)

        # show only following users and own posts
        following = self.request.user.following.all()
        following = [user.pk for user in following]
        following.append(self.request.user.pk)
        queryset = queryset.filter(user__pk__in=following)

        if hashtags is not None:
            queryset = queryset.filter(hashtags__name__in=hashtags.split(","))

        return queryset.filter(user__pk__in=[self.request.user.pk])

    # create a post on behalf of the user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HashtagView(viewsets.ModelViewSet):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer
