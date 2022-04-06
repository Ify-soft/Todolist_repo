from django.contrib import admin
from .models import todolist, Profile
# Register your models here.

admin.site.register(todolist)
admin.site.register(Profile)