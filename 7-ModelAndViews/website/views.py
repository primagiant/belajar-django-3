from django.shortcuts import render


def index(request):
    data = {
        'title': 'Halaman Home',
    }
    return render(request, 'index.html', data)
