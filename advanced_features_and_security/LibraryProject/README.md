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


# 🔐 Security Settings and Practices in the Project

This section documents the security measures applied to ensure the safety and privacy of user data and to protect against common web vulnerabilities.

---

## ⚙️ Security Configurations in `settings.py`

- `DEBUG = False`:  
  Disabled in production to avoid leaking sensitive error messages.

- `SECURE_BROWSER_XSS_FILTER = True`:  
  Enables the browser's built-in XSS protection.

- `X_FRAME_OPTIONS = 'DENY'`:  
  Prevents the website from being embedded in frames, protecting against clickjacking attacks.

- `SECURE_CONTENT_TYPE_NOSNIFF = True`:  
  Stops the browser from guessing content types, reducing risk of drive-by download attacks.

- `CSRF_COOKIE_SECURE = True`:  
  Ensures the CSRF cookie is only sent over HTTPS, protecting against man-in-the-middle attacks.

- `SESSION_COOKIE_SECURE = True`:  
  Forces session cookies to be sent only over HTTPS.

---

## 🧱 Content Security Policy (CSP)

We use a CSP header to control where scripts, styles, and other resources can be loaded from.

Example configuration:
```python
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", "https://trusted.cdn.com")
CSP_STYLE_SRC = ("'self'", "https://trusted.styles.com")
CSP_IMG_SRC = ("'self'", "data:", "https://images.com")

