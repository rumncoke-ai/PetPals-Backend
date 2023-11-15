
from rest_framework import serializers
from accounts.models import CustomUser, PetSeeker
from ..models.messages import Message, Chat


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['chat_or_review', 'date_sent', 'sender', 'message_content_type', 'object_id']


class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = '__all__'
        read_only_fields = ['date_created', 'seeker', 'shelter']
