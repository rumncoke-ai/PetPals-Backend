
from rest_framework import serializers
from accounts.models import CustomUser, PetSeeker
from ..models.messages import Message, Chat


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['content', 'sender', 'date_sent', 'message_content_type', 'object_id', 'message_type']
        read_only_fields = ['date_sent', 'sender', 'message_content_type', 'object_id', 'message_type']


class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = '__all__'
        read_only_fields = ['date_created', 'seeker', 'shelter']
