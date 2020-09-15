from django.urls import path,include
from . import views

urlpatterns = [
    #path('',views.home,name="home"),
    path('',views.forms,name="forms"),
    path('designation/',views.designation,name="designation"),
    #path('role/',views.role,name="role"),
    #path('',views.forms,name="forms"),
    

]    