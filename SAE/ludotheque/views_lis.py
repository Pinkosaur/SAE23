from django.shortcuts import render
from .forms import ListeForm
from . import models
from django.http import HttpResponseRedirect


def ajoutListe(request, id):
    form = ListeForm()
    models.Liste.joueurListe_id = id
    return render(request, "ludotheque/listes/ajoutliste.html", {"form": form, "id": id})

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
    idjoueur = models.Joueur.objects.get(pk=liste.joueurListe_id).id
    return render(request, 'ludotheque/listes/afficheliste.html', {'liste': liste, "idjoueur":idjoueur})

def updateListe(request, id):
    liste = models.Liste.objects.get(pk=id)
    aform = ListeForm(liste.dic())
    return render(request, "ludotheque/listes/updateliste.html/", {"form":aform, "id":id, "liste":liste})

def updatetraitementListe(request, id):
    l=models.Liste.objects.get(pk=id).joueurListe_id
    listeform = ListeForm(request.POST)
    saveid = id
    if listeform.is_valid():
        liste = listeform.save(commit = False)
        liste.id = saveid
        liste.joueurListe_id = l
        liste.save()
        return HttpResponseRedirect(f"/ludotheque/indexListe/{l}/")
    else:
        return render(request, "ludotheque/joueurs/updateJoueur.html", {"form": listeform})

def deleteListe(request, id):
    suppr = models.Liste.objects.get(pk=id)
    idjoueur = models.Joueur.objects.get(pk=suppr.joueurListe_id).id
    suppr.delete()
    return HttpResponseRedirect(f"/ludotheque/indexListe/{idjoueur}/")

def indexListe(request, id): #id du joueur
    liste = models.Liste.objects.filter(joueurListe_id=id)
    joueur = models.Joueur.objects.get(pk = id)
    return render(request, "ludotheque/listes/indexliste.html", {"liste": liste, "joueur":joueur})