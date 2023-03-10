from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('',  views.HomePage, name="HomePage"),
    path('posts', views.ShowAllPosts, name="ShowAllPosts"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('new-post/', views.new_post, name='new_post'),

]
