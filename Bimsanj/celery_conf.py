from celery import Celery, signals
import os
from .settings import BROKER_URL, RESULT_BACKEND
from kombu import Queue

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bimsanj.settings')

celery_app = Celery('Bimsanj')

celery_app.conf.task_queues = (
    Queue('default', routing_key='default'),
    Queue('reminder', routing_key='reminder'),
)

celery_app.conf.task_default_queue = 'default'

celery_app.conf.task_routes = {
    'apps.insurance.tasks.send_message_insurance_reminder' : {'queue' : 'reminder'},
}

# Load task modules from all registered Django apps.
celery_app.autodiscover_tasks()

celery_app.conf.broker_url = BROKER_URL
celery_app.conf.result_backend = RESULT_BACKEND
