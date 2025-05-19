from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent', 'is_enable', 'created_at', 'updated_at')
    list_filter = ('is_enable',)
    search_fields = ('title',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_enable', 'created_at', 'updated_at')
    list_filter = ('is_enable',)
    search_fields = ('title',)
    # filter_horizontal = ['categories']
    
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_enable', 'created_at', 'updated_at')
    list_filter = ('is_enable',)
    search_fields = ('title',)