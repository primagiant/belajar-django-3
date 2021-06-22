from django.shortcuts import render

# Create your views here.
def post(request):
    context = {
        'title' : 'Halaman Index Blog',
    }
    return render(request, 'blog/index.html', context)