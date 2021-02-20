from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Model of user."""
    email = models.EmailField(unique=True)  # change email to unique and blank to false
    # replacing username by email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # removes email from REQUIRED_FIELDS

    def __str__(self):
        return self.email
