from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "image")


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "email",
            "password",
            "is_staff",
            "image",
            "bio",
            "followers",
            "following",
        )
        read_only_fields = ("is_staff", "followers", "following")
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, set the password correctly and return it"""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()

        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "email", "followers", "following")
        read_only_fields = ("id", "email", "image", "bio")


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "email", "image", "bio", "followers", "following")
        read_only_fields = ("id", "email", "image", "bio", "followers", "following")
