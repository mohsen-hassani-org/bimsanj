from celery import Celery
import os
from .settings import BROKER_URL, RESULT_BACKEND

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bimsanj.settings')

celery_app = Celery('Bimsanj')

# Load task modules from all registered Django apps.
celery_app.autodiscover_tasks()

celery_app.conf.broker_url = BROKER_URL
celery_app.conf.result_backend = RESULT_BACKEND
