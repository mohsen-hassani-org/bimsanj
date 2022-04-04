from django.urls import path, include
from rest_framework import routers
from .views import InsuranceReminderView

app_name = 'insurance'

reminder_router = routers.DefaultRouter()
reminder_router.register(r'reminders', InsuranceReminderView, basename='reminders')

urlpatterns = [
    path('api/', include(reminder_router.urls)),
]
