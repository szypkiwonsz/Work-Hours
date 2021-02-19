from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model."""
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Function needed to properly hash the password.
        user = User(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, attrs):
        # Function needed to check if two passwords match.
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "password fields didn't match."})
        return attrs
