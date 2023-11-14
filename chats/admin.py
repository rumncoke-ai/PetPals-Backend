from django.contrib import admin

# Register your models here.
from .models.messages import Message, Chat

admin.site.register(Message)
admin.site.register(Chat)