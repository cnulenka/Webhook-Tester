import uuid

from django.db import models
from django.db.models import query
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey
from django.utils import timezone


class WebHook(models.Model):
    '''
        Models the webhook endpoint. This model has the
        unique endpoint name, creation time, also maintains
        the number of hits info.
    '''

    name = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    num_hits = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.name)


class WebHookData(models.Model):
    '''
        Models the webhook post data for any endpoint.
        This model has the payload(body), query_params, headers
        info. Also maintains webhook_hit_number which basically
        says this data belongs to which hit i.e 1st hit, 2nd hit etc.

        Also maintains received time. Has webhook model as foreign key.
        One webhook can have many post data calls.

        This model is indexed on received date to aid search and
        order by queries.
    '''

    webhook = ForeignKey(WebHook, on_delete=models.CASCADE)
    received_at = models.DateTimeField(default=timezone.now)
    payload = models.TextField(default=None, null=True)
    query_params = models.TextField(default=None, null=True)
    headers = models.TextField(default=None, null=True)
    webhook_hit_number = models.IntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=["-received_at"]),
        ]

    def __str__(self) -> str:
        return str(self.webhook.name) + "_" + str(self.webhook_hit_number)
