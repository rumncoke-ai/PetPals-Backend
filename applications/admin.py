from django.contrib import admin

# Register your models here.
from .models.applications import Application

admin.site.register(Application)