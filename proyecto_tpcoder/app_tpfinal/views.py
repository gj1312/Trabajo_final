from django.shortcuts import render
from django.http import HttpResponse
from app_tpfinal.models import Productos, Clientes, Obra_social, Avatar
from django.template import loader
from app_tpfinal.forms import Alta_producto, Alta_cliente, Alta_os, UserEditForm
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required 


# Create your views here.
def inicio(request):

    return render (request , "inicio.html")

#alta de productos
@login_required
def guarda_prod(request):

    if request.method == "POST":

        mi_formulario = Alta_producto( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

        
        producto = Productos( nombre_prod=datos['nombre'] , codigo_prod=datos['codigo'], precio_prod=datos['precio'])
        producto.save()
        
    
        producto2 = Productos.objects.all()
        return render(request , "lista_productos.html" , {"productos" : producto2})



    return render(request, "formularios.html")   

#busqueda de productos

def buscar_producto(request):

    return render( request, "buscar_producto.html")


def buscar_p(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        productos2 = Productos.objects.filter(nombre_prod__icontains = nombre)
        return render( request , "resultado_busqueda.html" ,  {"productos2": productos2})

    else:
        return HttpResponse("campo vacio")

#Alta de clientes
@login_required
def guarda_clie(request):

    if request.method == "POST":

        mi_formulario = Alta_cliente( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

        
        cliente = Clientes( nombre=datos['nombre'] , obra_social=datos['os'] , codigo_os=datos['cod_os'] , nacimiento=datos['fec'])
        cliente.save()
        
        cliente2 = Clientes.objects.all()
        return render(request , "lista_clientes.html" , {"clientes" : cliente2})



    return render(request, "formularios_clie.html")   

#alta OS
@login_required
def guarda_os(request):

    if request.method == "POST":

        mi_formulario = Alta_os( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

        
        os = Obra_social( nombre=datos['nombre'] , codigo_os=datos['cod_os'] , nombre_prod=datos['nombre_prod'] , codigo_prod=datos['codigo_prod'])
        os.save()
        
        os2 = Obra_social.objects.all()
        return render(request , "lista_os.html" , {"os" : os2})


    return render(request, "formularios_os.html") 

# busqueda clientes

def buscar_cliente(request):

    return render( request, "buscar_cliente.html")


def buscar_c(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        clientes2 = Clientes.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busquedac.html" ,  {"clientes2": clientes2})

    else:
        return HttpResponse("campo vacio")


#busqueda obra social

def buscar_os(request):

    return render( request, "buscar_os.html")


def buscar_o(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']      
        os2 = Obra_social.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busquedao.html" ,  {"os2": os2})

    else:
        return HttpResponse("campo vacio")
@login_required
def lista_productos(request):

    productos = Productos.objects.all()

    dicc = {"productos" : productos}
    plantilla = loader.get_template("lista_productos.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )

@login_required
def borra_producto(request , id):

    producto = Productos.objects.get(id=id)
    producto.delete()




    producto2 = Productos.objects.all()

    return render(request , "lista_productos.html" , {"productos" : producto2})
@login_required
def editar_producto( request, id):

    producto = Productos.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Alta_producto(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            producto.nombre_prod = datos['nombre']
            producto.codigo_prod = datos['codigo']
            producto.precio_prod = datos['precio']
            producto.save()

            
            producto2 = Productos.objects.all()
            return render(request , "lista_productos.html" , {"productos" : producto2})

    else:
         mi_formulario = Alta_producto()
         return render (request , "editar_producto.html" , {"mi_formulario":mi_formulario , "producto" :producto})


#lista de clientes
@login_required
def lista_clientes(request):

    clientes = Clientes.objects.all()

    dicc = {"clientes" : clientes}
    plantilla = loader.get_template("lista_clientes.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )

#borra y edita cliente
@login_required
def borra_cliente(request , id):

    cliente = Clientes.objects.get(id=id)
    cliente.delete()

    cliente2 = Clientes.objects.all()
    return render(request , "lista_clientes.html" , {"clientes" : cliente2})
    
@login_required
def editar_cliente( request, id):

    cliente = Clientes.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Alta_cliente(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            cliente.nombre = datos['nombre']
            cliente.obra_social = datos['os']
            cliente.codigo_os = datos['cod_os']
            cliente.nacimiento = datos['fec']
            cliente.save()

            
            cliente2 = Clientes.objects.all()
            return render(request , "lista_clientes.html" , {"clientes" : cliente2})

    else:
         mi_formulario = Alta_cliente()
         return render (request , "editar_cliente.html" , {"mi_formulario":mi_formulario , "cliente" :cliente})

#lista de Obra Social
@login_required
def lista_os(request):

    os = Obra_social.objects.all()

    dicc = {"os" : os}
    plantilla = loader.get_template("lista_os.html")
    
    documento = plantilla.render(dicc)
    return HttpResponse( documento)

#borra y edita Obra Social
@login_required
def borra_os(request , id):

    os = Obra_social.objects.get(id=id)
    os.delete()

    os2 = Obra_social.objects.all()
    return render(request , "lista_os.html" , {"os" : os2})
    
@login_required
def editar_os( request, id):

    os = Obra_social.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Alta_os(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            os.nombre = datos['nombre']
            os.codigo_os = datos['cod_os']
            os.nombre_prod = datos['nombre_prod']
            os.codigo_pro = datos['codigo_prod']
            os.save()

            
            os2 = Obra_social.objects.all()
            return render(request , "lista_os.html" , {"os" : os2})

    else:
         mi_formulario = Alta_cliente()
         return render (request , "editar_os.html" , {"mi_formulario":mi_formulario , "os" :os})


def register(request):

    if request.method == "POST":
        
        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()
            return render (request , "reg_ok.html")


    else:
        form = UserCreationForm()
    return render( request , "registro.html" , {"form":form})

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request , data= request.POST)

        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user is not None:
                login(request,user)
                avatares = Avatar.objects.filter(user=request.user.id)
                return render( request , "padre.html" , {"mensaje":f"Hola {usuario}", "url":avatares[0].imagen.url})   
            
            else:
                return HttpResponse(f"Usuario Incorrecto")
        else:         
            return render( request , "login.html" , {"form":form})

    form = AuthenticationForm()
    return render( request , "login.html" , {"form":form})



@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":
        
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()

            return render( request , "padre.html")

    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render( request , "editar_perfil.html" , {"miFormulario":miFormulario , "usuario":usuario})


def about(request):

    return render (request , "about.html")







