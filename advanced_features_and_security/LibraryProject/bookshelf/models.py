from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager



# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password = None, email = None, **kwargs):
        if not username:
            raise ValueError("User must have an username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            is_staff = False,
            is_superuser = False
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password = None, email = None, **kwargs):
        if not username:
            raise ValueError("User must have an username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            is_staff = True,
            is_superuser = True
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null = True, blank = True)
    profile_photo = models.ImageField(upload_to=None, null = True, blank = True)

    objects = CustomUserManager()
