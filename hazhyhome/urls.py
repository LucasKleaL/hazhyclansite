from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('home', views.home, name='home'),
]