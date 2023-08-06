from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .form import MyCustomForm

class MyUserAdmin(UserAdmin):
    add_form = MyCustomForm
    # Other customizations for the User admin if needed

# Register the User model with the custom admin class
admin.site.unregister(User)  # Unregister the default UserAdmin
admin.site.register(User, MyUserAdmin)  # Register with the custom MyUserAdmin
