
from django.contrib import admin
from django.urls import path, include
from app_ponfaes import views

urlpatterns = [
    # Página de login na raiz
    path('', views.login_view, name='login'),

    # Página inicial após login
    path('home/', views.home, name='home'),

    # Outras rotas
    path('admin/', admin.site.urls),
    path('avisos/', views.avisos_home, name='avisos_home'),
    path('boletim/', views.boletim_home, name='boletim_home'),
    path('frequencia/', views.frequencia_home, name='frequencia_home'),
    path('comunicacao/', views.comunicacao_home, name='comunicacao_home'),
    path('agenda/', views.agenda_home, name='agenda_home'),
]