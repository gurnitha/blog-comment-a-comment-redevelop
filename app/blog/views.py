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
    # Get 3 most viewed post
    top_posts = Post.objects.all().order_by('-view_count')[0:3]
    print(top_posts)
    context = {
        'posts':posts,
        'top_posts':top_posts
    }
    return render(request, 'app/blog/index.html', context)


# VIEWS: detail_page
def detail_page(request, slug):

    # Post
    post = Post.objects.get(slug=slug)
    # print(post)

    # Comment
    comments = Comment.objects.filter(post=post)
    comments = Comment.objects.filter(post=post, parent=None)
    form = CommentForm()

    if request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid:
            parent_obj = None
            if request.POST.get('parent'):
                # save reply
                parent = request.POST.get('parent')
                parent_obj = Comment.objects.get(id=parent)

                if parent_obj:
                    comment_reply = comment_form.save(commit=False)
                    comment_reply.parent = parent_obj
                    comment_reply.post = post
                    comment_reply.save()
                    return HttpResponseRedirect(reverse('blog:detail', kwargs={'slug':slug}))
            else:
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
