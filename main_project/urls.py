"""main_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import index 
from blog.views import author_page
from blog.views import article_page
from blog.views import test_page
from connection.views import get_message
from connection.views import thanks
#from blog.views import create_article
from connection.views import Create_Article
from user.views import Create_User
from user.views import login


urlpatterns = [
    path('', include('blog.urls')),
    path('ad/', admin.site.urls),
    path('get_message/',get_message,name='get_message'),
    path('thanks/',thanks,name='thanks'),
    path('auth/', include('user.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
