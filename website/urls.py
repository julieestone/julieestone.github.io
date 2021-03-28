from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pups_and_quotes', views.pups_and_quotes, name="pupsquotes")
]