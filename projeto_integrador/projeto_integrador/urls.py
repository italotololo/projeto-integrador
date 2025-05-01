
from django.contrib import admin
from django.urls import path, include
from app_ponfaes import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('admin/', admin.site.urls),
    path('avisos/', views.avisos_home, name='avisos_home'),
    path('boletim/', views.boletim_home, name='boletim_home'),
    path('frequencia/', views.frequencia_home, name='frequencia_home'),
    path('comunicacao/', views.comunicacao_home, name='comunicacao_home'),
    path('agenda/', views.agenda_home, name='agenda_home'),
]