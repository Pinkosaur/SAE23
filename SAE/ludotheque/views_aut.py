from django.shortcuts import render
from .forms import AuteurForm
from . import models
from django.http import HttpResponseRedirect

def ajoutAuteur(request):
    if request.method == "POST":
        form = AuteurForm(request)
        if form.is_valid():
            auteur = form.save()
            return render(request, "ludotheque/auteurs/afficheAuteur.html", {"auteur": auteur})
        else:
            return render(request, "ludotheque/auteurs/ajoutAuteur.html", {"form": form})
    else:
        form = AuteurForm()
        return render(request, "ludotheque/auteurs/ajoutAuteur.html", {"form": form})

def traitementAuteur(request):
    auteurform = AuteurForm(request.POST)
    if auteurform.is_valid():
        auteur = auteurform.save()
        return render(request, "ludotheque/auteurs/afficheAuteur.html", {"auteur": auteur})
    else:
        return render(request, "ludotheque/auteurs/ajoutAuteur.html", {"form": auteurform})

def afficheAuteur(request, id):
    auteur = models.Auteur.objects.get(pk=id)
    return render(request, 'ludotheque/auteurs/afficheAuteur.html', {'auteur': auteur})

def updateAuteur(request, id):
    auteur = models.Auteur.objects.get(pk=id)
    auteurform = AuteurForm(auteur.dic())
    return render(request, "ludotheque/auteurs/updateAuteur.html/", {"form":auteurform, "id":id})

def updatetraitementAuteur(request, id):
    auteurform = AuteurForm(request.POST)
    saveid = id
    if auteurform.is_valid():
        auteur = auteurform.save(commit = False)
        auteur.id = saveid
        auteur.save()
        return HttpResponseRedirect("/ludotheque/auteurs/indexAuteur/")
    else:
        return render(request, "ludotheque/auteurs/updateAuteur.html", {"form": auteurform})

def deleteAuteur(request, id):
    suppr = models.Auteur.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/ludotheque/indexAuteur")

def indexAuteur(request):
    liste = models.Auteur.objects.all()
    return render(request, "ludotheque/auteurs/indexAuteur.html", {"liste": liste})