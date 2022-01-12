from django.urls import path
from first_app import views

#Template tagging
app_name= 'basic_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('other/',views.other,name='other'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),

]
