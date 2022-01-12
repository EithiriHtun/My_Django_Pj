"""first_project URL Configuration

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
from django.urls import path
from first_app import views
from django.urls import include
from first_project import settings

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('first_app/',include('first_app.urls')),
    path('admin/', admin.site.urls),
    path('form_page/',views.form_name_view,name='form'),
    path('special/', views.special,name='special'),
    path('logout/', views.user_logout, name='logout'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
      path('__debug__/',include(debug_toolbar.urls))
    ] + urlpatterns
