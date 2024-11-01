from django.contrib import admin
from todoapp.models import Task, User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import TaskForm

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
        (
            _("Important dates"),
            {"fields": ("last_login",)},
        ),
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
    search_fields = ("username",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    readonly_fields = ("last_login",)


class CustomTaskAdmin(admin.ModelAdmin):
    form = TaskForm
    fields = ("user", "title", "description", "status", "duedate")
    list_display = ("title", )


# Register your models here.
admin.site.register(Task, CustomTaskAdmin)

admin.site.register(User, CustomUserAdmin)