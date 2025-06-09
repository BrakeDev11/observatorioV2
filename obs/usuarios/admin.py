from django.contrib import admin
from .models import Usuario
from django.contrib.auth.admin import UserAdmin

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ['username', 'email', 'tipo', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Rol del sistema', {'fields': ('tipo',)}),
    )

admin.site.register(Usuario, UsuarioAdmin)
