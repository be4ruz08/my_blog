from django.contrib import admin
from django.urls import path

from najot_talim.views import index

urlpatterns = [
    path('index/', index, name='index'),
]
