from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [path("" , views.inicio, name = "inicio"),
    path("alta_productos", views.guarda_prod , name="alta_productos"),
    path("buscar_producto" , views.buscar_producto , name="buscar_producto"),
    path("buscar_p" , views.buscar_p),
    path("alta_clientes", views.guarda_clie , name="alta_clientes"),
    path("alta_os", views.guarda_os , name="alta_os"),
    path("buscar_cliente" , views.buscar_cliente, name="buscar_cliente"),
    path("buscar_c" , views.buscar_c),
    path("buscar_os" , views.buscar_os, name="buscar_os"),
    path("buscar_o" , views.buscar_o),
    path("lista_productos", views.lista_productos , name="lista_productos"),
    path("borra_producto/<int:id>" , views.borra_producto, name="borra_producto"),
    path("borra_producto/alta_productos", views.guarda_prod , name="alta_productos"),
    path("editar_producto/<int:id>" , views.editar_producto , name="editar_producto"),
    path("editar_producto/" , views.editar_producto , name="editar_producto"),
    path("lista_clientes", views.lista_clientes , name="lista_clientes"),
    path("borra_cliente/<int:id>" , views.borra_cliente, name="borra_cliente"),
    path("borra_cliente/alta_clientes",  views.guarda_clie , name="alta_clientes"),
    path("editar_cliente/<int:id>" , views.editar_cliente , name="editar_cliente"),
    path("editar_cliente/" , views.editar_cliente , name="editar_cliente"),
    path("lista_os", views.lista_os , name="lista_os"),
    path("borra_os/<int:id>" , views.borra_os, name="borra_os"),
    path("borra_os/alta_os",  views.guarda_os , name="alta_os"),
    path("editar_os/<int:id>" , views.editar_os , name="editar_os"),
    path("editar_os/" , views.editar_os , name="editar_os"),
    path("register" , views.register , name="Register"),
    path("login" , views.login_request , name="Login"),
    path("logout" , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path("editar_perfil" , views.editarPerfil , name="editar_perfil"),
    path("editar_producto/logout" , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path("borra_producto/logout" , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path("editar_cliente/logout" , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path("borra_cliente/logout" , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path("editar_os/logout" , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path("borra_os/logout" , LogoutView.as_view(template_name="logout.html") , name="Logout"),
    path("editar_producto/editar_perfil" , views.editarPerfil , name="editar_perfil"),
    path("borra_producto/editar_perfil" , views.editarPerfil , name="editar_perfil"),
    path("editar_cliente/editar_perfil" , views.editarPerfil , name="editar_perfil"),
    path("borra_cliente/editar_perfil" , views.editarPerfil , name="editar_perfil"),
    path("editar_os/editar_perfil" , views.editarPerfil , name="editar_perfil"),
    path("borra_os/editar_perfil" , views.editarPerfil , name="editar_perfil"),
    path("editar_producto/login" , views.login_request , name="Login"),
    path("borra_producto/login" , views.login_request , name="Login"),
    path("editar_cliente/login" , views.login_request , name="Login"),
    path("borra_cliente/login" , views.login_request , name="Login"),
    path("editar_os/login" , views.login_request , name="Login"),
    path("borra_os/login" , views.login_request , name="Login"),
    path("editar_producto/register" , views.register , name="Register"),
    path("borra_producto/register" , views.register , name="Register"),
    path("editar_cliente/register" , views.register , name="Register"),
    path("borra_cliente/register" , views.register , name="Register"),
    path("editar_os/register" , views.register , name="Register"),
    path("borra_os/register" , views.register , name="Register"),
    path("about" , views.about , name="about"),

]