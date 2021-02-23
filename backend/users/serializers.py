from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

User = get_user_model()


class UserCreateSerializer(BaseUserRegistrationSerializer):
    """Override class of UserCreateSerializer from DJOSER to create user only with email."""

    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = ('email', 'password')
