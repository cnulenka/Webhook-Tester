from django.contrib import admin

from .models import WebHook, WebHookData

admin.site.register(WebHookData)
admin.site.register(WebHook)
