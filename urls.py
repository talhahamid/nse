from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.checkLogin,name="login"),
    path("signup",views.signup,name="signup"),
    path('register',views.register,name="register"),
    path('checkLogin',views.checkLogin,name="checkLogin"),
    path('oclist',views.oclist,name="oclist"),
    path("profile",views.profile,name="profile"),
    path("home",views.home,name="home"),
    path("logout",views.logout,name="logout"),
    path("forget",views.forget,name="forget"),
    path("plan",views.plan,name="plan"), 
    path("planstore",views.planstore,name="planstore"),      
]