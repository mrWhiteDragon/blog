from django import forms
from .models import Category

class PostAddForm(forms.Form):
    title = forms.CharField(max_length=155)
    text = forms.CharField(widget=forms.Textarea)
    category = forms.ModelChoiceField(queryset=Category.objects.all())