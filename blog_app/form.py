from django import forms
from django.forms import widgets
from .models import BlogPost

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fileds = ['text']
        labels = {'text':''}
        widgets = {'text' : forms. Textarea(attrs={'cols' : 100})}