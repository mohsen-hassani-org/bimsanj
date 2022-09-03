from django.templatetags.static import static
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from apps.core.models import District
from apps.core.mixins import Timestampable
from apps.core.utils import generate_random_string
from apps.insurance.models import Insurance
from .validators import MobileValidator, NationalCodeValidator, PhoneValidator
from .managers import CustomUserManager


def generate_referral():
    code = generate_random_string(use_lower=False, use_symbols=False, length=8)
    users_code = User.objects.values('referral_code')
    while code in users_code:
        code = generate_random_string(use_lower=False, use_symbols=False, length=8)
    return code


class User(Timestampable, AbstractUser):
    """Custom User model"""
    class DeactivateReasons(models.IntegerChoices):
        UNKNOWN = 0, 'نامشخص'
        BY_ADMIN = 1, 'غیر فعال توسط مدیر'
        BY_STAFF = 2, 'غیر فعال توسط کارمندان'
        VERIFY_MOBILE = 3, 'عدم تایید موبایل'
        VERIFY_EMAIL = 4, 'عدم تایید ایمیل'
        
    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'مدیر'
        STAFF = 'STAFF', 'کارمند'
        PARTNER = 'PARTNER', 'پیمانکار'
        CLIENT = 'CLIENT', 'مشتری'

    mobile = models.CharField('موبایل', max_length=11, unique=True,
                              help_text='موبایل باید به فرمت 09123456789 وارد شود',
                              validators=[MobileValidator()],
                              error_messages={
                                  'unique': 'این شماره موبایل از قبل در سامانه ثبت شده است',
                              },
                              )
    first_name = models.CharField(verbose_name='نام', max_length=150, blank=True)
    last_name = models.CharField(verbose_name='نام خانوادگی', max_length=150, blank=True)
    national_code = models.CharField(max_length=10, verbose_name='کد ملی',
                                     validators=[NationalCodeValidator()],
                                     null=True, blank=True, unique=True)
    deactivate_reason = models.PositiveSmallIntegerField(choices=DeactivateReasons.choices,
                                                         default=DeactivateReasons.UNKNOWN,
                                                         verbose_name='غیرفعال به دلیل')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='تصویر پروفایل')
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name='ایمیل')
    role = models.CharField(max_length=10, choices=Roles.choices, default=Roles.CLIENT, verbose_name='نقش')
    notes = models.TextField(verbose_name='یادداشت', null=True, blank=True)
    referral_code = models.CharField(verbose_name='کد معرف', max_length=10, default=None, unique=True, null=True)
    career = models.ForeignKey('core.Career', on_delete=models.PROTECT, null=True, verbose_name='شغل')
    objects = CustomUserManager()

    REQUIRED_FIELDS = ["mobile", ]

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر'
        ordering = ('-id',)

    def __str__(self):
        return self.display_name

    def get_absolute_url(self):
        return reverse('users:user_details', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if self.email == '':
            self.email = None
        if not self.referral_code:
            self.referral_code = generate_referral()
        super().save(*args, **kwargs)

    @property
    def display_name(self):
        return (
            self.first_name + ' ' + self.last_name
            if self.first_name and self.last_name
            else self.mobile
        )

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        f = static('account/profile.png')
        return f

    def deactivate(self, reason: DeactivateReasons):
        """Deactivate user by reason

        DO NOT explicitly set users is_active field without saving the reason
        why it is deactivated
        """
        self.deactivate_reason = reason
        self.is_active = False
        self.save()

    def activate(self):
        """Activate user

        Will change user's deactivate reason to UNKNOWN
        """
        self.deactivate_reason = self.DeactivateReasons.UNKNOWN
        self.is_active = True
        self.save()

    def convert_to_client(self, commit=True):
        self.role = self.Roles.CLIENT
        if commit:
            self.save()

    def convert_to_partner(self, commit=True):
        self.role = self.Roles.PARTNER
        if commit:
            self.save()
        
    def convert_to_staff(self, commit=True):
        self.role = self.Roles.STAFF
        if commit:
            self.save()
        
    def convert_to_admin(self, commit=True):
        self.role = self.Roles.ADMIN
        if commit:
            self.save()

    @property
    def total_referred_users(self):
        return self.referrals.count()


class Admin(User):
    """Admin User model"""
    class Meta:
        proxy = True
    

class Staff(User):
    """Staff User model"""
    class Meta:
        proxy = True
      

class Client(User):
    """Client User model"""
    class Meta:
        proxy = True


class PartnerManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role=User.Roles.PARTNER)

    def create(self, **kwargs):
        user = super().create(**kwargs)
        user.role = User.Roles.PARTNER
        user.save()
        return user


class Partner(Timestampable, models.Model):
    """Partner User model"""
    class PartnerShipStatues(models.IntegerChoices):
        ACTIVE = 0, 'فعال'
        INFORMATION_REQUIRED = 1, 'در انتظار تکمیل اطلاعات'
        DOCUMENT_UPLOAD_REQUIRED = 2, 'در انتظار بارگذاری مدارک'
        VERIFICATION_REQUIRED = 3, 'در انتظار احراز هویت'
        DEACTIVE_UNKNOWN = 99, 'غیرفعال'

    user = models.OneToOneField(User, related_name='partner', unique=True, verbose_name='کاربر', on_delete=models.PROTECT)
    partnership_status = models.PositiveSmallIntegerField(verbose_name='وضعیت', choices=PartnerShipStatues.choices,
                                                          default=PartnerShipStatues.INFORMATION_REQUIRED)
    manager_first_name = models.CharField(max_length=50, verbose_name='نام مدیر')
    manager_last_name = models.CharField(max_length=50, verbose_name='نام خانوادگی مدیر')
    home_address = models.TextField(verbose_name='آدرس محل سکونت')
    home_phone = models.CharField(max_length=11, validators=[PhoneValidator], verbose_name='شماره تلفن محل سکونت')
    work_address = models.TextField(verbose_name='آدرس محل کار')
    work_phone = models.CharField(max_length=11, validators=[PhoneValidator], verbose_name='شماره تلفن محل کار')
    manager_mobile = models.CharField(max_length=11, validators=[MobileValidator], verbose_name='شماره همراه به نام خود شخص')
    insurance = models.ForeignKey(Insurance, verbose_name='شرکت بیمه‌ای', related_name='partners', on_delete=models.PROTECT)
    district = models.ForeignKey(District, verbose_name='ناحیه', on_delete=models.PROTECT, related_name='partners')
    code = models.CharField(max_length=10, verbose_name='کد نمایندگی')

    objects = PartnerManager()
    
    class Meta:
        verbose_name = 'همکار'
        verbose_name_plural = 'همکار'


class Referral(Timestampable, models.Model):
    referred = models.OneToOneField(User, verbose_name='گاربر معرفی شده',
                                    on_delete=models.PROTECT, unique=True,
                                    related_name='referral_by')
    referrer = models.ForeignKey(User, verbose_name='ارجاع دهنده',
                                 on_delete=models.PROTECT,
                                 related_name='referrals')


