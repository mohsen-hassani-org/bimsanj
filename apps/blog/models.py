from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django_quill.fields import QuillField
from apps.core.models import AbstractModel, SingletonModel
from apps.users.models import User


class BlogManager(models.Manager):
    def get_blog_posts(self):
        return self.filter(status=self.model.PublishStatuses.PUBLISHED)


class PageManager(models.Manager):
    def get_published_pages(self):
        return self.filter(status=self.model.PublishStatuses.PUBLISHED)



class Tag(AbstractModel):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    slug = models.SlugField(max_length=255, verbose_name='اسلاگ', unique=True)
    description = models.TextField(verbose_name='توضیحات', blank=True)


class Category(AbstractModel):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    slug = models.SlugField(max_length=255, verbose_name='اسلاگ', unique=True)
    description = models.TextField(verbose_name='توضیحات', blank=True)
    is_publish = models.BooleanField(verbose_name='منتشر شود؟', default=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='دسته بندی پدر')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی‌'
        ordering = ('-id',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}'


class Post(AbstractModel):
    class PublishStatuses(models.TextChoices):
        PUBLISHED = 'published', 'منتشر شده'
        DRAFTED = 'drafted', 'پیش نویس'

    title = models.CharField(max_length=255, verbose_name='عنوان')
    slug = models.SlugField(max_length=255, verbose_name='اسلاگ', unique=True)
    body = QuillField(verbose_name='متن', blank=True)
    summary = models.CharField(max_length=2048, verbose_name='خلاصه', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی', related_name='posts', null=True, blank=True)
    tags = models.ManyToManyField(Tag, verbose_name='برچسب‌ها', blank=True, related_name='posts')
    image = models.ImageField(verbose_name='تصویر', upload_to='posts/')
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(300, 180)],
                                    format='JPEG', options={'quality': 60})
    status = models.CharField(max_length=10, choices=PublishStatuses.choices, default=PublishStatuses.DRAFTED)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='ایجاد کننده')

    objects = BlogManager()

    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Page(AbstractModel):
    
    class PublishStatuses(models.TextChoices):
        PUBLISHED = 'published', 'منتشر شده'
        DRAFTED = 'drafted', 'پیش نویس'

    title = models.CharField(max_length=255, verbose_name='عنوان')
    slug = models.SlugField(max_length=255, verbose_name='اسلاگ', unique=True)
    body = QuillField(verbose_name='متن', blank=True)
    summary = models.CharField(max_length=2048, verbose_name='خلاصه', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی', related_name='pages', null=True, blank=True)
    tags = models.ManyToManyField(Tag, verbose_name='برچسب‌ها', blank=True, related_name='pages')
    image = models.ImageField(verbose_name='تصویر', upload_to='posts/')
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(300, 180)],
                                    format='JPEG', options={'quality': 60})
    status = models.CharField(max_length=10, choices=PublishStatuses.choices, default=PublishStatuses.DRAFTED)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='ایجاد کننده')
    objects = PageManager()
 
    class Meta:
        verbose_name = 'صفحه'
        verbose_name_plural = 'صفحه'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

        
class SiteSetting(SingletonModel, AbstractModel):
    site_title = models.CharField(max_length=255, verbose_name='عنوان')
    site_subtitle = models.CharField(max_length=255, verbose_name='زیر عنوان')
    description = models.TextField(verbose_name='توضیحات', blank=True)
    keywords = models.TextField(verbose_name='کلمات کلیدی', blank=True)
    logo = models.ImageField(verbose_name='لوگو', upload_to='logo/')
    logo_thumbnail = ImageSpecField(source='logo', processors=[ResizeToFill(300, 180)],
                                    format='JPEG', options={'quality': 60})
    favicon = models.ImageField(verbose_name='فاویکون', upload_to='favicon/')
    favicon_thumbnail = ImageSpecField(source='favicon', processors=[ResizeToFill(300, 180)],
                                    format='JPEG', options={'quality': 60})
    footer_text = models.TextField(verbose_name='متن فوتر', blank=True)
    footer_logo = models.ImageField(verbose_name='لوگو فوتر', upload_to='logo/')
    footer_logo_thumbnail = ImageSpecField(source='footer_logo', processors=[ResizeToFill(300, 180)],
                                    format='JPEG', options={'quality': 60})
    footer_copyright = models.TextField(verbose_name='متن تمامی حقوق', blank=True)
    footer_address = models.TextField(verbose_name='آدرس', blank=True)
    footer_phone = models.CharField(max_length=255, verbose_name='تلفن', blank=True)
    footer_email = models.CharField(max_length=255, verbose_name='ایمیل', blank=True)
    home_page = models.ForeignKey(Page, on_delete=models.SET_NULL, verbose_name='صفحه خانه', blank=True, null=True)

   

