from django.conf import settings
from rest_framework import serializers
from .models import WebHookData, WebHook

class WebHookDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebHookData
        fields = ['payload', 'query_params', 'headers', 'received_at']


class WebhookSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebHook
        fields = ['name', 'num_hits', 'created_at']