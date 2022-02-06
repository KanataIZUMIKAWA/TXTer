from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('newtxt', views.newtxt, name='newtxt'),
    path('mypage', views.mypage, name='mypage'),
    path('regist', views.regist, name='regist'),
    path('posts', views.posts, name='posts'),
]