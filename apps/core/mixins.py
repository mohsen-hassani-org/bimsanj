from functools import lru_cache
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.cache import cache


class SingletonMixin:
    """An abstract base class that provides a Singleton pattern for models."""

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonMixin, self).save(*args, **kwargs)
        self._set_cache()

    @classmethod
    def load(cls):
        if cache.get(cls.cache_key()) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj._set_cache()
        return cache.get(cls.cache_key())

    def delete(self, *args, **kwargs):
        pass

    def _set_cache(self):
        cache.set(self.cache_key(), self)

    @classmethod
    @lru_cache
    def cache_key(cls):
        return f"{cls.__module__}:{cls.__name__}"


class Timestampable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class LogicalDeletable(models.Model):
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save(update_fields=["is_deleted"])

    def restore(self):
        self.is_deleted = False
        self.save(update_fields=["is_deleted"])


class Activable(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def activate(self):
        self.is_active = True
        self.save(update_fields=["is_active"])

    def deactivate(self):
        self.is_active = False
        self.save(update_fields=["is_active"])


class Permalinkable(models.Model):
    slug = models.SlugField(unique=True, max_length=255)

    class Meta:
        abstract = True

    def get_url_kwargs(self, **kwargs):
        kwargs.update(getattr(self, "url_kwargs", {}))
        return kwargs

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.slug:
            self.slug = slugify(self.slug_source, allow_unicode=True)
        return super().save(force_insert, force_update, using, update_fields)

    @property
    def slug_source(self):
        assert hasattr(self, "title"), (
            "Your model doesn't have a 'title' attribute. Either create a title attribute"
            "of type char or override `self.slug_source()` function"
        )
        return self.title


class Publishable(models.Model):
    publish_date = models.DateTimeField(null=True, verbose_name="تاریخ انتشار")

    class Meta:
        abstract = True

    def publish_on(self, date=None):
        if not date:
            date = timezone.now()
        self.publish_date = date
        self.save(update_fields=["publish_date"])

    @property
    def is_published(self):
        return self.publish_date and self.publish_date < timezone.now()


class Authorable(models.Model):
    created_by = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, verbose_name="ایجاد کننده"
    )

    class Meta:
        abstract = True
