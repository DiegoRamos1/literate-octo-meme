from django.shortcuts import render, HttpResponse

def index(request):
    context = {"pelicula1": "Titanic"}
    return render(request, "index.html",context)
def Origen(request):
    return render(request, "Origen.html")
def Autocuidado(request):
    return render(request, "Autocuidados.html")