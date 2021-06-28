from django.urls import path

from . import views

urlpatterns = [
    path('', views.post),
    path('berita/', views.berita),
    path('how_to/', views.how_to),
    path('gosip/', views.gosip),
]
