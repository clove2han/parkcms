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
    path(r'index',views.index,name='index'),
    path(r'login', views.login,name='login'),
    path(r'welcome', views.welcome,name='welcome'), 
    
    path(r'member-list', views.memberlist,name='memberlist'), 
    path(r'member-del', views.memberdel,name='memberdel'), 
    path(r'member-add', views.memberadd,name='memberadd'),   
    
    
    path(r'order-list', views.orderlist,name='orderlist'),   
    path(r'order-add', views.orderadd,name='orderadd'), 
        
    path(r'admin-list', views.adminlist,name='adminlist'),    
    path(r'admin-edit', views.adminedit,name='adminedit'), 
    path(r'admin-add', views.adminadd,name='adminadd'),  
]
