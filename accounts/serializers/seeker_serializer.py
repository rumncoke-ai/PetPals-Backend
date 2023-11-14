from rest_framework import serializers
from accounts.models import CustomUser, PetSeeker
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from django.contrib.auth.password_validation import validate_password
from ..models import CustomUser

class PetSeekerSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

class PetSeekerSignUpSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField( max_length=30,required=True)
    lastname = serializers.CharField( max_length=30,required=True)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'firstname', 'lastname']




class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'phone_number', 'address', 'email', 'profile_photo']
        read_only_fields = ['username']


class PetSeekerRetrieveSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = PetSeeker
        fields = ['firstname','lastname', 'user']

class CustomUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','phone_number', 'password', 'address', 'email', 'profile_photo']
        extra_kwargs = {
            'password': {'write_only': True},
            'usernmae': {'read_only': True},
        }

class PetSeekerUpdateSerializer(serializers.ModelSerializer):
    user = CustomUserUpdateSerializer(required=False)
    class Meta: 
        model = PetSeeker
        fields = ['firstname','lastname', 'user','dog_notification','cat_notification','other_notification']