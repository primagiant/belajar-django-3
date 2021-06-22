from django.shortcuts import render
from .models import Post


def index(request):
    # ambil query set
    posts = Post.objects.all()
    data = {
        'title': "Halaman Blog",
        'posts': posts,
    }
    return render(request, 'blog/index.html', data)
