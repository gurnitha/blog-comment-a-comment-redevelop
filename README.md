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