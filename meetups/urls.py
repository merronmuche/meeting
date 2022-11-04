

from django.contrib import admin
from django.urls import path, include
from meetups import views

urlpatterns = [
 path('',views.index),
 path('<int:meetup_id>/', views.meetup_details, name='meetup-detail'),
]
