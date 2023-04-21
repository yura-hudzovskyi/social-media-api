from django.db import models


class Hashtag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    @property
    def post_set(self):
        return self.post_set.all()

    @property
    def post_count(self):
        return self.post_set.count()


class Post(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True)

    def __str__(self) -> str:
        return self.message
