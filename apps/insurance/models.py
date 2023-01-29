from django.db import models
from apps.core.mixins import Timestampable
from apps.users.validators import MobileValidator
from django_celery_beat.models import PeriodicTask, IntervalSchedule, ClockedSchedule
from datetime import datetime, timedelta
import json
from jalali_date import date2jalali, datetime2jalali
from dateutil import relativedelta
import jdatetime


class InsuranceReminder(Timestampable, models.Model):
    class Meta:
        verbose_name = 'یادآوری بیمه'
        verbose_name_plural = 'یادآوری بیمه'
        ordering = ('-created_at', )

    class InsuranceReminderType(models.IntegerChoices):
        RUNNING = 0, 'در حال اجرا'
        EXPIRED = 1, 'منقضی شده'
        CANCELED = 2, 'لغو شده'

    title = models.CharField('عنوان یادآوری', max_length=255)
    user = models.ForeignKey('users.User', verbose_name='کاربر', null=True, blank=True,
                             on_delete=models.CASCADE, related_name='insurance_reminders')
    mobile = models.CharField("شماره تلفن", max_length=11, validators=[MobileValidator()])
    due_date = models.DateField('تاریخ سررسید')
    reminder_type = models.IntegerField('نوع یادآوری', choices=InsuranceReminderType.choices,
                                        default=InsuranceReminderType.RUNNING)
    remind_days_before = models.PositiveSmallIntegerField('روز قبل از سررسید', default=1)


    def create_reminder(self, date):
        reminder_time = datetime.strptime(str(date), "%Y-%m-%d")
        reminder_time += timedelta(hours=-15)
        schedule, _ = ClockedSchedule.objects.get_or_create(clocked_time=reminder_time)
        PeriodicTask.objects.update_or_create(
            name=f"Schedule for {self.title} - {self.mobile}",
            defaults={
                "task": "apps.insurance.tasks.send_message_insurance_reminder",
                "args": json.dumps([self.mobile, self.title, self.due_date],sort_keys = True, default = str),
                "clocked": schedule,
                "one_off": True,
            },
        )

class Insurance(Timestampable, models.Model):
    name = models.CharField(max_length=50, verbose_name='نام', unique=True)
    
    class Meta:
        verbose_name = 'شرکت بیمه'
        verbose_name_plural = 'شرکت بیمه'

    def __str__(self):
        return self.name
