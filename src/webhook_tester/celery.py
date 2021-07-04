import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed

# from core.task import delete_old_webhook_endpoints

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webhook_tester.settings")

app = Celery("webhook_tester")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    "delete-every-1-hour": {
        "task": "delete_old_webhook_endpoints",
        "schedule": crontab(minute="*/1"),
    }
}


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
