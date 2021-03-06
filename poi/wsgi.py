"""
WSGI config for poi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/var/www')
sys.path.append('/var/www/poi')
sys.path.append('/var/www/poi/poi')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "poi.settings")

application = get_wsgi_application()
