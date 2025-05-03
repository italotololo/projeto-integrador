from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # usa o alias para evitar conflito
            return redirect('home')   # redireciona após login bem-sucedido
        else:
            context = {'error': 'Usuário ou senha inválidos'}
            return render(request, 'login.html', context)
    return render(request, 'home/login.html')

    

def home(request):
    return render(request,'home/home.html')

def avisos_home(request):
    return render(request,'home/avisos.html')

def boletim_home(request):
    return render(request,'boletim/home.html')

def frequencia_home(request):
    return render(request,'frequencia/home.html')

def comunicacao_home(request):
    return render(request,'comunicacao/home.html')

def agenda_home(request):
    return render(request,'agenda/home.html')


