from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from rest_framework import generics, permissions
from rest_framework_simplejwt import authentication

from User.serializers import UserSerializer, UserListSerializer, UserDetailSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""

    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""

    serializer_class = UserSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user


class UserListView(generics.ListAPIView):
    """List all users"""

    serializer_class = UserListSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        params = self.request.query_params
        queryset = get_user_model().objects.all()
        if params.get("username"):
            queryset = queryset.filter(username=params.get("username"))
        return queryset


class UserDetailView(generics.RetrieveAPIView):
    """Detail user"""

    serializer_class = UserDetailSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        params = self.request.query_params
        queryset = get_user_model().objects.all()
        if params.get("id"):
            queryset = queryset.filter(id=params.get("id"))
        return queryset


def followToggle(request, pk=None):
    author = get_user_model().objects.get(pk=request.user.pk)
    current_user = get_user_model().objects.get(pk=pk)
    following = author.following.all()

    if author != current_user:
        if current_user in following:
            author.following.remove(current_user.id)
        else:
            author.following.add(current_user.id)
    return redirect("User:list")


class UserFollowersView(generics.ListAPIView):
    """List of all followers of user"""

    serializer_class = UserListSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = self.request.user.followers.all()
        return queryset


class UserFollowingView(generics.ListAPIView):
    """List of all user`s following"""

    serializer_class = UserListSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        queryset = self.request.user.following.all()
        return queryset
