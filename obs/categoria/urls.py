
from django.urls import path
from . import views
urlpatterns = [
    path('categorias/', views.CategoriaListView.as_view(), name='categoria_listar'),
    path('categorias/nueva/', views.CategoriaCreateView.as_view(), name='categoria_crear'),
    path('categorias/editar/<int:pk>/', views.CategoriaUpdateView.as_view(), name='categoria_editar'),
    path('categorias/eliminar/<int:pk>/', views.CategoriaDeleteView.as_view(), name='categoria_eliminar'),
]
