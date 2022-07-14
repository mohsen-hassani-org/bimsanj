from django.core.cache import cache
from django.db import models
from django.urls import reverse


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

        
class SingletonModel(models.Model):
    """An abstract base class that provides a Singleton pattern for models."""
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)
        self._set_cache()

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj._set_cache()
        return cache.get(cls.__name__)

    def delete(self, *args, **kwargs):
        pass

    def _set_cache(self):
        cache.set(self.__class__.__name__, self)



class Alert(AbstractModel):
    class AlertType(models.TextChoices):
        INFO = 'info', 'اطلاعات'
        SUCCESS = 'success', 'موفقیت'
        WARNING = 'warning', 'توجه'
        DANGER = 'danger', 'اخطار'
        
    title = models.CharField('عنوان', max_length=255, null=True, blank=True)
    body = models.TextField('توضیحات', null=True, blank=True)
    action_link = models.CharField('لینک عملیات', max_length=255, null=True, blank=True)
    alert_type = models.CharField('نوع', max_length=10,
                                  choices=AlertType.choices,
                                  default=AlertType.INFO)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, verbose_name='ایجاد کننده',
                                   related_name='created_alerts', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:alert_details", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'هشدار'
        verbose_name_plural = 'هشدار'
        ordering = ('-created_at', )


class UserAlert(AbstractModel):
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE, verbose_name='هشدار', related_name='user_alerts')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='کاربر', related_name='alerts')
    seen_datetime = models.DateTimeField('تاریخ دیده شدن', null=True, blank=True)

    def __str__(self):
        return f"{self.alert.title} for {self.user.username}"

    def get_absolute_url(self):
        return reverse("core:user_alert_details", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'هشدار کاربر'
        verbose_name_plural = 'هشدار کاربر'
        ordering = ('-created_at',)

class CareerGroup(AbstractModel):
    name = models.CharField(verbose_name='نام', max_length=150)

    class Meta:
        verbose_name = 'گروه شغلی'
        verbose_name_plural = 'گروه شغلی'

    def __str__(self):
        return self.name


class Career(AbstractModel):
    name = models.CharField(verbose_name='نام', max_length=150)
    career_group = models.ForeignKey(CareerGroup, verbose_name='گروه',
                                     on_delete=models.PROTECT, related_name='careers')

    class Meta:
        verbose_name = 'شغل'
        verbose_name_plural = 'شغل'

    def __str__(self):
        return f'{self.name} ({self.career_group.name})' 


class State(AbstractModel):
    name = models.CharField(max_length=25, verbose_name='نام')

    class Meta:
        verbose_name = 'استان'
        verbose_name_plural = 'استان'

    def __str__(self):
        return self.name

    
class City(AbstractModel):
    name = models.CharField(max_length=25, verbose_name='نام')
    state = models.ForeignKey(State, on_delete=models.PROTECT, verbose_name='استان', related_name='cities')

    class Meta:
        verbose_name = 'شهر'
        verbose_name_plural = 'شهر'

    def __str__(self):
        return f"{self.name} ({self.state.name})"


class District(AbstractModel):
    name = models.CharField(max_length=25, verbose_name='نام')
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='شهر', related_name='districts')

    class Meta:
        verbose_name = 'ناحیه'
        verbose_name_plural = 'ناحیه'

    def __str__(self):
        return f"{self.name} ({self.city.name} - {self.city.state.name})"
