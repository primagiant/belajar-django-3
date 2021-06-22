from django.shortcuts import render

def index(request):
    context = {
        'title': 'Halaman Index',
    }
    return render(request, "index.html", context)