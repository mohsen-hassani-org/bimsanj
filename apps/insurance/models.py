from math import remainder
from django.db import models
from django.contrib.auth import get_user_model

from apps.core.models import AbstractModel
from apps.users.validators import MobileValidator
User = get_user_model()


class InsuranceReminder(AbstractModel):
    class Meta:
        verbose_name = 'یادآوری بیمه'
        verbose_name_plural = 'یادآوری بیمه'
        ordering = ('-created_at', )

    class InsuranceReminderType(models.IntegerChoices):
        RUNNING = 0, 'در حال اجرا'
        EXPIRED = 1, 'منقضی شده'
        CANCELED = 2, 'لغو شده'

    title = models.CharField('عنوان یادآوری', max_length=255)
    user = models.ForeignKey(User, verbose_name='کاربر', null=True, blank=True,
                             on_delete=models.CASCADE, related_name='insurance_reminders')
    mobile = models.CharField("شماره تلفن", max_length=11, validators=[MobileValidator()])
    due_date = models.DateField('تاریخ سررسید')
    reminder_type = models.IntegerField('نوع یادآوری', choices=InsuranceReminderType.choices,
                                        default=InsuranceReminderType.RUNNING)
    remind_days_before = models.PositiveSmallIntegerField('روز قبل از سررسید', default=1)

