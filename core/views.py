from django.shortcuts import render, redirect
from .models import Post, Category

def main(request):
    posts = Post.objects.all()
    categories = Category.objects.all()

    return render(request,'main.html', {'posts': posts, 'categories': categories})

def post_add(request):
    error = ''
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        image = request.FILES.get('image')
        category = request.POST.get('category')

        category = Category.objects.get(title=category)

        if  title != '':
            post = Post(title=title, text=text, image=image,  category=category)
            post.save()

            return redirect('main')

        else:
            error = 'Ошибка. Заполните поле "Заголовок"'

    categories = Category.objects.all()

    return render(request, 'post_add.html', {'categories': categories, 'error': error})