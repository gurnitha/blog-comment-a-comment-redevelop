# app/blog/admin.py

# Import django modules
from django.contrib import admin

# Import from locals
from app.blog.models import Post


admin.site.register(Post)