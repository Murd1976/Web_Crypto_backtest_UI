# web_crypto_back/celery.py
 
import os
from celery import Celery
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_crypto_back.settings')
 
app = Celery('web_crypto_back')
app.config_from_object('django.conf:settings')
 
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
