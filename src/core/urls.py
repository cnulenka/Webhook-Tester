from django.urls import path

from .views import *

urlpatterns = [
    path("create-webhook/", create_webhook),
    path("post-data/webhook/<str:webhook_endpoint_name>", post_webhook_data),
    path("get-details/<str:webhook_endpoint_name>", webhook_detail_view),
    path("get-list/", webhook_list_view),
]
