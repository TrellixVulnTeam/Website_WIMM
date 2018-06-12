from django.contrib import admin
from .models import BlogType, Blog, ReadNum

@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog_type', 'author', 'created_time', 'lsat_updated_time')

@admin.register(ReadNum)
class ReadnumAdmin(admin.ModelAdmin):
    list_display = ('read_num', 'blog')