from django import forms
from .models import Post

class PostAddForm(forms.Form):
    model = Post
    fields = '__all__'