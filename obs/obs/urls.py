from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from usuarios.views import logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/',include('usuarios.urls')),
    path('categoria/',include('categoria.urls')),

    # Login y logout
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
]
