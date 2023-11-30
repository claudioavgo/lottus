from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("diaadiadogotas", views.diaadiadogotas, name="diaadiadogotas"),
    path("iniciativasdogotas", views.iniciativasdogotas, name="iniciativasdogotas"),
    path("doar", views.doar, name="doar"),
    path("login", views.loginPage, name="login"),
    path("empresa", views.empresa, name="empresa"),
    path("logout", views.logoutPage, name="logout"),
    path("cadastro", views.register, name="cadastro"),
    path("apadrinhe", views.apadrinhe, name="apadrinhe"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("dashboard/contrato", views.contrato, name="contrato"),
    path("empresa-info", views.empresa_info, name="empresa info"),
    path("dashboard/crianca", views.dash_crianca, name="dash_crianca"),
    path("dashboard/doacoes", views.dash_doacoes, name="dash_doacoes"),
    path("dashboard/apadrinhar", views.dash_random_child, name="dash_random_child"),
    path("dashboard/user/<str:nome>",views.dash_specific_user, name="dash_crianca"),
    path("dashboard/adicionar/crianca",views.dash_add_child, name="dash_add_child"),
    path("dashboard/crianca/<str:nome>",views.dash_specific_child, name="dash_crianca"),
    path("dashboard/adicionar/atividade",views.dash_add_activity, name="dash_add_activity"),
    path("dashboard/aprovar/contrato/<str:crianca>",views.dash_aprovar_contrato, name="dash_aprovar_contrato"),
    path("dashboard/configuracoes", views.configuracoes, name="configuracoes"),
    path("dashboard/dashcontas", views.dashcontas, name="dashcontas"),
    path("dashboard/criancas", views.criancas, name="criancas"),
    path("dashboard/usuarios", views.usuarios, name="usuarios"),
    path("dashboard/adicionar/administrador/<str:usuario>", views.add_admin, name="adicionar adminstrador"),
]
