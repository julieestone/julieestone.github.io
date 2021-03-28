from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('pups_and_quotes', views.pups_and_quotes, name="pupsquotes")
]