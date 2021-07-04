from django.urls import path

from .views import *

urlpatterns = [
    path("create_webhook/", create_webhook),
    path("post_data/webhook/<str:webhook_endpoint_name>", post_webhook_data),
    path("get_details/<str:webhook_endpoint_name>", webhook_detail_view),
    path("get_list/", webhook_list_view),
]
