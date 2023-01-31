from rest_framework import serializers, exceptions, status
from .models import InsuranceReminder
import jdatetime

class InsuranceReminderSerializer(serializers.ModelSerializer):
    due_date = serializers.DateField(input_formats=['%Y/%m/%d'])
    class Meta:
        model = InsuranceReminder
        fields = ('id', 'title', 'user', 'mobile', 'due_date', 'remind_days_before', 'reminder_type', 'created_at', 'updated_at')
        read_only_fields = ('id', 'reminder_type', 'created_at', 'updated_at')
        
    def validate_due_date(self, value):
        request = self.context.get("request")
        value = request.data['due_date']
        j_year, j_month, j_day = [int(x) for x in value.split('/')]
        date = jdatetime.date(j_year, j_month, j_day).togregorian()
        return date