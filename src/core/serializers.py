import datetime
import json

from django.conf import settings
from django.utils import timezone
from rest_framework import serializers

from .models import WebHook, WebHookData


class WebHookDataResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebHookData
        fields = ["payload"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        received_since = datetime.datetime.now(tz=timezone.utc) - instance.received_at
        received_since_seconds = round(received_since.total_seconds())
        received_since_mins = round(received_since_seconds / 60)
        if received_since_seconds <= 60:
            representation["received_since"] = str(received_since_seconds) + " seconds"
        else:
            representation["received_since"] = str(received_since_mins) + " minutes"

        representation["headers"] = json.loads(instance.headers)
        representation["query_params"] = json.loads(instance.query_params)
        return representation


class WebhookResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebHook
        fields = ["name", "num_hits"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        created_at_plus_one_hour = instance.created_at + datetime.timedelta(hours=1)
        time_left = created_at_plus_one_hour - datetime.datetime.now(tz=timezone.utc)
        time_left_seconds = round(time_left.total_seconds())
        time_left_mins = round(time_left_seconds / 60)
        if time_left_seconds <= 60:
            representation["time_left"] = str(time_left_seconds) + " secs"
        else:
            representation["time_left"] = str(time_left_mins) + " mins"
        return representation
