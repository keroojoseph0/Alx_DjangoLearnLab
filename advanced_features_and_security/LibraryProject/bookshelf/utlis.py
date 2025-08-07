from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

User = get_user_model()

user = User.objects.get(username='admin')
group, created = Group.objects.get_or_create(name='Admins')

group.user_set.add(user)