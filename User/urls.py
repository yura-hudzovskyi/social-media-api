from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from User.views import (
    CreateUserView,
    ManageUserView,
    UserListView,
    UserDetailView,
    followToggle,
    UserFollowersView,
    UserFollowingView,
)

app_name = "User"
urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("me/", ManageUserView.as_view(), name="me"),
    path("list/", UserListView.as_view(), name="list"),
    path("list/<int:pk>/", UserDetailView.as_view(), name="list"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("follow/<int:pk>/", followToggle, name="follow"),
    path("followers/", UserFollowersView.as_view(), name="followers"),
    path("following/", UserFollowingView.as_view(), name="following"),
]
