from django.shortcuts import render


def index(request):
    data = {
        'title': "Halaman Blog",
        'heading': "Selamat datang di Blog",
    }
    return render(request, 'blog/index.html', data)


def post(request):
    data = {
        'title': "Halaman Blog Post",
        'heading': "Selamat datang di Blog Post",
    }
    return render(request, 'blog/post.html', data)
