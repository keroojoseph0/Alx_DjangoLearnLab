from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

class CustomUserManger(UserManager):
    def create_usr(self, username, email = None, password = None, **kwargs):
        if not username:
            raise ValueError("Username is required")
        if not kwargs.get('date_of_birth'):
            raise ValueError('Date of birth is required')
        
        return super().create_user(username, email = email, password = password, **kwargs)

    def create_superuser(self, username, email = None, password = None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        if not kwargs.get('date_of_birth'):
            raise ValueError('Date of birth is required')
        
        return super().create_superuser(username, email = email, password = password, **kwargs)
    

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()

    objects = CustomUserManger()
    