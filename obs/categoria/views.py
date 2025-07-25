# views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Categoria
from .forms import CategoriaForm
from django.views import View
from django.shortcuts import get_object_or_404, redirect


class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'categoria/categoria_list.html'
    context_object_name = 'categoria'

class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/categoria_form.html'
    success_url = reverse_lazy('categoria_listar')

    def form_valid(self, form):
        form.instance.creado_por = self.request.user
        return super().form_valid(form)

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/categoria_form.html'
    success_url = reverse_lazy('categoria_listar')

class CategoriaDeleteView(View):
    def get(self, request, pk):
        categoria = get_object_or_404(Categoria, pk=pk)
        categoria.delete()
        return redirect('categoria_listar')