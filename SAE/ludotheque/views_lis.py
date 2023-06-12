from django.shortcuts import render
from .forms import ListeForm
from . import models
from django.http import HttpResponseRedirect


def ajoutListe(request, id):
    form = ListeForm()
    models.Liste.joueurListe_id = id
    return render(request, "ludotheque/listes/afficheliste.html", {"form": form, "id": id})

def traitementListe(request, id):
    joueur = models.Joueur.objects.get(pk=id)
    form = ListeForm(request.POST)
    if form.is_valid():
        liste = form.save(commit = False) #commit = False
        liste.joueurListe = joueur
        liste.joueur_id = id #bizarre
        liste.save()
        return render(request, "ludotheque/listes/afficheliste.html", {"liste": liste, "id":id})
    else:
        return render(request, "ludotheque/listes/afficheliste.html", {"form": form})

def afficheListe(request, id):
    liste = models.Liste.objects.get(pk=id)
    return render(request, 'ludotheque/listes/afficheliste.html', {'liste': liste, "id":id})

def updateListe(request, id):
    liste = models.Liste.objects.get(pk=id)
    aform = ListeForm(liste.dic())
    return render(request, "ludotheque/listes/updateliste.html/", {"form":aform, "id":id, "liste":liste})

def indexListe(request, id):
    liste = models.Liste.objects.filter(joueur_id=id)
    return render(request, "ludotheque/liste/indexliste.html", {"liste": liste, "id":id})