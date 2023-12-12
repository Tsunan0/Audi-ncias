from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Agenda
import datetime

# Create your views here.

def inicial(request):
    now = timezone.localtime(timezone.now())
    return render(request, 'inicial.html', {'now':now})

def lista(request):
    now = timezone.localtime(timezone.now())
    lista = Agenda.objects.all()
    return render(request, 'lista.html',{'agenda':lista, 'now':now})

def cadastro(request):
    return render(request, 'cadastro.html',)

def update(request):
    nova_agenda = Agenda()
    nova_agenda.nome = request.POST.get('nome')
    nova_agenda.dt_criacao = datetime.datetime.now()
    nova_agenda.responsavel = request.POST.get('responsavel')
    nova_agenda.dt_audiencia = request.POST.get('dt_audiencia')
    nova_agenda.classe = request.POST.get('classe')
    nova_agenda.save()

    return redirect(lista)

def deletar(request, id):
    agenda = Agenda.objects.get(id=id)
    agenda.delete()
    return redirect(lista)

def editar(request, id):
    agenda = Agenda.objects.get(id=id)
    return render(request, 'editar.html', {'agenda':agenda})

def salvar(request, id):
    vnome = request.POST.get('nome')
    vresponsavel = request.POST.get('responsavel')
    vdt_audiencia = request.POST.get('dt_audiencia')
    vclasse = request.POST.get('classe')

    agenda = Agenda.objects.get(id=id)

    agenda.nome = vnome
    agenda.responsavel = vresponsavel
    agenda.dt_audiencia = vdt_audiencia
    agenda.classe = vclasse
    agenda.save()
    return redirect(lista)