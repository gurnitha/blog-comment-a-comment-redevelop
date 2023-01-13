## Redevelop Django Blog Comment a Comment 

Building a very complete blog application

Github link: https://github.com/gurnitha/blog-comment-a-comment-redevelop
My Learning link: https://www.udemy.com/course/python-django-masterclass/learn/lecture/


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


## 08. Counting and Recording Views 


#### 08.1 Adding view_count field to Post model

        modified:   README.md
        new file:   app/blog/migrations/0003_post_view_count.py
        modified:   app/blog/models.py

        Activities:

        1. Adding view_count field in Post model
        2. Run and apply migrations

        NEXT: Add view_count logic to detail_page view


#### 08.2 Adding view_count logic to detail_page view

        modified:   README.md
        modified:   app/blog/views.py
        
        Activities:

        1. Adding logic to detail_page view to count and save each time of a view

        NEXT: Counting and recording the views 


#### 08.3 Counting and recording the views 

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



## 09. User Comments


#### 09.1 Creating Comment model

        modified:   README.md
        modified:   app/blog/admin.py
        new file:   app/blog/migrations/0004_comments.py
        modified:   app/blog/models.py
        
        Activities:

        1. Creating Comment model
        2. Run and apply migrations
        3. Register Comment model to admin.py

        NEXT: Creating CommentForm model


#### 09.2 Creating CommentForm model

        modified:   README.md
        new file:   app/blog/forms.py
        
        Activities:

        1. Creating CommentForm model

        NEXT: Configuring comment in the detail_page view


#### 09.3 Configuring comment in the detail_page view

        modified:   README.md
        modified:   app/blog/forms.py
        modified:   app/blog/views.py
        
        Activities:

        1. Configuring comment logic in detail_page view
        2. Correnting import typos in form.py

        NEXT: Creating comments 


#### 09.4 Creating comments

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


#### 09.5 Rendering comments

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


#### 09.6 Fixing issue comment re-render and author image

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


#### 09.7 Building replies to comments - Part 1: Create parent field in Comment model

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
