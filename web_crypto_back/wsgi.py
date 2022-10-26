"""
WSGI config for web_crypto_back project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_crypto_back.settings')

application = get_wsgi_application()
os.system('celery -A web_crypto_back multi restart worker --pidfile="$HOME/%/buf/web_crypto_back/celery/n.pid" --logfile="$HOME/buf/web_crypto_back/celery/%n%I.log"D ')
