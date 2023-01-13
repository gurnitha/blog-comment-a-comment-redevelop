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


# VIEWS: detail_page
def detail_page(request, slug):
    post = Post.objects.get(slug=slug)
    # print(post)

    # Conting and recording the view
    if post.view_count is None:
    	post.view_count = 1
    else:
    	post.view_count = post.view_count + 1
    post.save()

    
    context = {
            'post':post,
    }
    return render(request, 'app/blog/detail.html', context)
