"""Bimsanj URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .initial_setup import setup
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


setup()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.users.auth_urls', namespace='auth')),
    path('', include('apps.users.urls')),
    path('', include('apps.core.urls')),
    path('', include('apps.blog.urls')),
    path('', include('apps.insurance.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
