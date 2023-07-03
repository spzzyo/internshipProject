"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from .import views,admin_views,staff_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base, name= 'base'),

    path('', views.loginpage, name='loginpage' ), #naming urls 
    path('doLogin',views.doLogin, name='doLogin'),
    path('doLogout',views.doLogout, name='Logout'),

    path('hod/course/add', admin_views.add_course, name='add_course'),
    path('hod/course/view', admin_views.view_course, name='view_course'),
    path('hod/staff/add', admin_views.add_instructor, name='add_instructor'),
    path('hod/lecture/add', admin_views.add_lecture, name='add_lecture'),
    path('hod/lecture/view', admin_views.view_lecture, name='view_lecture'),
    path('instructors/<int:instructor_id>', staff_views.lecture_schedule, name='lecture_schedule'),


] 

