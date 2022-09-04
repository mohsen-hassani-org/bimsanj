from typing import Dict, Any
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView
from apps.insurance.forms import InsuranceReminderForm
from .models import Page, Post, SiteSetting



class ThemeMixin:
    def get_template_names(self):
        theme_prefix = settings.BLOG_THEME
        templates = []
        if hasattr(self, 'object') and self.object and self.object.template_name:
            templates = [f"{theme_prefix}/pages/{self.object.template_name}"]

        if not templates and self.template_name is None:
            raise ImproperlyConfigured(
                "You must define 'template_name' for blog views"
            )
        else:
            template_name = self.template_name
            templates += [
                f"{theme_prefix}/{template_name}",
                template_name,
            ]
            return templates


class HomeView(ThemeMixin, DetailView):
    def get(self, request, *args, **kwargs):
        settings = SiteSetting.load()
        if settings.home_page:
            self.queryset = Page.objects.filter(status=Page.PublishStatuses.PUBLISHED)
            self.object = self.queryset.get(slug=settings.home_page.slug)
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        return redirect("blog:posts")

        
class BlogView(ThemeMixin, ListView):
    template_name = 'base/post_list.html'
    queryset = Post.objects.filter(status=Post.PublishStatuses.PUBLISHED)
    context_object_name = 'posts'


class PostView(ThemeMixin, DetailView):
    template_name = 'base/post_details.html'
    queryset = Post.objects.filter(status=Post.PublishStatuses.PUBLISHED)
    context_object_name = 'post'


class PageView(ThemeMixin, DetailView):
    template_name = 'base/page_details.html'
    queryset = Page.objects.filter(status=Page.PublishStatuses.PUBLISHED)
    context_object_name = 'page'


   



