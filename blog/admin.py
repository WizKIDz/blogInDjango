from django.contrib import admin

from .models import blog
class BlogAdmin(admin.ModelAdmin):
    fields = ['title', 'body', 'pub_date']

admin.site.register(blog, BlogAdmin)
