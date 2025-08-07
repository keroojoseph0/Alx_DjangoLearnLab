from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]

    def __str__(self):
        return self.title

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email = None, password = None, **kwargs):
        if not username:
            raise ValueError("Username is required")
        
        user = self.model(username = username, email = email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email = None, password = None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        
        return self.create_user(username, email = email, password = password, **kwargs)
    

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(null=True, blank=True)

    objects = CustomUserManager()
    