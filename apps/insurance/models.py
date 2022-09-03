from django.db import models
from apps.core.mixins import Timestampable
from apps.users.validators import MobileValidator


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


class Insurance(Timestampable, models.Model):
    name = models.CharField(max_length=50, verbose_name='نام', unique=True)
    
    class Meta:
        verbose_name = 'شرکت بیمه'
        verbose_name_plural = 'شرکت بیمه'

    def __str__(self):
        return self.name
