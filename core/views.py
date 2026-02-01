from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Pessoa
import structlog

# Create your views here.

log = structlog.get_logger()

def home(request):
    log = structlog.get_logger()
    log.info("home_view", request_id=getattr(request, "request_id", None))
    pessoas = Pessoa.objects.all()
    return render(request, "index.html", {"pessoas":pessoas})

def save(request):
    if request.method == "POST":
        log.info("pessoa_criar_iniciado", request_id=getattr(request, "request_id", None))
        nome = request.POST.get("nome")
        idade = request.POST.get("idade")
        pessoa = Pessoa(nome=nome, idade=idade)
        pessoa.save()
        log.info("pessoa_criada", pessoa_id=pessoa.id, request_id=getattr(request, "request_id", None))
    return redirect(home)

def pessoa_detail(request, pessoa_id):
    pessoa = Pessoa.objects.get(id=pessoa_id)

    log.info("pessoa_detail", pessoa_id=pessoa_id, pessoa_nome=pessoa.nome, pessoa_idade=pessoa.idade, request_id=getattr(request, "request_id", None))
    return render(request, "pessoa_detail.html", {"pessoa": pessoa})

def pessoa_delete(request, pessoa_id):
    pessoa = Pessoa.objects.get(id=pessoa_id)
    pessoa.delete()
    pessoas = Pessoa.objects.all()
    log.warning("pessoa_deletada", pessoa_id=pessoa_id, request_id=getattr(request, "request_id", None))
    return render(request, "index.html", {"pessoas": pessoas})

def pessoa_update(request, pessoa_id):
    pessoa = Pessoa.objects.get(id=pessoa_id)
    if request.method == "POST":
        log.info("pessoa_atualizar_iniciado", pessoa_id=pessoa.id, request_id=getattr(request, "request_id", None))
        pessoa.nome = request.POST.get("nome")
        pessoa.idade = request.POST.get("idade")
        pessoa.save()
        log.info("pessoa_atualizada", pessoa_id=pessoa.id, request_id=getattr(request, "request_id", None))
    
    return redirect(home)

def ping(request):
    log.info("python_log_test", feature="observability")
    return HttpResponse("ok")

def exceptionExample(request):
    log.exception("pagamento_falhou", pedido_id=123)
    raise Exception("Erro de pagamento")