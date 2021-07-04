import datetime

from django.utils import timezone

from webhook_tester.celery import app

from .models import WebHook


@app.task(name="delete_old_webhook_endpoints")
def delete_old_webhook_endpoints():
    """
    A background job that runs in a set frequency deleting all
    expired endpoints (endpoints whose time to live is
    breached - time to live is 1 hour)
    """

    try:
        time_thresold = datetime.datetime.now(tz=timezone.utc) - datetime.timedelta(
            hours=1
        )
        webhook_endpoint_objects = WebHook.objects.filter(created_at__lte=time_thresold)
        webhook_endpoint_objects.delete()
    except Exception as e:
        print(e)
