from rest_framework import serializers
from accounts.models import CustomUser
from ..models.shelter import PetShelter, ShelterImage
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password

class PetShelterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

class PetShelterSignUpSerializer(serializers.ModelSerializer):
    
    shelter_name = serializers.CharField(write_only=True, max_length=30, required=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'shelter_name']

class ShelterImageSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ShelterImage
        fields = ['image_file', 'id']
        read_only_fields = ['id']


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['phone_number', 'address', 'email', 'profile_photo']

class PetShelterRetrieveSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    shelter_images = ShelterImageSerializer(many=True, read_only=True)

    class Meta:
        model = PetShelter
        fields = ['shelter_name', 'mission_statement', 'user', 'shelter_images']


class CustomUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['password','phone_number', 'address', 'email', 'profile_photo']



"""
Must send array of images want to keep
"""
class PetShelterUpdateSerializer(serializers.ModelSerializer):
    user = CustomUserUpdateSerializer()
    new_images = serializers.ListField(child=ShelterImageSerializer(), write_only=True, required=False)
    old_images = serializers.ListField(child=serializers.IntegerField(), write_only=True, required=False)
    shelter_images = ShelterImageSerializer(many=True, read_only=True)
    class Meta: 
        model = PetShelter
        fields = ['shelter_name', 'mission_statement', 'user', 'shelter_images','new_images', 'old_images']
