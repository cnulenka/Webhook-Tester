from webhook_tester.celery import app
from .models import Endpoint
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
        endpoint_objects = Endpoint.objects.filter(created_at__lte=current_time)
        endpoint_objects.delete()
    except Exception as e:
        print(e)
