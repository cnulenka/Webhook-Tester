from django.urls import path
from .views import *

urlpatterns = [
    path('create_webhook/', create_webhook),
    path('post_data/webhook/<str:endpoint_name>', post_data),
]
