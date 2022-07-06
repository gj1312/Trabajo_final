from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class Alta_producto(forms.Form):

    nombre = forms.CharField(max_length=40)
    codigo = forms.IntegerField()
    precio = forms.IntegerField()

class Alta_cliente(forms.Form):

    nombre = forms.CharField(max_length=80)
    os = forms.CharField(max_length=100)
    cod_os = forms.IntegerField()
    fec = forms.DateField()

class Alta_os(forms.Form):

    nombre = forms.CharField(max_length=40)
    cod_os = forms.IntegerField()
    nombre_prod = forms.CharField(max_length=40)
    codigo_prod = forms.IntegerField()

class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña" , widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña" , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email' , 'password1' , 'password2']
        help_text = {k:"" for k in fields}

    
    

