# Generated by Django 4.0.3 on 2022-04-03 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='useralert',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AddField(
            model_name='alert',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_alerts', to=settings.AUTH_USER_MODEL, verbose_name='ایجاد کننده'),
        ),
    ]
