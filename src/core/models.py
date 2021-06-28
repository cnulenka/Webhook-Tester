from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

class Endpoint(models.Model):
    name = models.CharField(max_length=40, primary_key = True)
    create_at = models.DateTimeField(auto_now_add=True, null=False)
    num_hits = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

class WebHookData(models.Model):
    endpoint = ForeignKey(Endpoint, on_delete=models.CASCADE)
    generated_at = models.DateTimeField()
    received_at = models.DateTimeField(default=timezone.now)
    payload = models.TextField(default=None, null=True)

    class Meta:
        indexes = [
            models.Index(fields=["received_at"]),
        ]

    def __str__(self) -> str:
        return self.endpoint.name + str(self.web_hook_data_id)