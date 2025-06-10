from django.urls import path
from . import views


urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('inicio/', views.UsuarioListView.as_view(), name='usuario_list'),
    path('crear/', views.UsuarioCreateView.as_view(), name='usuario_create'),
    path('<int:pk>/editar/', views.UsuarioUpdateView.as_view(), name='usuario_edit'),
    path('<int:pk>/inactivar/', views.usuario_inactivar, name='usuario_inactivar'),
    
    
]