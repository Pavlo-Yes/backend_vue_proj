from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class UserModel(AbstractUser):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(max_length=50, unique=True)
    # password = models.CharField
