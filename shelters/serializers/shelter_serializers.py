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
        fields = ['username','phone_number', 'address', 'email', 'profile_photo']
        read_only_fields = ['username']

class PetShelterRetrieveSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    shelter_images = ShelterImageSerializer(many=True, read_only=True)

    class Meta:
        model = PetShelter
        fields = [ 'shelter_name', 'mission_statement', 'user', 'shelter_images']
        

        
class CustomUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','phone_number', 'password', 'address', 'email', 'profile_photo']
        read_only_fields = ['username']
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'read_only': True}
        }

"""
Must send array of images want to keep
"""
class PetShelterUpdateSerializer(serializers.ModelSerializer):
    user = CustomUserUpdateSerializer(required=False)
    new_images = serializers.ListField(child=ShelterImageSerializer(), write_only=True, required=False)
    old_images = serializers.ListField(child=serializers.IntegerField(), write_only=True, required=False)
    shelter_images = ShelterImageSerializer(many=True, read_only=True)
    class Meta: 
        model = PetShelter
        fields = ['shelter_name', 'mission_statement', 'user', 'shelter_images','new_images', 'old_images']

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user_serializer = CustomUserUpdateSerializer(instance.user, data=user_data, partial=True)
            if user_serializer.is_valid():
                user_serializer.save()

        return super().update(instance, validated_data)
