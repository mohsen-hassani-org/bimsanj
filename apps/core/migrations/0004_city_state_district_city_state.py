# Generated by Django 4.0.3 on 2022-06-26 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_careergroup_career'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=25, verbose_name='نام')),
            ],
            options={
                'verbose_name': 'شهر',
                'verbose_name_plural': 'شهر',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=25, verbose_name='نام')),
            ],
            options={
                'verbose_name': 'استان',
                'verbose_name_plural': 'استان',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=25, verbose_name='نام')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='districts', to='core.city', verbose_name='شهر')),
            ],
            options={
                'verbose_name': 'ناحیه',
                'verbose_name_plural': 'ناحیه',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cities', to='core.state', verbose_name='استان'),
        ),
    ]
