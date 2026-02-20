from django.contrib import admin
from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fields = ('id', 'username', 'email', 'first_name', 'last_name', 'bio', 'profile_picture', 'followers', 'is_staff', 'is_active', 'is_superuser')
    readonly_fields = ('id',)
    
