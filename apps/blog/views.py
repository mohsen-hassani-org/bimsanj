from typing import Dict, Any
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView
from apps.insurance.forms import InsuranceReminderForm
from .models import Page, Post, SiteSetting


THEME = settings.BLOG_THEME_PREFIX

class ThemeMixin:
    def get_template_names(self):
        if self.template_name is None:
            raise ImproperlyConfigured(
                "You must define 'template_name' for blog views"
            )
        else:
            template_name = self.template_name
            return [
                f"{THEME}/{template_name}",
                template_name,
            ]



class HomeView(ThemeMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        settings = SiteSetting.load()
        if settings.home_page:
            return redirect(settings.home_page)
        return redirect("blog:blog")

        
class BlogView(ThemeMixin, ListView):
    template_name = THEME + 'pages/blog.html'
    model = Post
    context_object_name = 'blog'


class PostView(ThemeMixin, DetailView):
    template_name = 'pages/post_details.html'
    queryset = Post.objects.filter(status=Post.PublishStatuses.PUBLISHED)
    context_object_name = 'post'


class PageView(ThemeMixin, DetailView):
    template_name = 'pages/page_details.html'
    queryset = Page.objects.filter(status=Page.PublishStatuses.PUBLISHED)
    context_object_name = 'page'

   



