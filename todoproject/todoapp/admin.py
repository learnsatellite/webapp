from django.contrib import admin
from todoapp.models import Task, User

# Register your models here.
admin.site.register(Task)

admin.site.register(User)