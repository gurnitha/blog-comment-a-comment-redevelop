## Redevelop Django Blog Comment a Comment 

Building a very complete blog application

Github link: https://github.com/gurnitha/blog-comment-a-comment-redevelop
My Learning link: https://www.udemy.com/course/python-django-masterclass/learn/lecture/


## Building Real World Project: A Blog Application - Getting Started


## 01. Project Setup

#### 01.1 Create virtual environment and install django 4.1


        F:\_workspace\blog\blog-comment-a-comment-redevelop (main)
        λ python -m venv venv3941
        λ venv3941\Scripts\activate.bat
        (venv3941) λ pip install django
        ...
        (venv3941) λ python.exe -m pip install --upgrade pip

        modified:   README.md

        Activities:

        1. Create virtual environment 'venv3941'
        2. Activate venv3941
        3. Install django
        4. Update pip


## 02. Create Django Project

#### 02.1 Create django project called 'config'

        (venv3941) λ django-admin startproject config .

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py

        Activities:

        1. Create django project


## 03. Create Django Application

#### 03.1 Create django app called 'blog'

        (venv3941) λ mkdir app\blog
        (venv3941) λ django-admin startapp blog app\blog

        modified:   README.md
        new file:   app/blog/__init__.py
        new file:   app/blog/admin.py
        new file:   app/blog/apps.py
        new file:   app/blog/migrations/__init__.py
        new file:   app/blog/models.py
        new file:   app/blog/tests.py
        new file:   app/blog/views.py

        Activities:

        1. Create folder app/blog
        2. Create django app inside the app folder

#### 03.2 Register the blog app to config

        modified:   README.md
        modified:   app/blog/apps.py
        modified:   config/settings.py

        Activities:

        1. In blog/apps.py, modified the app name to: name = 'app.blog'
        2. Register the blog app to settings.py
        3. Run the server to test it
        4. Result: It worked


## 04. Django Urls, Views and Templates

#### 04.1 Django hello world

        modified:   README.md
        new file:   app/blog/urls.py
        modified:   app/blog/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   templates/app/blog/index.html

        Activities:

        1. Create urls in:app/blog/urls.py
        2. Create home_page views
        3. Include the blog urls in config/urls.py
        4. Activate templates in settings.py
        5. Create folders and index file:templates/app/blog/index.html
        6. Add hellow world to index.html
        7. Run the server, and open in the browser: http://127.0.0.1:8000/blog/
        8. Result: Hellow World!

#### 04.2 Create the homepage

        modified:   README.md
        modified:   templates/app/blog/index.html

        Activities:

        1. Adding html template to index.html
        2. Refresh the browser

        NOTE:

        1. The page look ugly without styles

        NEXT: Add style to the home page

#### 04.3 Configure static files

        modified:   README.md
        modified:   templates/app/blog/index.html

        Activities:

        1. Adding assets to config
        
        NOTE: The page still look the same due to the assets did not load yet.

        NEXT: Load the static files or assets

#### 04.4 Configure static files

        modified:   README.md
        modified:   templates/app/blog/index.html

        Activities:

        1. Loading static files

        NOTE:

        1. It worked nicely. But we need to use django template inheritance

        NEXT: Use django template inheritance  


## 05. Django Templates Inheritance

#### 05.1 Create base template

        modified:   README.md
        modified:   templates/app/blog/index.html
        new file:   templates/base.html

        Activities:

        1. Create base template
        2. Extends base template in the index.html

        NOTE:

        1. It worked nicely.
        2. It need further separation to use django DRY

        NEXT: Use include and partials

#### 05.2 Include and partials

        modified:   README.md
        modified:   templates/app/blog/index.html
        modified:   templates/base.html
        new file:   templates/partials/footer.html
        new file:   templates/partials/header.html

        Activities:

        1. Create partials files
        2. Include the files in base.html

        NOTE:

        1. It works nicely.
        2. But the page title need to use django tags

        NEXT: Use django tags for the page title

#### 05.3 Page title

        modified:   templates/app/blog/index.html
        modified:   templates/base.html

        Activities:

        1. Adding tags title to base and index files

        NOTE:

        1. It works nicely
        2. But page still static.

        NEXT: Making the page dynamic by building Django Model


## 06. Django Models

#### 06.1 Creating Post model

        modified:   README.md
        modified:   app/blog/admin.py
        new file:   app/blog/migrations/0001_initial.py
        modified:   app/blog/models.py

        (venv3941) λ pip install pillow
        (venv3941) λ python manage.py makemigrations
        (venv3941) λ python manage.py migrate
        (venv3941) λ python manage.py createsuperuser
        Username (leave blank to use 'hp'): admin
        Email address: admin@admin.com
        Password: admin
        Password (again): admin
        The password is too similar to the username.
        This password is too short. It must contain at least 8 characters.
        This password is too common.
        Bypass password validation and create user anyway? [y/N]: y
        Superuser created successfully.        

        Activities:

        1. Create Post model
        2. Install pillow
        3. Run and apply migrations
        4. Create superuser
        5. Register Post model to admin
        6. Run the server: (venv3941) λ python manage.py runserver
        7. Testing: login admin: http://127.0.0.1:8000/admin/login/?next=/admin/
        8. Result: great

        NEXT: Creating and Rendering post to homepage


## 07. Django Pages

#### 07.1 Creating and rendering posts

        modified:   README.md
        modified:   app/blog/views.py
        new file:   images/post.png
        modified:   templates/app/blog/index.html

        Activities:

        1. Import Post model to view
        2. Get all the instance of the posts and put them in the context
        3. Render posts instance to the homepage
        4. Testing: refresh the browser
        5. Result: Image did not show up

        NEXT: Configure the media files

#### 07.2 Configuring media files

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   upload/images/post.png

        Activities:

        1. Confituring media files path in config/settings.py and in  config/urls.py
        2. Re-upload image in the admin panel for the posts
        3. Testing: reload browser
        4. Result: image showed up

        NEXT: Creating Detail Page

#### 07.3 Modified readme file 

        modified:   README.md

#### 07.4 Creating post detail page

        modified:   README.md
        modified:   app/blog/urls.py
        modified:   app/blog/views.py
        new file:   templates/app/blog/detail.html
        modified:   templates/app/blog/index.html

        Activities:

        1. Creating url path for post detail
        2. Creating detail_page view
        3. Creating detail page
        4. Render the post title on the page title
        5. Add links
        6. Testing: 
           - go to home page
           - refresh the browser
           - hover and click the post
        7. Result: it render the detail post page

        NEXT: Creating Tags


## 08. Creating Tags

#### 08.1 Creating Tag model

        modified:   README.md
        modified:   app/blog/admin.py
        new file:   app/blog/migrations/0002_tag_post_tags.py
        modified:   app/blog/models.py

        Activities:

        1. Creating Tag model
        2. Run and apply migrations
        3. Register Tag model to admin

        NEXT: Creating and rendering tags to post

#### 08.2 Creating and rendering tags to post

        modified:   README.md
        modified:   templates/app/blog/detail.html

        Activities:

        1. Render the tag to post detail page
        2. Testing: refresh the browser
        3. Result: tags rendered

        NEXT: Counting and Recording Views 


## 09. Counting and Recording Views 

#### 09.1 Adding view_count field to Post model

        modified:   README.md
        new file:   app/blog/migrations/0003_post_view_count.py
        modified:   app/blog/models.py

        Activities:

        1. Adding view_count field in Post model
        2. Run and apply migrations

        NEXT: Add view_count logic to detail_page view

#### 09.2 Adding view_count logic to detail_page view

        modified:   README.md
        modified:   app/blog/views.py
        
        Activities:

        1. Adding logic to detail_page view to count and save each time of a view

        NEXT: Counting and recording the views 

#### 09.3 Counting and recording the views 

        modified:   README.md
        modified:   templates/app/blog/detail.html
        
        Activities:

        1. Render the view_count on detail_page like this:
           {{ post.view_count }} view{{ post.view_count|pluralize }}
        2. Tesing:
           - refresh the page several times
           - each page refresh was counted as + 1 view
           - go to admin panel, make the view_count = 0
        3. Result: it make singular and plural views

        NEXT: User Comments


## 10. User Comments

#### 10.1 Creating Comment model

        modified:   README.md
        modified:   app/blog/admin.py
        new file:   app/blog/migrations/0004_comments.py
        modified:   app/blog/models.py
        
        Activities:

        1. Creating Comment model
        2. Run and apply migrations
        3. Register Comment model to admin.py

        NEXT: Creating CommentForm model

#### 10.2 Creating CommentForm model

        modified:   README.md
        new file:   app/blog/forms.py
        
        Activities:

        1. Creating CommentForm model

        NEXT: Configuring comment in the detail_page view

#### 10.3 Configuring comment in the detail_page view

        modified:   README.md
        modified:   app/blog/forms.py
        modified:   app/blog/views.py
        
        Activities:

        1. Configuring comment logic in detail_page view
        2. Correnting import typos in form.py

        NEXT: Creating comments 

#### 10.4 Creating comments

        modified:   README.md
        modified:   app/blog/migrations/0001_initial.py
        deleted:    app/blog/migrations/0002_tag_post_tags.py
        deleted:    app/blog/migrations/0003_post_view_count.py
        deleted:    app/blog/migrations/0004_comments.py
        modified:   app/blog/views.py
        modified:   templates/app/blog/detail.html
        new file:   upload/images/post_IwvPFq8.png

        Activities:

        1. Rendering form instance from the detail_page view to detail page
        2. Testing: create a comment
        3. Error found after submiting the form, it says: no such table: blog_comment

        Solution to poin 3:

        1. Remove all the migrations files
        2. Delete db.sqlite3 db
        3. Run and apply again migrations
        4. Create superuser
        5. Add post from the admin panel 
        6. Add tag from the admin panel 
        7. Open post and select tag in admin panel 

        Resutl: 

        1. Comments could save in db.
        2. But comments does not appear in the post detail page.

        NEXT: Rendering comments

#### 10.5 Rendering comments

        modified:   README.md
        modified:   app/blog/views.py
        modified:   templates/app/blog/detail.html

        Activities:

        1. Use the Comment model in detail_page view and get its instances
        2. Render the comment instances to post detail page
        3. Testing: creating new comment
        4. Result:  comments rendered.

        NOTE:

        1. A new comment re-render when refresh the browser
        2. Author image does not show up, because there is no author image in the Comment model.

        NEXT: Fixing the issues

#### 10.6 Fixing issue comment re-render and author image

        modified:   README.md
        modified:   app/blog/views.py

        Activities:

        1. In detail_page views, do these import django modules:
           from django.http import HttpResponseRedirect
           from django.urls import reverse 
        2. In detail_page view, add this after the line comment.save():
           return HttpResponseRedirect(reverse('blog:detail', kwargs={'slug':slug}))
        3. Loading static image for the author's comment
        4. Testing: submit a new comment
        5. Result: the comment render correctly and not re-render again.

        NOTE:

        1. So far, we can comment a post or posts.
        2. But we coult not yet been able to reply to a comment or commnents.

        NEXT: Building replies

#### 10.7 Building replies to comments - Part 1: Create parent field in Comment model

        modified:   README.md
        new file:   app/blog/migrations/0002_comment_parent.py
        modified:   app/blog/models.py
        modified:   app/blog/views.py
        modified:   templates/app/blog/detail.html

        Activities:

        1. Create a new field in Comment model called parent which reference the Comment model itself.
        2. Run and apply migrations.
        3. Testing: added a comment from admin panel refering a post and comment as perent.
        4. Result: It worked.

        NEXT: Allowing users to leave comments

#### 10.8 Building replies to comments - Part 2: Configuring logic in detail_page view

        modified:   README.md
        modified:   app/blog/views.py

        Activities:

        1. Configure the logic in detail_page view to allow reply to comments.
        2. Tesing: re run the server
        3. Result: ok

        NEXT: Allowing users to leave comments

#### 10.9 Building replies to comments - Part 3: Rendering form instance to allow users to reply comments

        modified:   README.md
        modified:   templates/app/blog/detail.html

        Activities:

        1. Rendering the form instance of the detail_page view
        2. Testing: reply to a comment
        3. Result: It worked, but it did not show the reply.

        NEXT: Rendering replies

#### 10.10 Building replies to comments - Part 4: Rendering replies

        modified:   README.md
        modified:   templates/app/blog/detail.html


## 11 Section Summary


        Hello guys. Welcome to this class.
        So in this lecture, we will be doing a section overview.
        So far, we have made a really good progress with our blog application.
        So in this section, we will be going a bit further
        and we will be adding
        more features into our blog application.

        After completing this section,
        you would have made a really good progresson your blog application.
        So, here's what we are going to covers.

        So we will be finishing the home page, the tags page
        and the authors page.

        So we still have some development that is to be done on the homepage.
        Our application does not have a tags page and a dedicated
        authors page, so we will be setting that up in this section.

        What will we learn?
        -------------------

        1. We will be finishing the homepage, tags page, author page.
        2. We will learn, how can you allow users to search on your website?

                Search is a basic functionality in today's
                modern web application. So if you're building any 
                website that has lots of posts,
                lots of products or anything,
                it's mandatory that you should have search,
                which will allow users to discover what they want.

        3. And then, we will learn, how can you render HTML content in the post.
                So right now,
                our post consists of just text,
                so you cannot have formatting like bold, italics and so on.
                So, we will be learning, how can you render HTML content
                to make your post well formatted.

        So that's what we are going to cover and I'm excited to see you inside.
        Thank you.


## Building Real World Project: A Blog Application - Building More Features


## 12. Homepage

#### 12.1 Displaying popular posts on homepage

        modified:   app/blog/views.py
        modified:   templates/app/blog/index.html
        new file:   upload/images/post-1.png
        new file:   upload/images/post-3.png
        new file:   upload/images/post-4.png

        Activities:

        1. Configure to load 3 most viewed post, like this
           top_posts = Post.objects.all().order_by('-view_count')[0:3]
        2. Render them to homepage.
           
           Note about rendering tag: 
           <!-- post.tags.all()[0].name -->
           <div class="tag">{{post.tags.all.0.name|capfirst}}</div>

        NEXT: Rendering 3 newest posts

#### 12.2 Displaying most recent posts on homepage

        modified:   README.md
        modified:   app/blog/views.py
        modified:   templates/app/blog/index.html

        NOTE: Almost the same as 12.1

        NEXT: Making users to subscribe

#### 12.2 Subscribe - Part 1: Create Subscribe model

        modified:   README.md
        modified:   app/blog/admin.py (register Subscribe model)
        new file:   app/blog/migrations/0003_subscribe_alter_post_tags.py (run and apply migrations)
        modified:   app/blog/models.py (create Subscribe model)

#### 12.3 Subscribe - Part 2: Create SubscribeForm model

        modified:   README.md
        modified:   app/blog/forms.py (Create SubscribeForm model)

#### 12.4 Subscribe - Part 3: Using SubscribeForm model in indev views

        modified:   README.md
        modified:   app/blog/views.py (Use SubscribeForm in index view and add logic to it)

#### 12.5 Subscribe - Part 4: Rendering subscribe_form instance to home page

        modified:   README.md
        modified:   templates/app/blog/index.html (render subscribe_form instance)

#### 12.6 Subscribe - Part 5: Configure Subscribe table display in admin panel

        modified:   README.md
        modified:   app/blog/admin.py

#### 12.7 Configuring and rendering featured posts

        modified:   README.md
        new file:   app/blog/migrations/0004_post_is_featured.py (run and apply migrations)
        modified:   app/blog/models.py (add is_featured boolean field)
        modified:   app/blog/views.py (add logic to get the featured post instance)
        modified:   templates/app/blog/index.html (render the featured blog instances)


## 13. Tags

#### 13.1 Tag - Part 1: Creating tag page

        modified:   README.md
        modified:   app/blog/urls.py
        modified:   app/blog/views.py
        new file:   templates/app/blog/tag.html

#### 13.2 Tag - Part 2: Adding html template to tag page 

        modified:   README.md
        modified:   templates/app/blog/tag.html

#### 13.3 Tag - Part 3: Get a tag object and reder it to tag page

        modified:   README.md
        modified:   app/blog/views.py (get a tag object)
        modified:   templates/app/blog/tag.html (reder it to tag page)

#### 13.4 Tag - Part 4: Get 2 objects of the most viewed posts by a spesific tag

        modified:   README.md
        1. Add logic
        modified:   app/blog/views.py

        # Get 2 objects of the most viewed posts by a spesific tag
        top_posts = Post.objects.filter(tags__in=[tag.id]).order_by('-view_count')[0:2]

        2. Reder the object
        modified:   templates/app/blog/tag.html

#### 13.5 Tag - Part 5: Get 3 objects of the most recent posts by a spesific tag

        modified:   README.md
        1. Add logic
        modified:   app/blog/views.py

        # Get 3 objects the most recent posts by a spesific tag
        recent_posts = Post.objects.filter(tags__in=[tag.id]).order_by('-last_updated')[0:3]

        2. Render objects
        modified:   templates/app/blog/tag.html

#### 13.6 Tag - Part 6: Get 3 objects of the featured posts by a spesific tag

        modified:   README.md
        1. Add logic
        modified:   app/blog/views.py

        # Get 3 objects of featured posts by a spesific tag
        featureds = Post.objects.filter(tags__in=[tag.id],is_featured = True).order_by('-view_count')[0:3]

        2. Render objects
        modified:   templates/app/blog/tag.html

#### 13.7 Tag - Part 7: Get and render all tags

        modified:   README.md
        modified:   app/blog/views.py
        modified:   templates/app/blog/tag.html

#### 13.8 Tag - Part 8: Showing posts by tag from tag's link in post detail

        modified:   README.md
        1. Modified blog path
        modified:   config/urls.py (removed 'blog/')

        2. Add post's link by tag
        modified:   templates/app/blog/detail.html

        {% for tag in post.tags.all %}
                # It will show something like this:
                # http://127.0.0.1:8000/tag/django
                <a class="tag" href="{% url 'blog:tag_page' tag.slug %}">{{tag.name}}</a>
        {% endfor %}

#### 13.9 Tag - Part 9: Add link to posts by tag and dynamic page title

        modified:   README.md

        1. Add link to posts by tag
        modified:   templates/app/blog/index.html

          {% if recent_posts %}
          {% for recent_post in recent_posts %} 
          <!-- card -->
            <div class="card">
              <div class="post-img">
                <a href="{% url 'blog:detail' recent_post.slug %}">
                <img src="{{ recent_post.image.url }}" alt="" />
              </a>
                {% if recent_post.tags %}
                {% for tag in recent_post.tags.all %}
                  <!-- post.tags.all()[0].name -->
                  <a class="tag" href="{% url 'blog:tag_page' tag.slug %}"> {{recent_post.tags.all.0.name|capfirst}}
                  </a>
                {% endfor %}
                {% endif %}
              </div>
              <div class="card-content">
                <h3>
                  <a href="{% url 'blog:detail' recent_post.slug %}">
                  {{ recent_post.title }}
                  </a>
                </h3>
                <div class="author">
                  <div class="profile-pic">
                    <img src="{% static 'assets/images/author.svg' %}" alt="" />
                  </div>
                  <div class="details">
                    <p>{{ recent_post.autor }}</p>
                    <small>{{ recent_post.date }}</small>
                  </div>
                </div>
              </div>
            </div>
          <!-- card end-->
          {% endfor %}
          {% endif %}

        modified:   templates/app/blog/tag.html
        modified:   templates/partials/header.html

#### 13.10 Modified readme file 

        modified:   README.md


## 14. Author

        modified:   README.md

#### 14.1 Create Profile model

        modified:   README.md
        modified:   app/blog/admin.py (register model)
        new file:   app/blog/migrations/0005_profile.py (run and apply migrations)
        modified:   app/blog/models.py (create Profile model)
        new file:   upload/images/ing.jfif (create a profile from admin panel)

#### 14.2 Add author field in Post model

        modified:   README.md
        new file:   app/blog/migrations/0006_post_author.py (run and apply migrations)
        modified:   app/blog/models.py (add author field)
        >> author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

#### 14.3 Render the author name and image in home page

        modified:   README.md
        1. Render author last_name and profile_image
        modified:   templates/app/blog/index.html

        <!-- 
            The way how to render author last_name and its profile_image

            Post model, has author field: author = models.ForeignKey(User, ..
            Profile model, has profile_image field: profile_image = models.ImageField
            To get the author image: {{recent_post.author.profile.profile_image.url}}
            1. use the var instance, 2. author field in Post model, 3. go to Profile model, 4. use profile_image
            recent_post>>author field>>profile model>>profile_image field>>url
        -->
        (venv3941) λ python manage.py shell
        ...

        In [1]: from app.blog.models import Post

        In [2]: post_1 = Post.objects.get(id=1)

        In [3]: post_1
        Out[3]: <Post: Post object (1)>

        In [4]: post_1.author
        Out[4]: <User: admin>

        In [5]: post_1.author.profile_image
        ---------------------------------------------------------------------------
        AttributeError                            Traceback (most recent call last)
        <ipython-input-5-f57fdaf87e90> in <module>
        ----> 1 post_1.author.profile_image

        AttributeError: 'User' object has no attribute 'profile_image'

        In [6]: post_1.author.profile.profile_image
        Out[6]: <ImageFieldFile: images/ing.jfif>

        In [7]: exit()

#### 14.4 Render the author's username and profile_image in tag page

        modified:   README.md

        1. Render author's username
        modified:   templates/app/blog/tag.html

        <!--  
              How to render author username, first_name or last_name ?

              <p>{{top_post.author.username}}</p>

              use: 
              var instance + author field in Post model 
              + (username, first_name, or last_name from the default User model)
        -->

        2. Rendering author's profile_image:

        var instance + author field in Post model + Profile model + profile_image + url

        <img src="{{top_post.author.profile.profile_image.url}}" alt="" />

#### 14.5 Building author page - Part 1: Create static page

        modified:   README.md

        1. Create path
        modified:   app/blog/urls.py
        path('author/<slug:slug>',views.author_page,name='author_page'),

        2. Create author_page view
        modified:   app/blog/views.py
        # VIEWS: author_page
        def author_page(request, slug):
                return render(request, 'app/blog/author.html')

        3. Create author page
        new file:   templates/app/blog/author.html

        4. Testing
        http://127.0.0.1:8000/author/1

        5. Result :)

#### 14.6 Building author page - Part 2: Adding htmal template

        modified:   README.md
        modified:   templates/app/blog/author.html

#### 14.7 Building author page - Part 3: Rendering user and bio based on Profile model

        modified:   README.md

        1. Use and get user
        modified:   app/blog/views.py
        profile = Profile.objects.get(slug=slug)

        2. Render user and bio
        modified:   templates/app/blog/author.html
        {{profile.user|capfirst}}
        {{profile.bio|capfirst}}

        3. Testing
        url/path/slug
        http://127.0.0.1:8000/author/admin

        4. Result :)

#### 14.8 Building author page - Part 4: Rendering 2 most viewed posts by a spesific author

        modified:   README.md
        modified:   app/blog/views.py
        modified:   templates/app/blog/author.html

#### 14.9 Building author page - Part 5: Rendering 3 most recent posts by a spesific author

        modified:   app/blog/views.py
        modified:   templates/app/blog/author.html

#### 14.10 Building author page - Part 6: Rendering 3 feature posts by a spesific author

        modified:   README.md
        modified:   app/blog/views.py
        modified:   templates/app/blog/author.html

#### 14.11 Building author page - Part 7: Using the sourcecodes for the author_page view

        modified:   README.md

        1. Change the codes
        modified:   app/blog/views.py
        modified:   templates/app/blog/author.html
        new file:   upload/images/darling.PNG
        new file:   upload/images/darling_oMZdrV9.PNG
        new file:   upload/images/post-2.png

        NOTE: 

        1. It worked in the author.html
        2. Next to render the top authors 

#### 14.12 Building author page - Part 8: Showing the top authors

        modified:   README.md

        1. Get the top_authors
        modified:   app/blog/views.py
        top_authors = User.objects.annotate(number=Count('post')).order_by('-number') 

        2. Render it to author page
        modified:   templates/app/blog/author.html

#### 14.13 Building author page - Part 9 (2): Showing the top authors

        modified:   README.md
        new file:   app/blog/migrations/0007_profile_tags.py
        modified:   app/blog/models.py
        modified:   app/blog/views.py
        modified:   templates/app/blog/author.html

        NOTE:

        1. Working file is: 14.2 - Part 9(2)
        2. I shows top author and its posts

        3. But the posts are not linking to show detail page.

        NEXT:

        Link the posts to detail page with slug flag.

#### 14.14 Building author page - Part 10: Link the posts to detail page with slug flag

        modified:   app/blog/views.py
        modified:   templates/app/blog/author.html

        NOTE:

        Successfully display detail page for Top Posts and Trendy :)


#### 14.15 Building author page - Part 11: Showing feature posts, author name and bio 

        modified:   README.md
        modified:   app/blog/views.py
        modified:   templates/app/blog/author.html

        NOTE:

        1. Successfully display:

           1.1 Author name and bio 
           1.2 Feature posts by author