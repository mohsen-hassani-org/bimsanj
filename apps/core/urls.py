from django.urls import path
from .views import AlertListView
app_name = 'core'

urlpatterns = [
    path('alerts/', AlertListView.as_view(), name='alerts'),
]
