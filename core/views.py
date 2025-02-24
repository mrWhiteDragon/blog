from django.shortcuts import render
from .models import Post

def main(request):
    posts = Post.objects.all()

    return render(request,'main.html', {'posts': posts})

def post_add(request):
    return render(request, 'post_add.html')