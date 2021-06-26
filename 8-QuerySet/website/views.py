from django.shortcuts import render


def index(request):
    data = {
        'title': "Halaman Home",
        'heading': "Halaman Home Index",
    }
    return render(request, 'index.html', data)
