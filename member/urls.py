from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('marker/', views.marker, name='marker'),
]
