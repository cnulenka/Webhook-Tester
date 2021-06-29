from django.shortcuts import render
import datetime
import json

from django.conf import settings
from django.db.transaction import atomic, non_atomic_requests
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone

from .models import Endpoint


@csrf_exempt
@require_POST
def create_webhook(request):
    '''
        create a new enpoint object, adds a
        new row to Endpoint table.
    '''
    Endpoint.objects.create()
    return HttpResponse("Message received okay.", content_type="text/plain")
