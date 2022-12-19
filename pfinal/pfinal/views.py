from django.shortcuts import render

def inicio(request):
    template_name= "index.html"
    contexto={
        'Nombre':"Nico"
    }
    return render(request,template_name,contexto)