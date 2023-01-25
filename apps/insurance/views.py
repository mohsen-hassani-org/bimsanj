from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin, UpdateModelMixin, RetrieveModelMixin,
    ListModelMixin, DestroyModelMixin
)
from .models import InsuranceReminder
from .serializers import InsuranceReminderSerializer
from datetime import datetime, timedelta
from .tasks import send_message_insurance_reminder

# Create your views here.

class InsuranceReminderView(GenericViewSet, CreateModelMixin):
    serializer_class = InsuranceReminderSerializer
    model = InsuranceReminder

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        eta = datetime.now() + timedelta(seconds=10)
        task = send_message_insurance_reminder.signature(
            (serializer.validated_data['title'],
            serializer.validated_data['mobile'],
            serializer.validated_data['due_date']))
        task.apply_async()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)