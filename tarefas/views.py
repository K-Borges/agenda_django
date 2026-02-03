from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def tarefas_home(request):
    return HttpResponse("<h1>Aqui estao suas tarefas</h1>")
