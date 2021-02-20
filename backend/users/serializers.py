from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers

from users.models import User


class UserSerializer(BaseUserRegistrationSerializer):
    """Serializer for User model."""
    password2 = serializers.CharField(write_only=True)

    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = ('email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        """Function needed to check if two passwords match."""
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "password fields didn't match."})
        return attrs
