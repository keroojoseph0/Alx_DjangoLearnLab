# LibraryProject

## Django Permissions & Groups Setup

### Custom Permissions
We have defined custom permissions in the `Book` model:

- **can_edit** → Allows editing books.
- **can_create** → Allows creating new books.

These are created automatically when running `python manage.py migrate`.

---

### Groups Setup
1. Go to Django Admin → Groups.
2. Create groups (e.g., `Editors`, `Admins`, `Viewers`).
3. Assign permissions:
   - `Editors`: can_edit, can_create
   - `Admins`: all permissions
   - `Viewers`: read-only (no custom perms)

---

### Assigning Users to Groups
In code:

```python
from django.contrib.auth.models import Group, User

user = User.objects.get(username="john")
group = Group.objects.get(name="Editors")
user.groups.add(group)

### Security Measures
- Debug mode disabled in production.
- CSP enabled via django-csp middleware.
- Secure cookie settings (`CSRF_COOKIE_SECURE`, `SESSION_COOKIE_SECURE`).
- HTTPS enforced (`SECURE_SSL_REDIRECT`, HSTS).
- ORM used instead of raw SQL to prevent injection.
- All user input validated with Django forms.
