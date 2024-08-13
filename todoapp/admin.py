from django.contrib import admin
from todoapp.models import Task, User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("email",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    list_display = ("username",)
    search_fields = ("username", "email")
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


class CustomTaskAdmin(admin.ModelAdmin):
    fields = ("user", "title", "description", "status", "duedate")
    list_display = ("title", )


# Register your models here.
admin.site.register(Task, CustomTaskAdmin)

admin.site.register(User, CustomUserAdmin)