import re
from django.core import validators
from django.utils.deconstruct import deconstructible

@deconstructible
class MobileValidator(validators.RegexValidator):
    regex = r'^09\d{9}$'
    message = "شماره موبایل باید به فرمت 09123456789 وارد شود"
    flags = 0

@deconstructible
class PhoneValidator(validators.RegexValidator):
    regex = r'^0\d{11}$'
    message = "تلفن ثابت باید با صفر شروع شده و ۱۱ رقم باشد"
    flags = 0

@deconstructible
class NationalCodeValidator(validators.RegexValidator):
    regex = r'^\d{10}$'
    message = 'کد ملی باید ده رقم باشد'
    flags = 0


