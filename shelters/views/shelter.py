from django.shortcuts import render

from django.shortcuts import render
from rest_framework import status
from django.core.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView,UpdateAPIView
from rest_framework import views
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from ..models import PetShelter
from accounts.models import CustomUser, PetSeeker
from ..serializers.shelter_serializers import PetShelterSerializer, PetShelterSignUpSerializer,PetShelterRetrieveSerializer,PetShelterUpdateSerializer
from rest_framework.generics import RetrieveAPIView
from django.shortcuts import get_object_or_404

class PetShelterSignUpView(generics.CreateAPIView):
    serializer_class = PetShelterSignUpSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        shelter_name = serializer.validated_data.pop('shelter_name')
        new_user = serializer.save()
        new_shelter = PetShelter.objects.create(user=new_user, shelter_name=shelter_name)
        new_shelter.save()



class PetShelterLoginView(views.APIView):

    serializer_class = PetShelterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = CustomUser.objects.filter(username=username).first()
        
        if user is None or not (user.password == password):
            return Response({'message': 'Invalid credentials'})
        
        refresh = RefreshToken.for_user(user)
        response_data = {
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token),
        }
        return Response(response_data)

"""
Single endpoint /shelter/<>/
-> GET 
-> DELETE 
=> UPDATE shelter information
"""
class ShelterRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = PetShelterRetrieveSerializer
    permission_classes = [permissions.AllowAny]
    queryset = PetShelter.objects.all()

    def get_object(self):
        return get_object_or_404(PetShelter, pk=self.kwargs['shelter_pk'])

    def get_serializer_class(self):
        # Override to use different serializers for different HTTP methods
        if self.request.method == 'PUT': # update
            return PetShelterUpdateSerializer
        return PetShelterRetrieveSerializer

    def get_permissions(self):
        # change permissions for DELETE and UPDATE, so user must be logged in 
        if self.request.method == 'DELETE' or self.request.method=='PUT':
            return [IsAuthenticated()]
        return super().get_permissions()

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.user:
            return Response({"detail": "You do not have permission to update this shelter."},
                            status=status.HTTP_403_FORBIDDEN)

        new_images = serializer.validated_data.pop('new_images', tuple())
        old_image_id = serializer.validated_data.pop('old_images', [])
        user_data = serializer.validated_data.pop('user', tuple())

        user = CustomUser.objects.get(id=self.request.user.id)
        for key, value in user_data.items():
            setattr(user, key, value)
        user.save()
       
        #shelter = PetShelter.objects.update(**serializer.validated_data)
        #shelter.save()
        serializer.save()
        shelter = serializer.instance

        # for each new image file, create a new image object
        for image_file in new_images:
            ShelterImage.objects.create(**image_file, shelter=shelter)
        for image in shelter.shelter_images.all():
            if image.id not in old_image_id:
                image.delete()

    def perform_destroy(self, instance):
        if self.request.user != instance.user:
            return Response({"detail": "You do not have permission to delete this shelter."},
                            status=status.HTTP_403_FORBIDDEN)
        user = CustomUser.objects.get(id=instance.user.id)
        user.delete()
        instance.delete()






"""
List View for all Shelters 
Anybody can see all shelters
"""
class PetShelterListView(ListAPIView):
    queryset = PetShelter.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PetShelterRetrieveSerializer


class PetShelterUpdateView(UpdateAPIView):
    queryset = PetShelter.objects.all()
    serializer_class = PetShelterSerializer