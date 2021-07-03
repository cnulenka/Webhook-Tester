from django.db import models
from django.db.models import query
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
import uuid

class WebHook(models.Model):
    name = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    num_hits = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.name)

class WebHookData(models.Model):
    webhook = ForeignKey(WebHook, on_delete=models.CASCADE)
    received_at = models.DateTimeField(default=timezone.now)
    payload = models.TextField(default=None, null=True)
    query_params = models.TextField(default=None, null=True)
    headers = models.TextField(default=None, null=True)
    webhook_hit_number = models.IntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=["received_at"]),
        ]

    def __str__(self) -> str:
        return str(self.endpoint.name) + "_" + str(self.endpoint_hit_number)