"""
WSGI config for paparajotesybellotas project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ papybell_django_settings }}")


# Activate your virtual env
sys.path.append('{{ papybell_venv }}/lib/python3.6/site-packages/')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

