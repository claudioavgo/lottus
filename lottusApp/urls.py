from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.loginPage, name="login"),
    path("logout", views.logoutPage, name="logout"),
    path("cadastro", views.register, name="cadastro"),
    path("doar", views.doar, name="doar"),
    path("apadrinhe", views.apadrinhe, name="apadrinhe"),
    path("dashboard/crianca", views.dash_crianca, name="dash-crianca"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("dashboard/contrato", views.contrato, name="contrato"),
]