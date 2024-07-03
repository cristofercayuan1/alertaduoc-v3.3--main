"""
WSGI config for alertaduoc project.

It exposes the WSGI callable as a module-level variable named 'app'.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

# Path to your Django project directory
path = os.path.expanduser('~/alertaduoc-v3.6--main')  # Replace with your actual project path

# Insert the path to sys.path if not already there
if path not in sys.path:
    sys.path.insert(0, path)

# Set the Django settings module
os.environ["DJANGO_SETTINGS_MODULE"] = "alertaduoc.settings"

# Import the WSGI application from Django
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

# Create a WSGI application with static files handling
application = StaticFilesHandler(get_wsgi_application())
