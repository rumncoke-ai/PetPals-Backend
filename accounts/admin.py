from django.contrib import admin

# Register your models here.
# myapp/admin.py


from .models import PetSeeker
from .models import CustomUser

admin.site.register(PetSeeker)

admin.site.register(CustomUser)
