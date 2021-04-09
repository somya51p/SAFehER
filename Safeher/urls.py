"""Safeher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from women.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signup/', signup1, name='signup'),
    path('login/', userlogin, name='login'),
    path('logout/', Logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('changepassword/', changepassword, name='changepassword'),
    path('menstrual/', menstrual, name='menstrual'),
    path('bmi/', bmi, name='bmi'),
    path('browse/', browse, name='browse'),
    path('login_admin/', login_admin, name='login_admin'),
    path('admin_home/', admin_home, name='admin_home'),
    path('view_users/', view_users, name='view_users'),
    path('delete_user/<int:pid>', delete_user, name='delete_user'),
]
