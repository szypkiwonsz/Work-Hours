import pytest
from django.db import IntegrityError

from users.models import User


@pytest.mark.users_models
class TestCustomUserManager:

    def test_create_user(self, db):
        user = User.objects.create_user(
            email='test@email.com',
            password='test_password'
        )
        assert user

    def test_create_user_without_email(self, db):
        with pytest.raises(TypeError):
            User.objects.create_user(
                password='test_password'
            )


@pytest.mark.users_models
class TestUser:

    def test_string_representation(self, user):
        assert str(user) == 'test@email.com'

    def test_is_active(self, user):
        assert not user.is_active

    def test_username_field_is_email(self, user):
        assert user.USERNAME_FIELD == 'email'

    def test_email_uniques(self, user):  # fixture user already create a user object with same email
        with pytest.raises(IntegrityError):
            User.objects.create(
                email='test@email.com',
                password='test_password'
            )
