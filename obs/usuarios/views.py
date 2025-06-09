from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Usuario
from .forms import UsuarioForm

# Mixin personalizado para restringir acceso a usuarios tipo 'admin'
class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.tipo == 'admin'

    def handle_no_permission(self):
        from django.contrib.auth.views import redirect_to_login
        return redirect_to_login(self.request.get_full_path())

# Vista del Dashboard (solo para admins autenticados)
class DashboardView(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'usuarios/dashboard.html'

# Lista de usuarios (solo para admins)
class UsuarioListView(LoginRequiredMixin, AdminRequiredMixin, ListView):
    model = Usuario
    template_name = 'usuarios/usuario_list.html'
    context_object_name = 'usuarios'

# Crear usuario (solo admins)
class UsuarioCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('usuario_list')

# Editar usuario (solo admins)
class UsuarioUpdateView(LoginRequiredMixin, AdminRequiredMixin, UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('usuario_list')

# Inactivar usuario (solo admins)
def usuario_inactivar(request, pk):
    if request.user.is_authenticated and request.user.tipo == 'admin':
        usuario = get_object_or_404(Usuario, pk=pk)
        usuario.is_active = False
        usuario.save()
        return redirect('usuario_list')
    else:
        from django.contrib.auth.views import redirect_to_login
        return redirect_to_login(request.get_full_path())

