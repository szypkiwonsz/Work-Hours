import pytest

from users.models import User
from users.serializers import UserCreateSerializer


# fixtures for test_models
@pytest.fixture()
def user(db):
    user = User.objects.create(
        email='test@email.com',
        password='test_password'
    )
    return user


# fixtures for test_serializers
@pytest.fixture()
def user_create_serializer_data():
    user_create_serializer_data = {
        'email': 'test@email.com',
        'password': 'test_password',
        're_password': 'test_password'
    }
    return user_create_serializer_data


@pytest.fixture()
def user_create_serializer(db, user_create_serializer_data):
    return UserCreateSerializer(data=user_create_serializer_data)
