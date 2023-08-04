from django.urls import path
from dogs.views import home

urlpatterns = [
    path('', home)
]
