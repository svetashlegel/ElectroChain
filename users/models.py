from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
        Custom user model where email is the primary identifier instead of username.
    """

    username = None
    email = models.EmailField(unique=True, verbose_name='Email')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
