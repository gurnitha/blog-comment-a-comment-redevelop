# app/blog/views.py

# Import django modules
from django.shortcuts import render

# Import from locals
from app.blog.models import Post 


# VIEWS: home_page
def home_page(request):
	posts = Post.objects.all()
	context = {
		'posts':posts,
	}
	return render(request, 'app/blog/index.html', context)
