from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email',
        'username',
        'age',
        'is_staff'
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('age',)}),)
    add_fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('age',)}),)

admin.site.register(CustomUser, CustomUserAdmin)