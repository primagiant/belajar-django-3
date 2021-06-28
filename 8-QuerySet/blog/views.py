from django.shortcuts import render
from .models import Post


def post(request):
    posts = Post.objects.all()
    data = {
        'title': "Halaman Blog",
        'heading': "Selamat datang di Blog Post",
        'posts': posts,
    }
    return render(request, 'blog/post.html', data)


def berita(request):
    berita = Post.objects.filter(category='Berita')
    data = {
        'title': "Halaman Berita",
        'heading': "Selamat datang di Berita",
        'posts': berita,
    }
    return render(request, 'blog/berita.html', data)


def how_to(request):
    how_to = Post.objects.filter(category='How To')
    data = {
        'title': "Halaman How To",
        'heading': "Selamat datang di Halaman How To",
        'posts': how_to,
    }
    return render(request, 'blog/howto.html', data)


def gosip(request):
    gosip = Post.objects.filter(category='Gosip')
    data = {
        'title': "Halaman Gosip",
        'heading': "Gosip Hangat",
        'posts': gosip,
    }
    return render(request, 'blog/gosip.html', data)
