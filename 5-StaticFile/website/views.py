from django.shortcuts import render

def index(request):
    context = {
        'title': 'Halaman Index',
    }
    return render(request, "index.html", context)

def about(request):
    context = {
        'title' : 'Halaman About',
    }
    return render(request, "about.html", context)