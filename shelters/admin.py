from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models.pets import Pet
from .models.reviews import Review
from .models.shelter import PetShelter

admin.site.register(Pet)
admin.site.register(PetShelter)
admin.site.register(Review)