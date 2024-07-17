from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Producto
from django.contrib.auth.decorators import login_required

def registro_view(request):
    if request.method == 'POST':
        return redirect('login')  
    else:
        return render(request, 'registro.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials.'})
    else:
        return render(request, 'login.html')

def recuperar_view(request):
    if request.method == 'POST':
        return redirect('login')  
    else:
        return render(request, 'recuperar.html')
    
@login_required
def principal_view(request):
    return render(request, 'principal.html')

@login_required
def add_producto(request):
    productos = Producto.objects.all()
    return render(request, "todosProductos.html", {"productos": productos})

@login_required
def registrar_producto(request):
    if request.method == 'POST':
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        precio = request.POST['numPrecio']

        producto = Producto.objects.create(codigo=codigo, nombre=nombre, precio=precio)
        return redirect('productos')
    else:
        return redirect('principal')
    
@login_required    
def eliminarProducto(request, codigo):
    if request.method == 'POST':
        producto = Producto.objects.get(codigo=codigo)
        producto.delete()
        return redirect('productos')
    else:
        return redirect('principal')
    
@login_required    
def editarProducto(request):
    if request.method == 'POST':
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        precio = request.POST['numPrecio']

        producto = Producto.objects.get(codigo=codigo)
        producto.nombre = nombre
        producto.precio = precio 
        producto.save()

        return redirect('productos')
    else:
        return redirect('principal')
    
@login_required
def edicionProducto(request, codigo):
    if request.method == 'GET':
        producto = Producto.objects.get(codigo=codigo)
        return render(request, "edicionProducto.html", {"producto": producto})
    elif request.method == 'POST':
        producto = Producto.objects.get(codigo=codigo)
        producto.nombre = request.POST['txtNombre']
        producto.precio = request.POST['numPrecio']
        producto.save()
        return redirect('productos')
    else:
        return redirect('principal')


