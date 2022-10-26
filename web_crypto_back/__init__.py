from .celery import app as celery_app
#import os

__all__ = ('celery_app',)
#os.system('celery -A web_crypto_back worker --loglevel=info --logfile=/buf/web_crypto_back/celery.log')