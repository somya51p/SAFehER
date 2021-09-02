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
from django.contrib.auth import views as auth_views  

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
    path('helpline/', helpline, name='helpline'),
    path('information/', information, name='information'),
    path('upload_queries/', upload_queries, name='upload_queries'),
    path('faq/', faq, name='faq'),
    path('vaccine/', vaccine, name='vaccine'),
    path('magazine/', magazine, name='magazine'),
    path('ngos/', ngos, name='ngos'),
    path('login_admin/', login_admin, name='login_admin'),
    path('admin_home/', admin_home, name='admin_home'),
    path('pending_queries/', pending_queries, name='pending_queries'),
    path('accepted_queries/', accepted_queries, name='accepted_queries'),
    path('rejected_queries/', rejected_queries, name='rejected_queries'),
    path('all_queries/', all_queries, name='all_queries'),
    path('assign_status/<int:pid>', assign_status, name='assign_status'),
    path('pending_m/', pending_m, name='pending_m'),
    path('accepted_m/', accepted_m, name='accepted_m'),
    path('rejected_m/', rejected_m, name='rejected_m'),
    path('all_m/', all_m, name='all_m'),
    path('assignstatus_m/<int:pid>', assignstatus_m, name='assignstatus_m'),
    path('upload_m/', upload_m, name='upload_m'),
    path('view_m/', view_m, name='view_m'),
    path('view_users/', view_users, name='view_users'),
    path('delete_user/<int:pid>', delete_user, name='delete_user'),
    path('delete_notes/<int:pid>', delete_notes, name='delete_notes'),
    path('delete_m/<int:pid>', delete_m, name='delete_m'),
    path('chat/', include('chat.urls')),
    #password reset
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
