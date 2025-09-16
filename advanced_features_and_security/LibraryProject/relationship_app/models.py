from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.base_user import BaseUserManager
from django.conf import settings



# Create your models here.

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


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    class Meta:
         permissions = [
            ('can_add_book', 'Can add book'),
            ('can_change_book', 'Can change book'),
            ('can_delete_book', 'Can delete book'),
        ]

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='books')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class UserProfile(models.Model):
    ROLE = [
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
        ('Admin', 'Admin')
    ]
    role = models.CharField(max_length=50, choices=ROLE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
    

@receiver(post_save, sender= settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user = instance)

    