from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views
from accounts import views as rest_views

router = routers.DefaultRouter()
router.register(r'users', rest_views.UserViewSet)
router.register(r'groups', rest_views.GroupViewSet)
router.register(r'Articles', rest_views.ArticleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #accounts urls
    path('accounts/', include('accounts.urls')),
    #articles urls
    path('articles/', include('articles.urls')),
    #main urls
    path('about/', views.about),
    path('home/', article_views.article_list, name="home"),

    #wire up our APi using automatic URL routing
    #additionally, we include login URLS for the browser APi
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
