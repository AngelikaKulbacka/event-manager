from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Event
        fields = '__all__'