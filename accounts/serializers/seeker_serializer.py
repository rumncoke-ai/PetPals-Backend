from rest_framework import serializers
from accounts.models import CustomUser, PetSeeker
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from django.contrib.auth.password_validation import validate_password
from ..models import CustomUser

class PetSeekerSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

class PetSeekerSignUpSerializer(serializers.ModelSerializer):
   
    firstname = serializers.CharField(write_only=True, max_length=30,required=True)
    lastname = serializers.CharField(write_only=True, max_length=30,required=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'firstname', 'lastname']



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['phone_number', 'address', 'email', 'profile_photo']


class PetSeekerRetrieveSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = PetSeeker
        fields = ['firstname','lastname', 'user']

class CustomUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['password','phone_number', 'address', 'email', 'profile_photo']


class PetSeekerUpdateSerializer(serializers.ModelSerializer):
    user = CustomUserUpdateSerializer()
    class Meta: 
        model = PetSeeker
        fields = ['firstname','lastname', 'user','dog_notification','cat_notification','other_notification']