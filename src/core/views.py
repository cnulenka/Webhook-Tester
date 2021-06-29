from django.db import models
from django.db.models import query
from django.http.response import HttpResponseNotFound
from django.shortcuts import render
import copy, json, datetime

from django.conf import settings
from django.db.transaction import atomic, non_atomic_requests
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.core import exceptions

from .models import Endpoint, WebHookData


@csrf_exempt
@require_POST
def create_webhook(request):
    '''
        create a new enpoint object, adds a
        new row to Endpoint table.
    '''
    Endpoint.objects.create()
    return HttpResponse("Message received okay.", content_type="text/plain")

@csrf_exempt
@require_POST
def post_data(request, endpoint_name):
    '''
        Add data to existing webhooks
    '''

    try:
        endpoint = Endpoint.objects.get(pk=endpoint_name)
    except exceptions.ObjectDoesNotExist:
        return HttpResponseNotFound("Endpoint id does not exits")

    payload = request.body.decode('utf-8')
    headers = json.dumps(dict(request.headers))
    query_params = json.dumps(dict(request.POST))

    #save the webhook post data
    WebHookData.objects.create(received_at=timezone.now(), payload=payload, headers=headers, query_params=query_params, endpoint=endpoint)

    #update endpoint count
    endpoint.num_hits += 1
    endpoint.save()

    return HttpResponse("Message received okay.", content_type="text/plain")