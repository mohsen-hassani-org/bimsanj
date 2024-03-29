# Generated by Django 4.0.3 on 2022-04-12 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BigSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('subtitle', models.CharField(blank=True, max_length=255, verbose_name='زیر عنوان')),
                ('body', models.TextField(blank=True, verbose_name='متن')),
                ('image', models.ImageField(upload_to='big_slider', verbose_name='تصویر')),
                ('button_text', models.CharField(blank=True, max_length=255, verbose_name='متن دکمه')),
                ('button_link', models.CharField(blank=True, max_length=255, verbose_name='لینک دکمه')),
                ('text_position', models.CharField(choices=[('left', 'چپ'), ('right', 'راست'), ('center', 'مرکز')], default='center', max_length=255, verbose_name='موقعیت متن')),
                ('page', models.CharField(blank=True, help_text='اسلاگ صفحه\u200cای که این المان در آن نمایش داده می\u200cشود.\n                                         در صورتی که این فیلد خالی باشد،\n                                         در صفحه\u200cی اصلی نمایش داده می\u200cشود.', max_length=255, verbose_name='صفحه')),
                ('is_publish', models.BooleanField(default=False, verbose_name='منتشر شود؟')),
            ],
            options={
                'verbose_name': 'اسلایدر بزرگ',
                'verbose_name_plural': 'اسلایدر بزرگ',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('subtitle', models.CharField(blank=True, max_length=255, verbose_name='زیر عنوان')),
                ('thumbnail', models.ImageField(upload_to='features', verbose_name='تصویر کوچک')),
                ('button_text', models.CharField(blank=True, max_length=255, verbose_name='متن دکمه')),
                ('button_link', models.CharField(blank=True, max_length=255, verbose_name='لینک دکمه')),
                ('page', models.CharField(blank=True, help_text='اسلاگ صفحه\u200cای که این المان در آن نمایش داده می\u200cشود.\n                                         در صورتی که این فیلد خالی باشد،\n                                         در صفحه\u200cی اصلی نمایش داده می\u200cشود.', max_length=255, verbose_name='صفحه')),
                ('is_publish', models.BooleanField(default=False, verbose_name='منتشر شود؟')),
            ],
            options={
                'verbose_name': 'المان ویژگی',
                'verbose_name_plural': 'المان ویژگی',
                'ordering': ('-id',),
            },
        ),
    ]
