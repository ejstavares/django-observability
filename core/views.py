from django.shortcuts import render, redirect
from .models import Pessoa
import structlog

# Create your views here.

def home(request):
    log = structlog.get_logger()
    log.info("home_view", request_id=getattr(request, "request_id", None))
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas":pessoas})

def save(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        idade = request.POST.get("idade")
        pessoa = Pessoa(nome=nome, idade=idade)
        pessoa.save()
    return redirect(home)

def pessoa_detail(request, pessoa_id):
    pessoa = Pessoa.objects.get(id=pessoa_id)

    log = structlog.get_logger()
    log.info("pessoa_detail", pessoa_id=pessoa_id, pessoa_nome=pessoa.nome, pessoa_idade=pessoa.idade, request_id=getattr(request, "request_id", None))
    return render(request, "pessoa_detail.html", {"pessoa": pessoa})

def pessoa_delete(request, pessoa_id):
    pessoa = Pessoa.objects.get(id=pessoa_id)
    pessoa.delete()
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas": pessoas})

def pessoa_update(request, pessoa_id):
    pessoa = Pessoa.objects.get(id=pessoa_id)
    if request.method == "POST":
        pessoa.nome = request.POST.get("nome")
        pessoa.idade = request.POST.get("idade")
        pessoa.save()
    
    return redirect(home)
