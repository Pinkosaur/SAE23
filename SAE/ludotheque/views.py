from django.shortcuts import render
from .forms import
from . import models
from django.http import HttpResponseRedirect

# Create your views here.

def ajoutjeu(request):
    if request.method == "POST":
        form = JeuForm(request)
        if form.is_valid():
            jeu = form.save()
            return render(request, "ludotheque/affichejeu.html", {"jeu": jeu})
        else:
            return render(request, "ludotheque/ajoutjeu.html", {"form": form})
    else:
        form = JeuForm()
        return render(request, "ludotheque/ajoutjeu.html", {"form": form})


def traitementjeu(request):
    jeuform = JeuForm(request.POST)
    if jeuform.is_valid():
        jeu = jeuform.save()
        return render(request, "ludotheque/affichejeu.html", {"jeu": jeu})
    else:
        return render(request, "ludotheque/ajoutjeu.html", {"form": jeuform})


def affichejeu(request, id):
    jeu = models.Jeu.objects.get(pk=id)
    return render(request, 'ludotheque/affichejeu.html', {'jeu': jeu})


def updatejeu(request, id):
    jeu = models.Jeu.objects.get(pk=id)
    jeuform = JeuForm(jeu.dic())
    return render(request, "ludotheque/ajoutupdatejeu.html/", {"form":jeuform, "id":id})


def updatetraitementjeu(request, id):
    jeuform = JeuForm(request.POST)
    saveid = id
    if jeuform.is_valid():
        jeu = jeuform.save(commit = False)
        jeu.id = saveid
        jeu.save()
        return HttpResponseRedirect("/ludotheque/indexjeu/")
    else:
        return render(request, "ludotheque/ajoutupdatejeu.html", {"form": jeuform})


def deletejeu(request, id):
    suppr = models.Jeu.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/ludotheque/indexjeu")


def indexjeu(request):
    liste = models.Jeu.objects.all()
    return render(request, "ludotheque/indexjeu.html", {"liste": liste})