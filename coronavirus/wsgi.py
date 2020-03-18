import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coronavirus.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

application = get_wsgi_application()
