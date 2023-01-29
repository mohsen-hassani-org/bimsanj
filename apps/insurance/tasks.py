from Bimsanj.celery_conf import celery_app
from celery.utils.log import get_task_logger
from django_celery_beat.models import PeriodicTask, IntervalSchedule, ClockedSchedule
from datetime import datetime, timedelta
from uuid import uuid4

logger = get_task_logger(__name__)

@celery_app.task(name="apps.insurance.tasks.send_message_insurance_reminder")
def send_message_insurance_reminder(title, mobile, due_date):
    logger.info('send message insurance reminder')
    # return send_reminder_message(title, mobile, due_date)
    return f'{title} _ {mobile} _ {due_date}'