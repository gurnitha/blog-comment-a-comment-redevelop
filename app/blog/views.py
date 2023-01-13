# app/blog/views.py

# Import django modules
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Import from locals
from app.blog.models import Post 
from app.blog.forms import CommentForm
from app.blog.models import Comment

# VIEWS: home_page
def home_page(request):
	posts = Post.objects.all()
	context = {
		'posts':posts,
	}
	return render(request, 'app/blog/index.html', context)


# VIEWS: detail_page
def detail_page(request, slug):

    # Post
    post = Post.objects.get(slug=slug)
    # print(post)

    # Comment
    comments = Comment.objects.filter(post=post)
    form = CommentForm
    if request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid:
            comment = comment_form.save(commit=False)
            postid = request.POST.get('post_id')
            post = Post.objects.get(id = postid)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('blog:detail', kwargs={'slug':slug}))


    # Conting and recording the view
    if post.view_count is None:
    	post.view_count = 1
    else:
    	post.view_count = post.view_count + 1
    post.save()
    
    context = {
        'post':post,
        'form':form,
        'comments':comments,
    }
    return render(request, 'app/blog/detail.html', context)
