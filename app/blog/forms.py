# app/blog/forms.py

# Import django modules
from django import forms

# Import from locals
from app.blog.models import Comment

class CommentForm(forms.ModelForm):
	# Creating form field based on the Comment model fields
    class Meta:
        model = Comment
        fields = {'content','email','name','website'}
    
    # Adding widgets to form input
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['placeholder'] = 'Type your comment....'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['website'].widget.attrs['placeholder'] = 'Website'