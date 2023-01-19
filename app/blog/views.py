# app/blog/views.py

# Import django modules
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Import from locals
from app.blog.models import Post, Tag 
from app.blog.forms import CommentForm
from app.blog.models import Comment
from app.blog.forms import SubscribeForm

# VIEWS: home_page
def home_page(request):
    posts = Post.objects.all()
    # Get 3 most viewed post
    top_posts = Post.objects.all().order_by('-view_count')[0:3]
    # print(top_posts)
    recent_posts = Post.objects.all().order_by('-last_updated')[0:3]
    # print(recent_posts)

    # Featured posts
    featured_blog = Post.objects.filter(is_featured = True)
    # In case there more than one freatured posts, render the first one
    if featured_blog:
        featured_blog = featured_blog[0]

    # Using SubscribeForm
    subscribe_form = SubscribeForm
    # If something wrong, render None
    subscribe_successful = None 
    # If form submited
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            subscribe_successful = 'Subscribe successfully'
            # Clearing the form after submiting it
            subscribe_form = SubscribeForm()

    context = {
        'posts':posts,
        'top_posts':top_posts,
        'recent_posts':recent_posts,
        'subscribe_form':subscribe_form, 
        'subscribe_successful':subscribe_successful,
        'featured_blog':featured_blog,
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


# VIEWS: tag_page
def tag_page(request, slug):

    # Get single tag instance
    tag = Tag.objects.get(slug=slug)

    # Get 3 most viewed post by a spesific tag
    top_posts = Post.objects.filter(tags__in=[tag.id]).order_by('-view_count')[0:2]

    # Get 3 objects the most recent posts by a spesific tag
    recent_posts = Post.objects.filter(tags__in=[tag.id]).order_by('-last_updated')[0:3]

    # Get 3 objects of featured posts by a spesific tag
    featureds = Post.objects.filter(tags__in=[tag.id],is_featured = True).order_by('-view_count')[0:3]

    context = {
        'tag':tag,
        'top_posts':top_posts,
        'recent_posts':recent_posts,
        'featurals':featureds,
    }
    
    return render(request, 'app/blog/tag.html', context)