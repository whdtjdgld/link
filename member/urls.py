from django.contrib import admin
from django.urls import path
from member import views

urlpatterns = [
    path("signup", views.signup, name="signup"),
    path("", views.main, name="main"),
    path("main", views.main, name="main"),
    path("profile", views.profile, name="profile"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("congrats", views.congrats, name="congrats"),
    path("q2", views.q2, name="q2"),
    path("q3", views.q3, name="q3"),
    path("q4", views.q4, name="q4"),
    path("findpw", views.findpw, name="findpw"),
]