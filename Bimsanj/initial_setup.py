from django.contrib import admin
from django.contrib.auth.models import Group


def setup():
    """Setup initial configuration for the project."""
    admin.site.unregister(Group)
    override_admin_panel_defaults()


def override_admin_panel_defaults():
    """Change values in django admin panel UI."""
    admin.site.site_header = "سامانه خدمات بیمه بیمسنج"
    admin.site.site_title = "سامانه خدمات بیمه بیمسنج"
    admin.site.index_title = "پنل مدیریت"
