from django.contrib import admin


from .models import Post
from .models import Tag
from .models import Comment
from .models import Category


class CommentInlineAdmin(admin.TabularInline):
    model = Comment
    extra = 1


class PostAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'created_at', )
    list_display_links = ('id', 'title', )
    ordering = ('-id', '-created_at', )
    inlines = [CommentInlineAdmin]
    list_filter = ('tags', )
    search_fields = ('content', )
    date_hierarchy = 'created_at'


class TagAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'created_at')
    list_display_links = ('id', 'name', )
    list_filter = ('created_at', )
    search_fields = ('name', )
    date_hierarchy = 'created_at'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at', )
    list_display_links = ('id', 'name', )
    list_filter = ('created_at', )
    search_fields = ('name', )
    date_hierarchy = 'created_at'



admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)
admin.site.register(Category)
