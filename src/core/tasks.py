from webhook_tester.celery import app
from .models import WebHook
import datetime
from django.utils import timezone

@app.task(name="delete_old_webhook_endpoints")
def delete_old_webhook_endpoints():
    '''
    A background job that runs in a set frequency deleting all
    expired endpoints (endpoints whose time to live is
    breached - time to live is 1 hour)
    '''

    try:
        current_time = datetime.datetime.now(tz=timezone.utc)
        webhook_endpoint_objects = WebHook.objects.filter(created_at__lte=current_time)
        webhook_endpoint_objects.delete()
    except Exception as e:
        print(e)
