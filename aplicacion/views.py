from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserForm, NucleosForm, IntegrantesForm, DatosPersonalesForm
from .models import User, Nucleos, Integrantes, DatosPersonales


# Create your views here.

def home(request):
    return render(request, 'home.html')

def registro(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {"form": UserForm})
    else:
        usuario = User.objects.filter(username=request.POST['username']).values('username').first()
        
        if usuario is None:
            if request.POST['password1'] == request.POST['password']:

                user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'],
                                        password=request.POST['password'])
                login(request, user)
                return redirect('nucleos')
            else:
                return render(request, 'registro.html', {"form": UserForm, "error": "Contraseñas no coinciden"})
        else: 
            return render(request, 'registro.html', {"form": UserForm, "error": "El usuario ya existe"})

def autenticacion(request):
    if request.method == 'GET':
        return render(request, 'autenticacion.html', {"form":AuthenticationForm})
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'autenticacion.html', {"form":AuthenticationForm, "error": "El usuario o contraseña no son correctas"})
        else:
            login(request, user)
            return redirect('nucleos')

@login_required
def nucleos(request):
    nucleo = Nucleos.objects.filter(user=request.user).exists()
    if nucleo is False:
        return render(request, 'no_existe.html', {"nombre": "Nucleo Familiar", "nucleo": "No ha creado un nucleo"})
    else:
        nucleo = Nucleos.objects.filter(user=request.user)
        return render(request, 'nucleos.html', {"nucleo": nucleo})

@login_required
def crear_nucleo(request):
    if request.method == 'GET':
        return render(request, 'crear_nucleo.html', {"form": NucleosForm})
    else:
        form = NucleosForm(request.POST)
        new_form = form.save(commit=False)
        new_form.user = request.user
        new_form.save()
        return redirect('nucleos')

@login_required
def eliminar_nucleo(request, user_id):
    nucleo = Nucleos.objects.get(pk=user_id).delete()
    return redirect('nucleos')
    
@login_required
def integrantes(request):
    if request.method == 'GET':
        return render(request, 'integrantes.html', {"form": IntegrantesForm})
    else:
        form = IntegrantesForm(request.POST)
        new_form = form.save(commit=False)
        new_form.user = request.user
        new_form.save()
        return redirect('detalle')

@login_required
def detalle(request):
    integrantes = Integrantes.objects.filter(user=request.user).exists()
    if integrantes is False:
        return render(request, 'no_existe.html', {"nombre": "Integrantes","nucleo": 'No ha añadido integrantes a su nucleo'})
    else:
        integrantes = Integrantes.objects.filter(user=request.user)
        return render(request, 'detalle.html', {"int": integrantes})

@login_required
def eliminar_integrante(request, int_id):
    integrantes = Integrantes.objects.get(pk=int_id).delete()
    return redirect('detalle')

@login_required
def actualizar_integrantes(request, act_id):
    if request.method == 'GET':
        integrantes = Integrantes.objects.filter(pk=act_id)
        return render(request, 'actualizar.html', {"int": integrantes, "form": DatosPersonalesForm})
    else:
        intancia = Integrantes.objects.get(pk=act_id)
        integrantes = Integrantes.objects.filter(pk=act_id).values().first()
        form = DatosPersonalesForm(request.POST)
        new_form = form.save(commit=False)
        new_form.nombre = integrantes['nombre']
        new_form.user = intancia
        new_form.save()
        return redirect('casos')

@login_required
def casos(request, id):
    form = DatosPersonales.objects.filter(user_id=id, trabaja__isnull=False, estudia__isnull=False,                      desocupado__isnull=False)
    return render(request, 'casos.html', {"form": form})

@login_required
def cerrar(request):
    logout(request)
    return redirect('home')

@login_required
def eliminar_usuario(request):
    user = User.objects.get(username=request.user).delete()
    logout(request)
    return redirect('home')