from django.contrib import admin

from blog.models import BlogMainPage, BlogItem, BlogTag, BlogImage


class BlogImageInline(admin.TabularInline):
    model = BlogImage
    max_num = 9

class BlogMainPageAdmin(admin.ModelAdmin):
    model = BlogMainPage
    list_display = ['title', 'description', 'keyword']

class BlogItemAdmin(admin.ModelAdmin):
    list_display = ['title',  'content']
    inlines = [BlogImageInline]


admin.site.register(BlogItem, BlogItemAdmin)
admin.site.register(BlogMainPage)
admin.site.register(BlogTag)