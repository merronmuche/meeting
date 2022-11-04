

from django.contrib import admin
from django.urls import path, include
from meetups import views

urlpatterns = [
 path('',views.index)
]
