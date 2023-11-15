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
from ..models import PetShelter, Review
from accounts.models import CustomUser, PetSeeker
from ..serializers.shelter_serializers import PetShelterSerializer, PetShelterSignUpSerializer,PetShelterRetrieveSerializer,PetShelterUpdateSerializer
from rest_framework.generics import RetrieveAPIView
from django.shortcuts import get_object_or_404
from ..serializers.review_serializers import ReviewSerializer
from chats.serializers.message_serializers import MessageSerializer
from rest_framework.pagination import PageNumberPagination
from django.contrib.contenttypes.models import ContentType
from chats.models.messages import Message





class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5  # Set the default page size
    page_size_query_param = 'page_size'  
    # Allow clients to override the page size via query parameter
    max_page_size = 5  # Set the maximum allowed page size

    def get_paginated_response(self, data):
        return Response({
            'pagination_details': {
                'count': self.page.paginator.count,
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                'page_size': self.page_size,
            },
            'results': data,
        })

class CreateReviewMessageView(generics.CreateAPIView):
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        user_id = self.request.user.id
        user = get_object_or_404(CustomUser, id=user_id)

        review_id = self.kwargs['review_pk']
        review = get_object_or_404(Review, id=review_id)
        serializer.save(sender=user, message_content_type=ContentType.objects.get_for_model(review),
            object_id=review.id)


class CreateListView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        shelter_id = self.kwargs.get('shelter_pk')
        shelter = get_object_or_404(PetShelter, id=shelter_id)
        queryset = Review.objects.filter(shelter=shelter).order_by('-creation_time')
        return queryset

    def perform_create(self, serializer):
        user_id = self.request.user.id
        user = get_object_or_404(CustomUser, id=user_id)
        shelter_id = self.kwargs['shelter_pk']
        shelter = get_object_or_404(PetShelter, id=shelter_id)
        serializer.save(user=user, shelter=shelter)


class MessageListAPIView(ListAPIView):
    serializer_class = MessageSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        review_id = self.kwargs.get('review_pk')
        return Message.objects.filter(
            message_content_type=ContentType.objects.get_for_model(Review),
            object_id=review_id
        ).order_by('-date_sent')