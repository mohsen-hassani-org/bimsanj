from django import forms
from .models import InsuranceReminder


class InsuranceReminderForm(forms.ModelForm):
    class Meta:
        model = InsuranceReminder
        fields = ('title', 'mobile', 'due_date', 'remind_days_before')
        