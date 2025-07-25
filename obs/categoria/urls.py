
from django.urls import path
from . import views
urlpatterns = [
    path('listar/', views.CategoriaListView.as_view(), name='categoria_listar'),
    path('nueva/', views.CategoriaCreateView.as_view(), name='categoria_crear'),
    path('editar/<int:pk>/', views.CategoriaUpdateView.as_view(), name='categoria_editar'),
    path('eliminar/<int:pk>/', views.CategoriaDeleteView.as_view(), name='categoria_eliminar'),
]
