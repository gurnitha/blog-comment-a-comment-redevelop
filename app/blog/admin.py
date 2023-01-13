# app/blog/admin.py

# Import django modules
from django.contrib import admin

# Import from locals
from app.blog.models import Post, Tag, Comment


admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)