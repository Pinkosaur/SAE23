from django.shortcuts import render
from .forms import JoueurForm
from . import models
from django.http import HttpResponseRedirect

def ajoutJoueur(request):
    jform = JoueurForm()
    return render(request, "ludotheque/joueurs/ajoutJoueur.html", {"form": jform})

def traitementJoueur(request):
    joueurform = JoueurForm(request.POST)
    if joueurform.is_valid():
        joueur = joueurform.save()
        return render(request, "ludotheque/joueurs/afficheJoueur.html", {"joueur": joueur})
    else:
        return render(request, "ludotheque/joueurs/ajoutJoueur.html", {"joueur": joueurform})

def afficheJoueur(request, id):
    joueur = models.Joueur.objects.get(pk=id)
    liste = models.Liste.objects.filter(joueurListe_id = id)
    return render(request, 'ludotheque/joueurs/afficheJoueur.html', {'joueur': joueur, "liste":liste})

def updateJoueur(request, id):
    joueur = models.Joueur.objects.get(pk=id)
    joueurform = JoueurForm(joueur.dic())
    return render(request, "ludotheque/joueurs/updateJoueur.html/", {"form":joueurform, "id":id})

def updatetraitementJoueur(request, id):
    joueurform = JoueurForm(request.POST)
    saveid = id
    if joueurform.is_valid():
        joueur = joueurform.save(commit = False)
        joueur.id = saveid
        joueur.save()
        return HttpResponseRedirect("/ludotheque/indexJoueur/")
    else:
        return render(request, "ludotheque/joueurs/updateJoueur.html", {"form": joueurform})

def deleteJoueur(request, id):
    suppr = models.Joueur.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/ludotheque/indexJoueur")

def indexJoueur(request):
    liste = models.Joueur.objects.all()
    return render(request, "ludotheque/joueurs/indexJoueur.html", {"liste": liste})