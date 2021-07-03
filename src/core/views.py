from django.db import models
from django.db.models import query
from django.http.response import HttpResponseNotFound
from django.shortcuts import render
import copy, json, datetime

from django.conf import settings
from django.db.transaction import atomic, non_atomic_requests
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from .serializers import WebHookDataSerializer, WebhookSerializer
from django.views.decorators.http import require_POST, require_GET
from django.utils import timezone
from django.core import exceptions

from .models import WebHook, WebHookData


@csrf_exempt
@require_POST
def create_webhook(request):
    '''
        create a new webhook enpoint object, adds a
        new row to Webhook table.
    '''
    WebHook.objects.create()
    return HttpResponse("Webhook enpoint created.", status=200)

@csrf_exempt
@require_POST
def post_webhook_data(request, webhook_endpoint_name):
    '''
        add/post data to existing webhooks
    '''

    try:
        webhook_endpoint = WebHook.objects.get(pk=webhook_endpoint_name)
    except exceptions.ObjectDoesNotExist:
        return HttpResponseNotFound("Endpoint id does not exits")

    payload = request.body.decode('utf-8')
    headers = json.dumps(dict(request.headers))
    query_params = json.dumps(dict(request.POST))

    #save the webhook post data
    WebHookData.objects.create(received_at=timezone.now(), payload=payload, headers=headers,
                                query_params=query_params, webhook=webhook_endpoint,
                                webhook_hit_number=webhook_endpoint.num_hits+1)

    #update endpoint count
    webhook_endpoint.num_hits += 1
    webhook_endpoint.save()

    return HttpResponse("Webhook data received.", status=200)

@require_GET
def webhook_detail_view(request, webhook_endpoint_name):
    '''
        returns all post data for input webhook
        endpoint.
    '''

    try:
        webhook_endpoint = WebHook.objects.get(pk=webhook_endpoint_name)
    except exceptions.ObjectDoesNotExist:
        return HttpResponseNotFound("Endpoint id does not exits")
    
    webhook_data = WebHookData.objects.filter(webhook=webhook_endpoint)
    webhook_data_serializer = WebHookDataSerializer(webhook_data, many=True)
    webhook_endpoint_serializer = WebhookSerializer(webhook_endpoint)
    context = {
        "webhook_endpoint_data_list" : webhook_data_serializer.data,
        "webhook_endpoint": webhook_endpoint_serializer.data
    }
    return render(request, "webhook_detail.html", context=context)

@require_GET
def webhook_list_view(request):
    '''
        returns list of created webhook endpoints,
        which are alive yet with name and hit count.
    '''

    webhook_endpoints = WebHook.objects.all()
    webhook_endpoints_serializer = WebhookSerializer(webhook_endpoints, many=True)
    print(webhook_endpoints_serializer.data)

    context = {
        "webhook_endpoint_list" : webhook_endpoints_serializer.data
    }
    return render(request, "webhook_list.html", context=context)