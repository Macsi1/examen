from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login

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

def principal_view(request):
    return render(request, 'principal.html')
