"""
WSGI config for alertaduoc project.
It exposes the WSGI callable as a module-level variable named 'application'.
For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

# Añade la ruta del proyecto a sys.path
path = os.path.expanduser('~/alertaduoc-v3.6--main')
if path not in sys.path:
    sys.path.insert(0, path)

# Configura la variable de entorno para Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'alertaduoc.settings'

# Obtén la aplicación WSGI de Django
application = StaticFilesHandler(get_wsgi_application())