# web_crypto_back/celery.py
 
import os
from django.conf import settings
from celery import Celery
 
#Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_crypto_back.settings')
 
app = Celery('web_crypto_back')

# namespace='CELERY' means all celery-related configuration keys
# should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')
 
# Load task modules from all registered Django app configs.
app.autodiscover_tasks(settings.INSTALLED_APPS)
