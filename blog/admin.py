from django.contrib import admin
from blog.models import Blog



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'count')
    list_filter = ('status',)
    search_fields = ('title', 'status')