from django.db import models
from django_quill.fields import QuillField
from django.conf import global_settings, settings
from django.urls import reverse
from django.db.models.constraints import UniqueConstraint
from django.db.models.functions import Lower
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from apps.core.mixins import Authorable, Timestampable, Publishable, LogicalDeletable, Permalinkable, SingletonMixin
from apps.users.models import User


class BlogManager(models.Manager):
    def get_blog_posts(self):
        return self.filter(status=self.model.PublishStatuses.PUBLISHED)


class PageManager(models.Manager):
    def get_published_pages(self):
        return self.filter(status=self.model.PublishStatuses.PUBLISHED)



class Tag(Timestampable, Permalinkable, models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات', blank=True)


class Category(Timestampable, Permalinkable, Publishable, models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات', blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='دسته بندی پدر')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی‌'
        ordering = ('-id',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}'


class Post(Timestampable, Permalinkable, Authorable, models.Model):
    class PublishStatuses(models.TextChoices):
        PUBLISHED = 'published', 'منتشر شده'
        DRAFTED = 'drafted', 'پیش نویس'

    title = models.CharField(max_length=255, verbose_name='عنوان')
    body = QuillField(verbose_name='متن', blank=True)
    summary = models.CharField(max_length=2048, verbose_name='خلاصه', blank=True)
    template_name = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی', related_name='posts', null=True, blank=True)
    tags = models.ManyToManyField(Tag, verbose_name='برچسب‌ها', blank=True, related_name='posts')
    image = models.ImageField(verbose_name='تصویر', upload_to='posts/')
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(300, 180)],
                                    format='JPEG', options={'quality': 60})
    status = models.CharField(max_length=10, choices=PublishStatuses.choices, default=PublishStatuses.DRAFTED)

    objects = BlogManager()

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post", kwargs={"slug": self.slug})
    


class Page(Timestampable, Permalinkable, Authorable, models.Model):
    
    class PublishStatuses(models.TextChoices):
        PUBLISHED = 'published', 'منتشر شده'
        DRAFTED = 'drafted', 'پیش نویس'

    title = models.CharField(max_length=255, verbose_name='عنوان')
    body = QuillField(verbose_name='متن', blank=True)
    template_name = models.CharField(max_length=255, blank=True)
    summary = models.CharField(max_length=2048, verbose_name='خلاصه', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی', related_name='pages', null=True, blank=True)
    tags = models.ManyToManyField(Tag, verbose_name='برچسب‌ها', blank=True, related_name='pages')
    image = models.ImageField(verbose_name='تصویر', upload_to='pages/', blank=True)
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(300, 180)],
                                    format='JPEG', options={'quality': 60})
    status = models.CharField(max_length=10, choices=PublishStatuses.choices, default=PublishStatuses.DRAFTED)
    objects = PageManager()
 
    class Meta:
        verbose_name = 'صفحه'
        verbose_name_plural = 'صفحه'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

        
class SiteSetting(SingletonMixin, Timestampable, models.Model):
    site_title = models.CharField(max_length=255, verbose_name='عنوان', default='Django Website')
    site_subtitle = models.CharField(max_length=255, verbose_name='زیر عنوان', blank=True)
    description = models.TextField(verbose_name='توضیحات', blank=True)
    author = models.CharField(max_length=255, blank=True, verbose_name='توضیحات')
    keywords = models.TextField(verbose_name='کلمات کلیدی', blank=True)
    home_page = models.ForeignKey(Page, on_delete=models.SET_NULL, verbose_name='صفحه خانه', blank=True, null=True)
    language = models.CharField(max_length=10, verbose_name='زبان', choices=global_settings.LANGUAGES, default='fa')
    is_rtl = models.BooleanField(default=False)
    logo = models.ImageField(verbose_name='لوگو', upload_to='logo/', blank=True)
    logo_thumbnail = ImageSpecField(source='logo', processors=[ResizeToFill(300, 180)],
                                    format='JPEG', options={'quality': 60})
    favicon = models.ImageField(verbose_name='فاویکون', upload_to='favicon/', blank=True)
    favicon_thumbnail = ImageSpecField(source='favicon', processors=[ResizeToFill(300, 180)],
                                    format='JPEG', options={'quality': 60})

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'

    @property
    def dir(self):
        return "rtl" if self.is_rtl else "ltr"

class ThemeContentManager(models.Manager):
    def theme_contents(self, theme=None):
        theme = theme or settings.BLOG_THEME
        return self.filter(theme=theme)

class ThemeContent(Timestampable, models.Model):
    theme = models.CharField(max_length=255, default='blog')
    key = models.SlugField(max_length=255)
    value = models.TextField(blank=True)
    objects = ThemeContentManager()

    class Meta:
        constraints = [
            UniqueConstraint(fields=['theme', 'key'], name='theme_key_unique_constraint')
        ]
        verbose_name = 'اطلاعات قالب'
        verbose_name_plural = 'اطلاعات قالب'

    def __str__(self):
        return f"({self.theme}) {self.key}: {self.value}"
