# app/blog/views.py

# Import django modules
from django.shortcuts import render


# VIEWS: home_page
def home_page(request):
	return render(request, 'app/blog/index.html')
