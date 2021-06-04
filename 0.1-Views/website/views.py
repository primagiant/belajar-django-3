from django.http import HttpResponse

def index(request):
    return HttpResponse("Ini Adalah Halaman Beranda")

def about(request):
    return HttpResponse("Ini Halaman About")