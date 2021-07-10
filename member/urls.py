from django.contrib import admin
from django.urls import path
from member import views

urlpatterns = [
    path("", views.main, name="main"),
    path("main", views.main, name="main"),
    path("profile", views.profile, name="profile"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    
    
]
