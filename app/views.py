from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    return render(request,'home.html')




def tienda(request):
    return render(request,'tienda.html')




def contactos(request):
    return render(request,'contactos.html')
