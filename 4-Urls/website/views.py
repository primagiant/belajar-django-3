from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Halaman Index")

def about(requestt):
    return HttpResponse("Halaman About")