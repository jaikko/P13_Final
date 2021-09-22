from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('', include('lettings.urls')),
    path('', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
