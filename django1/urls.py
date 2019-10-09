from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #articles urls
    path('articles/', include('articles.urls')),
    #main urls
    path('about/', views.about),
    path('', views.home)
]
