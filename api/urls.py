from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import PostView, HashtagView

router = DefaultRouter()
router.register("posts", PostView, basename="post")
router.register("hashtags", HashtagView, basename="hashtag")

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),
]
