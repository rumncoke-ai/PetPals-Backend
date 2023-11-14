from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from accounts.models import PetSeeker as Seeker 
from shelters.models.shelter import PetShelter as Shelter

class Notifications(models.Model):

    # Sender can be either a Seeker or a Shelter
    sender_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='sender_content_type')
    sender_object_id = models.PositiveIntegerField()
    sender = GenericForeignKey('sender_content_type', 'sender_object_id')

    notification_type = models.CharField(max_length=50, choices=[
        ('new_message', 'new_message'),
        ('application_status', 'application_status'),
        ('new_pet', 'new_pet'),
        ('review', 'review'),
        ('new_application', 'new_application'),
    ], blank=False, null=False)
    notification_object = models.PositiveIntegerField(blank=False, null=False)  # Store the primary key of the related object
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification - {self.notification_type} {self.id}"
