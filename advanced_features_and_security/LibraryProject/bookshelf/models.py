from django.conf import settings
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
            ('can_create', 'Can Create'),
            ('can_delete', 'Can Delete'),
            ('can_edit', 'Can Edit'),
            ('can_view', 'Can View')
        ]


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


class UserProfile(models.Model):
    USER_PROFILE_EDITORS = 'E'
    USER_PROFILE_VIEWERS = 'V'
    USER_PROFILE_ADMINS = 'A'

    ROLE = [
        (USER_PROFILE_EDITORS, 'Editors'),
        (USER_PROFILE_VIEWERS, 'Viewers'),
        (USER_PROFILE_ADMINS, 'Admins')
    ]

    role = models.CharField(max_length=50, choices=ROLE, default= USER_PROFILE_VIEWERS)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookshelf_profile')

    def __str__(self):
        return str(self.user)