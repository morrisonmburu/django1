from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name="article_list"),
    path('create/', views.article_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
]
