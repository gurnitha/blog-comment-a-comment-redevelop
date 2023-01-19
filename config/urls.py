# config/urls.py

# Import django modules
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    
    # admin 
    path('admin/', admin.site.urls),
    
    # blog
    path('', include('app.blog.urls', namespace='blog')),

    # media files
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
