from django.shortcuts import render, redirect
from .models import Post

def main(request):
    posts = Post.objects.all()

    return render(request,'main.html', {'posts': posts})

def post_add(request):
    if request.method == 'POST':
        # print(request.POST)
        title = request.POST.get('title')
        text = request.POST.get('text')
        image = request.FILES.get('image')
        post = Post(title=title, text=text, image=image)
        post.save()

        return redirect('main')

    return render(request, 'post_add.html')