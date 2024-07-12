from django.shortcuts import render

# Create your views here.
def lasya(request):
    return render(request,'lasya.html')

def akarsh(request):
    return render(request,'akarsh.html')


def register(request):
    return render(request,'register.html')


def login(request):
    return render(request,'login.html')