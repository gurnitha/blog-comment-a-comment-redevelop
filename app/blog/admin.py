# app/blog/admin.py

# Import django modules
from django.contrib import admin

# Import from locals
from app.blog.models import Post, Tag, Comment, Subscribe

class SubscribeAmin(admin.ModelAdmin):
	list_display = ['email', 'date']
	list_filter = ['date',] 

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Subscribe, SubscribeAmin)
