from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models  import Book, Author, Librarian, Library, UserProfile, CustomUser
# Register your models here.

admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(Author)
admin.site.register(UserProfile)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('pdate_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
