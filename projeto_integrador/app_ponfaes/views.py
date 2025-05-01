from django.shortcuts import render

def home(request):
    return render(request,'home/home.html')



def avisos_home(request):
    return render(request,'avisos/home.html')



def boletim_home(request):
    return render(request,'boletim/home.html')



def frequencia_home(request):
    return render(request,'frequencia/home.html')



def comunicacao_home(request):
    return render(request,'comunicacao/home.html')


def agenda_home(request):
    return render(request,'agenda/home.html')
