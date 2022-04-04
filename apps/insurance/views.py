from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin, UpdateModelMixin, RetrieveModelMixin,
    ListModelMixin, DestroyModelMixin
)
from .models import InsuranceReminder
from .serializers import InsuranceReminderSerializer

# Create your views here.

class InsuranceReminderView(GenericViewSet, CreateModelMixin):
    serializer_class = InsuranceReminderSerializer
    model = InsuranceReminder

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)