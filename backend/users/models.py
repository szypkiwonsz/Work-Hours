from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    """Override class to be able to correctly use user registration from DJOSER without a username."""

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('user must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email)

        user.set_password(password)
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom model of user without username (uses email instead)."""
    email = models.EmailField(unique=True)  # change email to unique and blank to false
    is_active = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # removes email from REQUIRED_FIELDS

    def __str__(self):
        return self.email
