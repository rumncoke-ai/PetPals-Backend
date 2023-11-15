from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView
from .views.shelter import PetShelterSignUpView, PetShelterLoginView,ShelterRetrieveUpdateDestroyView
from .views.shelter import PetShelterListView
from .views.pets import CreatePetView, PetDetailView
from .views.reviews import CreateListView, CreateReviewMessageView, MessageListAPIView

app_name = 'shelter'

urlpatterns = [
    path('account/', PetShelterSignUpView.as_view(), name='signup'),
    path('token/', PetShelterLoginView.as_view(), name='login'),
    path('<int:shelter_pk>/', ShelterRetrieveUpdateDestroyView.as_view(), name='detail'),
    path('', PetShelterListView.as_view(), name='list'),
    path('<int:shelter_pk>/review/', CreateListView.as_view()),
    path('<int:shelter_pk>/review/<int:review_pk>/', MessageListAPIView.as_view(), name='list_review'),
    path('<int:shelter_pk>/review/<int:review_pk>/message/', CreateReviewMessageView.as_view(), name='create_review_message'),
    path('<int:shelter_pk>/pet/', CreatePetView.as_view(), name='create_pet'),
    path('<int:shelter_pk>/pet/<int:pet_pk>/', PetDetailView.as_view(), name='pet_detail'),
]

