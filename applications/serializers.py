from rest_framework import serializers
from accounts.models import PetSeeker
from .models.applications import Application
from shelters.models import PetShelter, Pet
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password

class PetShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetShelter
        fields = '__all__'
        read_only_fields = ('user',)

class PetSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetSeeker
        fields = '__all__'
        read_only_fields = ('user',)

class PetSerializer(serializers.ModelSerializer):
    shelter = PetShelterSerializer(required=False)
    class Meta:
        model = Pet
        fields = '__all__'
        read_only_fields = ('user',)

class CreateApplicationSerializer(serializers.ModelSerializer):
    pet = PetSerializer(required=False)
    shelter = PetShelterSerializer(required=False)
    seeker = PetSeekerSerializer(required=False)
    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ['pet', 'seeker', 'shelter', 'last_update_time', 'application_status', 'creation_time']
    
class ListApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ('pet', 'seeker', 'shelter', 'name', 'phone_number', 'email', 'address1', 'address2', 'city', 'province', 'zip_code',
                            'num_adults', 'num_children', 'residence', 'ownership', 'pet_alone_time',
                            'current_pets', 'daily_routine', 'expenses', 'previous_pets', 'reason',
                            'reference_name', 'reference_number', 'reference_email', 'additional_comments', 'last_update_time', 'creation_time')

    # def validate(self, data):
    #     # Ensure that the user can only update the application_status field
    #     if 'application_status' not in data:
    #         raise serializers.ValidationError("You can only update the application_status field.")
    #     return data