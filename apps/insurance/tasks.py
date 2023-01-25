from Bimsanj.celery_conf import celery_app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@celery_app.task(name="send_message_insurance_reminder")
def send_message_insurance_reminder(title, mobile, due_date):
    logger.info('send message insurance reminder')
    # return send_reminder_message(title, mobile, due_date)
    return f'{title} _ {mobile} _ {due_date}'