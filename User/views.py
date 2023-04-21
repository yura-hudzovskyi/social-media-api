from django.contrib.auth import get_user_model
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
    queryset = get_user_model().objects.all()
    authentication_classes = (authentication.JWTAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


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
