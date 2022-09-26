from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not nome.strip():
            return redirect('cadastro')
        if not email.strip():
            return redirect('cadastro')
        if senha != senha2:
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print('Usuario cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == '' or senha == '':
            return redirect('login')
        return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def logout(request):
    pass

def dashboard(request):
    return render(request, 'usuarios/dashboard.html')