"""
WSGI config for Food5 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/

WSGI/ASGI servers do not run manage.py:
When you run Django management commands (like runserver, migrate, etc.), manage.py is executed, and your environment variables are loaded if you call dotenv.load_dotenv() in manage.py.
But in production, your app is started by a WSGI/ASGI server, which loads your project via wsgi.py or asgi.py—not via manage.py.
"""

import os
from django.core.wsgi import get_wsgi_application
import dotenv
dotenv.load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Food5.settings')

application = get_wsgi_application()
