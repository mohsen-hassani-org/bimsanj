"""Bimsanj URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from .initial_setup import setup

setup()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.users.auth_urls', namespace='auth')),
    path('', include('apps.users.urls')),
    path('', include('apps.core.urls')),
    path('', include('apps.blog.urls')),
    path('', include('apps.insurance.urls')),
]
