# app/blog/forms.py

# Import django modules
from django import forms
from django.utils.translation import gettext_lazy as _

# Import from locals
from app.blog.models import Comment, Subscribe

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


class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields='__all__'
        # Remove lables
        labels = {'email':_('')}
    
    # Add placeholder text
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'