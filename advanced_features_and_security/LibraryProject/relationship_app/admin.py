from django.contrib import admin
from .models  import Book, Author, Librarian, Library, UserProfile, CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    # show in detail page
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

    # show in add new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(Author)
admin.site.register(UserProfile)
