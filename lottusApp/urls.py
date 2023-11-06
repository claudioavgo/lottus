from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("doar", views.doar, name="doar"),
    path("empresa", views.empresa, name="empresa"),
    path("login", views.loginPage, name="login"),
    path("logout", views.logoutPage, name="logout"),
    path("cadastro", views.register, name="cadastro"),
    path("apadrinhe", views.apadrinhe, name="apadrinhe"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("dashboard/crianca", views.dash_crianca, name="dash_crianca"),
    path("dashboard/doacoes", views.dash_doacoes, name="dash_doacoes"),
    path("dashboard/contrato", views.contrato, name="contrato"),
    path("dashboard/user/<str:nome>", views.dash_specific_user, name="dash_crianca"),
    path("dashboard/crianca/<str:nome>", views.dash_specific_child, name="dash_crianca"),
    path("dashboard/adicionar/crianca", views.dash_add_child, name="dash_add_child"),
    path("dashboard/adicionar/atividade", views.dash_add_activity, name="dash_add_activity"),
    path("dashboard/apadrinhar", views.dash_random_child, name="dash_random_child"),
    path("dashboard/aprovar/contrato/<str:crianca>", views.dash_aprovar_contrato, name="dash_aprovar_contrato"),
]