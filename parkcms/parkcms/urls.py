"""parkcms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from users import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'',views.index),
#把post/开头的网址后面的字符串都找出来。
    path(r'index/', views.index),
    path(r'login/', views.login),
    path(r'userinfo/', views.userinfo),
    path(r'adduser/', views.adduser),
    path(r'adduser_html/', views.adduser_html),
]
