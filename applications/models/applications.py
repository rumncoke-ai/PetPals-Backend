from django.db import models
from shelters.models.pets import Pet
from accounts.models.seekers import PetSeeker as Seeker
from shelters.models.shelter import PetShelter as Shelter


class Application(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='applications')
    seeker = models.ForeignKey(Seeker, on_delete=models.CASCADE, related_name='applications')
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE, related_name='applications')  # This field is tentative, you can adjust it as needed
    APPLICATION_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    application_status = models.CharField(max_length=10, choices=APPLICATION_STATUS_CHOICES, blank=False, null=False)
    last_update_time = models.DateTimeField(auto_now=True)  # Automatically updated on each save
    name = models.CharField(max_length=200, blank=False, null=False)
    phone_number = models.CharField(max_length=15, blank=False, null=False)
    email = models.EmailField(max_length=200, blank=False, null=False)
    address1 = models.CharField(max_length=200, blank=False, null=False)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=False, null=False)
    province = models.CharField(max_length=2, blank=False, null=False)
    zip_code = models.CharField(max_length=7, blank=False, null=False)
    num_adults = models.IntegerField(blank=False, null=False)
    num_children= models.IntegerField(blank=False, null=False)
    RESIDENCE_CHOICES = [
        ('House', 'House'),
        ('Apartment', 'Apartment'),
        ('Condo', 'Condo'),
        ('Townhouse', 'Townhouse'),
        ('Mobile Home', 'Mobile Home'),
    ]
    residence = models.CharField(max_length=50, choices=RESIDENCE_CHOICES, blank=False, null=False)
    OWNERSHIP_CHOICES = [
        ('Own', 'Own'),
        ('Rent', 'Rent'),
    ]
    ownership = models.CharField(max_length=50, choices=OWNERSHIP_CHOICES, blank=False, null=False)
    pet_alone_time = models.TextField(max_length=1000, blank=False, null=False)
    current_pets = models.TextField(max_length=1000, blank=False, null=False)
    daily_routine = models.TextField(max_length=1000, blank=False, null=False)
    expenses = models.TextField(max_length=1000, blank=False, null=False)
    previous_pets = models.TextField(max_length=1000, blank=False, null=False)
    reason = models.TextField(max_length=1000, blank=False, null=False)
    reference_name = models.CharField(max_length=50, blank=False, null=False)
    reference_number = models.CharField(max_length=15, blank=False, null=False)
    reference_email = models.EmailField(blank=False, null=False)
    additional_comments = models.TextField(max_length=1000)

    def __str__(self):
        return f"Application #{self.id} for {self.pet.name}"