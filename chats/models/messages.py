from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from accounts.models import PetSeeker as Seeker 
from shelters.models.shelter import PetShelter as Shelter
from accounts.models import CustomUser

class Chat(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    seeker = models.ForeignKey(Seeker, on_delete=models.CASCADE, related_name='chats')  # Foreign Key to Seeker
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE, related_name='chats')  # Foreign Key to Shelter

    def __str__(self):
        return f"Chat {self.id} between {self.seeker.username} and {self.shelter.username}"


class Message(models.Model):
    # message can be attached to either a chat or review 
    message_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='messages')
    object_id = models.PositiveIntegerField()
    chat_or_review = GenericForeignKey('message_content_type', 'object_id')
    
    date_sent = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=500, blank=False, null=False)
    
    # Sender can be either a Seeker or a Shelter
   
    sender = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return f"Message {self.id} - Sent by {self.sender.username}"

# Example of usage:

# chat_message = Message.objects.create(content_type=ContentType.objects.get_for_model(Chat), 
# object_id=chat_instance.id, date_sent=..., message_contents=..., sender=...)

# review_message = Message.objects.create(content_type=ContentType.objects.get_for_model(Review),
# object_id=review_instance.id, date_sent=..., message_contents=..., sender=...)





