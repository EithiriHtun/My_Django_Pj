from django.urls import path
from first_app import views

#Template tagging
app_name= 'basic_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('/other',views.other,name='other')

]
