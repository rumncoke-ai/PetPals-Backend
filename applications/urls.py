from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import CreateApplicationView, ApplicationDetailView, ListApplicationView


app_name = 'applications'

urlpatterns = [
    path('<int:pet_pk>/application/', CreateApplicationView.as_view(), name='create'),
    path('<int:pet_pk>/<int:application_pk>/', ApplicationDetailView.as_view(), name='update'),
    path('<int:pet_pk>/', ListApplicationView.as_view(), name='list-apps'),
]