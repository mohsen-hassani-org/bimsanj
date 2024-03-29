# Generated by Django 4.0.3 on 2022-04-03 12:46

import apps.users.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceReminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='عنوان یادآوری')),
                ('mobile', models.CharField(max_length=11, validators=[apps.users.validators.MobileValidator()], verbose_name='شماره تلفن')),
                ('due_date', models.DateField(verbose_name='تاریخ سررسید')),
                ('reminder_type', models.IntegerField(choices=[(0, 'در حال اجرا'), (1, 'منقضی شده'), (2, 'لغو شده')], default=0, verbose_name='نوع یادآوری')),
                ('remind_days_before', models.PositiveSmallIntegerField(default=1, verbose_name='روز قبل از سررسید')),
            ],
            options={
                'verbose_name': 'یادآوری بیمه',
                'verbose_name_plural': 'یادآوری بیمه',
                'ordering': ('-created_at',),
            },
        ),
    ]
