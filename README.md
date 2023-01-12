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
