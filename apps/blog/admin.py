from django.contrib import admin
from .forms import PageModelAdminForm
from .models import Post, Page, Category, SiteSetting, Tag, ThemeContent


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "summary_short",
        "status",
        "category",
        "created_by",
        "updated_at",
    )
    list_filter = ("status", "created_by", "created_at", "updated_at")
    search_fields = ("title", "slug", "summary", "body")
    readonly_fields = ("created_at", "updated_at", "created_by")

    def save_model(self, request, obj, form, change):
        if not obj.created_by_id:
            obj.created_by = request.user
        return super().save_model(request, obj, form, change)

    def summary_short(self, obj):
        return obj.summary[:100] + "..."


@admin.register(Page)
class PageAdmin(PostAdmin):
    prepopulated_fields = {"slug": ("title",)}
    fields = [
        "title",
        "slug",
        "body",
        "template_name",
        "summary",
        "category",
        "tags",
        "image",
        "status",
        "created_at",
        "updated_at",
        "created_by",
    ]
    form = PageModelAdminForm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "publish_date", "created_at", "updated_at")
    list_filter = (
        "created_at",
        "updated_at",
        "parent",
    )
    search_fields = (
        "title",
        "slug",
        "description",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = (
        "title",
        "slug",
        "description",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ("site_title", "site_subtitle", "created_at", "updated_at")

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ThemeContent)
class ThemeContentAdmin(admin.ModelAdmin):
    list_display = ("key", "value")
    fields = ("theme", "key", "value")

    def get_queryset(self, request):
        qs = self.model._default_manager.theme_contents()
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    def has_add_permission(self, request) -> bool:
        return True

    def has_delete_permission(self, request, obj=None):
        return False
