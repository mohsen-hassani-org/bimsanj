# Generated by Django 4.0.6 on 2022-07-07 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_alter_bigslider_image_alter_feature_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='bigslider',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='feature',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('slug', models.SlugField(max_length=255, verbose_name='اسلاگ')),
                ('body', django_quill.fields.QuillField(blank=True, verbose_name='متن')),
                ('summary', models.CharField(blank=True, max_length=2048, verbose_name='خلاصه')),
                ('image', models.ImageField(upload_to='posts/', verbose_name='تصویر')),
                ('status', models.CharField(choices=[('published', 'منتشر شده'), ('drafted', 'پیش نویس')], default='drafted', max_length=10)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='ایجاد کننده')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
