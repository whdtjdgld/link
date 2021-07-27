<<<<<<< HEAD
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
    path("q5", views.q5, name="q5"),
    path("q6", views.q6, name="q6"),
    path("q7", views.q7, name="q7"),
    path("q8", views.q8, name="q8"),
    path("findpw", views.findpw, name="findpw"),
    path("findteam", views.findteam, name="findteam"),
    path("detail", views.detail, name="detail"),
    path("findprj", views.findprj, name="findprj"),
    path("prjdetail", views.prjdetail, name="prjdetail"),
    path("chat", views.chat, name="chat"),
    path("gongmo", views.gongmo, name="gongmo"),
    path("revise", views.revise, name="revise"),
    path("mypage", views.mypage, name="mypage"),
    path("consultchat", views.consultchat, name="consultchat"),
]
=======
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
    path("q5", views.q5, name="q5"),
    path("q6", views.q6, name="q6"),
    path("q7", views.q7, name="q7"),
    path("q8", views.q8, name="q8"),
    path("findpw", views.findpw, name="findpw"),
    path("findteam", views.findteam, name="findteam"),
    path("detail", views.detail, name="detail"),
    path("findprj", views.findprj, name="findprj"),
    path("prjdetail", views.prjdetail, name="prjdetail"),
    path("chat", views.chat, name="chat"),
    path("app", views.app, name="app"),
]
>>>>>>> 132128f449ed0da379de227deeca644fd3dbb357
