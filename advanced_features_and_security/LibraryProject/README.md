# LibraryProject

# Permissions and Groups Setup Guide

This Django application uses **custom permissions** and **user groups** to control access to various model actions (create, edit, view, delete).

## 🔐 Custom Permissions

Custom permissions are defined inside the model `Book` using the `Meta` class.

```python
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_view", "Can view books"),
            ("can_create", "Can create books"),
            ("can_edit", "Can edit books"),
            ("can_delete", "Can delete books"),
        ]
