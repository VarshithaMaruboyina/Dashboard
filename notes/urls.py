from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings

urlpatterns = [
    path('register/',views.registerfunction,name='register'),
    path('registerdata/',views.registerdatafunction,name="registerdata"),
    path('loginform/',views.loginfunction,name="loginform"),
    path('logincheck/',views.logincheckfunction,name="logincheck"),

]
