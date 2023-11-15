# urls.py

from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView
from .views import PetSeekerSignUpView, PetSeekerLoginView, SeekerRetrieveUpdateDestroyView


app_name = 'seeker'

urlpatterns = [
    path('account/', PetSeekerSignUpView.as_view(), name='signup'),
    path('token/', PetSeekerLoginView.as_view(), name='login'),
    path('<int:pk>/', SeekerRetrieveUpdateDestroyView.as_view(), name='seeker_detail'),
]
