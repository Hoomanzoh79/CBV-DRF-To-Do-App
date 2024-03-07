from django.contrib.auth.admin import UserAdmin

from .models import User,Profile
from django.contrib import admin

@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    list_display = (
        "email",
        "is_superuser",
        "is_active",
    )
    list_filter = (
        "email",
        "is_superuser",
        "is_active",
    )
    search_fields = ("email",)
    ordering = ("email",)
    fieldsets = (
        ("Authentication", {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                )
            },
        ),
        (
            "Group Permissions",
            {
                "fields": (
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important Data", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_superuser",
        
                ),
            },
        ),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    fields = ("user","first_name","last_name")