from django.urls import path
from .views import *
from django.shortcuts import render

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers', topSellers, name='top-sellers'),
    path('advertisement-post', advertisementPost, name='advertisement-post'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('profile', profile, name='profile')
]