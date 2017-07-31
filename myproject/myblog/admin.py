from django.contrib import admin

# Register your models here.
from .models import Category, Tag, Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','createdTime')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Tag)
