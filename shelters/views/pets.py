from django.shortcuts import render

from django.shortcuts import render
from rest_framework import status
from django.core.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework import views
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from ..models import PetShelter, Review, PetImage, Pet, PetShelter
from accounts.models import CustomUser, PetSeeker
from ..serializers.shelter_serializers import PetShelterSerializer, PetShelterSignUpSerializer,PetShelterRetrieveSerializer,PetShelterUpdateSerializer
from rest_framework.generics import RetrieveAPIView
from django.shortcuts import get_object_or_404
from ..serializers.pet_serializers import PetSerializer, PetImageSerializer, PetUpdateSerializer, PetRetrieveSerializer
from rest_framework.pagination import PageNumberPagination
from django.contrib.contenttypes.models import ContentType
from chats.models.messages import Message

class CreatePetView(CreateAPIView):
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = self.request.user

        # Check if the user is a PetShelter user
        shelter = PetShelter.objects.filter(user=user).first()
        if not shelter:
            return Response({"detail": "Only shelter can create pets. You do not have permission to create a pet."},
                            status=status.HTTP_403_FORBIDDEN)

        shelter = get_object_or_404(PetShelter, user=user)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.validated_data['shelter'] = shelter
            pet = serializer.save()
            response_data = {
                'pet_id': pet.id,
                'message': 'Pet successfully created.',
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            response_data = {
                'errors': serializer.errors,
                'message': 'Invalid Request.',
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class PetDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = PetRetrieveSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        return get_object_or_404(Pet, id=self.kwargs['pet_pk'])
    
    def get_serializer_class(self):
        # Override to use different serializers for different HTTP methods
        if self.request.method == 'PUT': # update
            return PetUpdateSerializer
        return PetRetrieveSerializer

    def get_permissions(self):
        # change permissions for DELETE and UPDATE, so user must be logged in 
        if self.request.method == 'DELETE' or self.request.method=='PUT':
            return [IsAuthenticated()]
        return super().get_permissions()

    def destroy(self, request, *args, **kwargs):
        pet = self.get_object()
        if self.request.user != pet.shelter.user:
            return Response({"detail": "Your shelter did not create this pet. You do not have permission to delete it."},
                            status=status.HTTP_403_FORBIDDEN)
        pet.delete()
        response_data = {
            'message': 'Pet successfully deleted.',
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        pet = self.get_object()
        serializer = self.get_serializer(instance=pet, data=request.data)
        if self.request.user != pet.shelter.user:
            return Response({"detail": "Your shelter did not create this pet. You do not have permission to update it."},
                            status=status.HTTP_403_FORBIDDEN)

        if serializer.is_valid():
            new_images = serializer.validated_data.pop('new_images', tuple())
            old_image_id = serializer.validated_data.pop('old_images', [])
            # shelter_data = serializer.validated_data.pop('shelter', tuple())

            shelter = get_object_or_404(PetShelter, user=self.request.user)
            serializer.instance.shelter = shelter
            serializer.save()
            pet = serializer.instance

            for image_file in new_images:
                PetImage.objects.create(**image_file, pet=pet)
            for image in pet.pet_images.all():
                if image.id not in old_image_id:
                    image.delete()
            
            response_data = {
                'pet_id': pet.id,
                'message': 'Pet successfully updated.',
            }
            return Response(response_data, status=status.HTTP_200_OK)

        else:
            response_data = {
                'errors': serializer.errors,
                'message': 'Invalid Request.',
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)