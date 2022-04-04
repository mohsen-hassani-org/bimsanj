from django.contrib.auth.mixins import LoginRequiredMixin
from apps.core.models import UserAlert
from apps.core.base import GenericModelListView

# Create your views here.

class AlertListView(LoginRequiredMixin, GenericModelListView):
    page_title = 'هشدارها'
    fields = ['alert__title', 'alert__body', 'created_at']
    field_labels = {
        'created_at': 'ایجاد شده در'
    }
    datetime_fields = ['created_at']

    def get_queryset(self):
        return UserAlert.objects.filter(user=self.request.user)