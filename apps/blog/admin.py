from django.contrib import admin
from .models import Post, Page, Category, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'summary_short', 'status', 'category', 'created_by', 'updated_at')
    list_filter = ('status', 'created_by', 'created_at', 'updated_at')
    search_fields = ('title', 'slug', 'summary', 'body')
    readonly_fields = ('created_at', 'updated_at', 'created_by')

    def save_model(self, request, obj, form, change):
        if not obj.created_by_id:
            obj.created_by = request.user
        return super().save_model(request, obj, form, change)

    def summary_short(self, obj):
        return obj.summary[:100] + '...'

@admin.register(Page)
class PageAdmin(PostAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish_date', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'parent', )
    search_fields = ('title', 'slug', 'description', )
    readonly_fields = ('created_at', 'updated_at',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'slug', 'description', )
    readonly_fields = ('created_at', 'updated_at',)


