from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models.pets import Pet, PetImage
from .models.reviews import Review
from .models.shelter import PetShelter, ShelterImage

admin.site.register(Pet)
admin.site.register(PetImage)
admin.site.register(PetShelter)
admin.site.register(ShelterImage)
admin.site.register(Review)