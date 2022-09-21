import os
from django import forms
from django.conf import settings
from apps.blog.models import Page


class PageModelAdminForm(forms.ModelForm):
    template_name = forms.ChoiceField(label="قالب", required=True, choices=())

    class Meta:
        model = Page
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        theme_prefix = settings.BLOG_THEME
        templates = os.listdir(f"apps/{theme_prefix}/templates/{theme_prefix}/pages")
        choices = [(template, template) for template in templates]
        self.base_fields["template_name"].choices = choices
        super().__init__(*args, **kwargs)
