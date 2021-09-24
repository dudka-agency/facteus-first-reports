from django.urls import path

from . import views

urlpatterns = [
    path('pdf', views.GeneratePdf.as_view(), name='pdf'),
]