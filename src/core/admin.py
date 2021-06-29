from django.contrib import admin
from .models import WebHookData, Endpoint

admin.site.register(WebHookData)
admin.site.register(Endpoint)
