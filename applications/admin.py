from django.contrib import admin

# Register your models here.
from .models.applications import Application
from .models.chat import Chat

admin.site.register(Chat)
admin.site.register(Application)