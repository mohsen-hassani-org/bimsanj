from rest_framework import serializers, exceptions, status
from .models import InsuranceReminder

class InsuranceReminderSerializer(serializers.ModelSerializer):
    due_date = serializers.DateField(input_formats=['%d/%m/%Y'])
    class Meta:
        model = InsuranceReminder
        fields = ('id', 'title', 'user', 'mobile', 'due_date', 'remind_days_before', 'reminder_type', 'created_at', 'updated_at')
        read_only_fields = ('id', 'reminder_type', 'created_at', 'updated_at')