# app/blog/urls.py

# Import django modules
from django.urls import path

# Import from locals
from app.blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.home_page, name='home'),
]