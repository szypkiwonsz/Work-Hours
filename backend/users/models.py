from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUserManager(UserManager):
    """Override class to be able to correctly use user registration from DJOSER without a username."""

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.pop('password2')  # removing the password2 field in order to save the object correctly.
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Custom model of user without username (uses email instead)."""
    objects = CustomUserManager()

    username = models.CharField(max_length=40, unique=False, default='')  # change username to be not unique
    email = models.EmailField(unique=True)  # change email to unique and blank to false
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # removes email from REQUIRED_FIELDS

    def __str__(self):
        return self.email
