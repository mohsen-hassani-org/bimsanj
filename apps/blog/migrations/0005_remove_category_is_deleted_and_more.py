# Generated by Django 4.0.6 on 2022-09-03 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category_page_sitesetting_tag_delete_bigslider_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='category',
            name='is_publish',
        ),
        migrations.RemoveField(
            model_name='page',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='post',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='sitesetting',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='is_deleted',
        ),
        migrations.AddField(
            model_name='category',
            name='publish_date',
            field=models.DateTimeField(null=True, verbose_name='تاریخ انتشار'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
