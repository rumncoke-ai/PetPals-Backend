from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView

from .views.pets import CreatePetView, PetDetailView, PetListView, PetImageCreateView, PetImageDeleteView
from .views.applications import CreateApplicationView, ApplicationDetailView, ListAllApplicationView
from .views.applications import CreateChatMessageView,MessageListAPIView,CreateChatListView

app_name = 'pet'

urlpatterns = [
    path('new/', CreatePetView.as_view(), name='create_pet'),
    path('<int:pet_pk>/', PetDetailView.as_view(), name='pet_detail'),
    path('', PetListView.as_view(), name='pet_search'),
    path('<int:pet_pk>/applications/new/', CreateApplicationView.as_view(), name='create'),
    path('<int:pet_pk>/applications/<int:application_pk>/', ApplicationDetailView.as_view(), name='update'),
    path('applications/', ListAllApplicationView.as_view(), name='list-apps'),
    path('applications/<int:application_pk>/chat/', CreateChatListView.as_view()),
    path('applications/chat/<int:chat_pk>/message/', CreateChatMessageView.as_view()),
    path('applications/chat/<int:chat_pk>/', MessageListAPIView.as_view()),
    path('<int:pet_pk>/image/', PetImageCreateView.as_view()),
    path('<int:pet_pk>/image/<int:image_pk>/', PetImageDeleteView.as_view()),

]