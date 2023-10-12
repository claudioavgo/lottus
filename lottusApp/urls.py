from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("login", views.login, name="login"),
    path("cadastro", views.register, name="cadastro"),
    path("doar", views.doar, name="doar"),
    path("apadrinhe", views.apadrinhe, name="apadrinhe"),
]