from django.contrib import admin
from .models import WebHookData, WebHook

admin.site.register(WebHookData)
admin.site.register(WebHook)
