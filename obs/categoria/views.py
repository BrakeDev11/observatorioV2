# views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Categoria
from .forms import CategoriaForm

class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'categoria/listar.html'
    context_object_name = 'categorias'

class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/formulario.html'
    success_url = reverse_lazy('categoria_listar')

    def form_valid(self, form):
        form.instance.creado_por = self.request.user
        return super().form_valid(form)

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/formulario.html'
    success_url = reverse_lazy('categoria_listar')

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'categoria/confirmar_eliminar.html'
    success_url = reverse_lazy('categoria_listar')
