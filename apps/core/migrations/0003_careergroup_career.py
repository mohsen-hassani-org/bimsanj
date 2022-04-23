# Generated by Django 4.0.3 on 2022-04-23 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150, verbose_name='نام')),
            ],
            options={
                'verbose_name': 'گروه شغلی',
                'verbose_name_plural': 'گروه شغلی',
            },
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150, verbose_name='نام')),
                ('career_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='careers', to='core.careergroup', verbose_name='گروه')),
            ],
            options={
                'verbose_name': 'شغل',
                'verbose_name_plural': 'شغل',
            },
        ),
    ]
