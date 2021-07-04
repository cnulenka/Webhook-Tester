from django.urls import path

from .views import *

urlpatterns = [
    path("create-webhook", create_webhook),
    path("<str:webhook_endpoint_name>", post_webhook_data),
    path("get-details/<str:webhook_endpoint_name>", webhook_detail_view),
    #list view is the home page
    path("", webhook_list_view),
]
