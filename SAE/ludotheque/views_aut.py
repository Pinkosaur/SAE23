from django.shortcuts import render
from .forms import AuteurForm
from . import models
from django.http import HttpResponseRedirect

def ajoutAuteur(request):
    form = AuteurForm()
    return render(request, "ludotheque/auteurs/ajoutAuteur.html", {"form": form})

def traitementAuteur(request):
    auteurform = AuteurForm(data=request.POST, files=request.FILES)
    if auteurform.is_valid():
        auteur = auteurform.save()
        return render(request, "ludotheque/auteurs/afficheAuteur.html", {"auteur": auteur})
    else:
        return render(request, "ludotheque/auteurs/ajoutAuteur.html", {"form": auteurform})

def afficheAuteur(request, id):
    auteur = models.Auteur.objects.get(pk=id)
    image = auteur.photoAuteur
    return render(request, 'ludotheque/auteurs/afficheAuteur.html', {'auteur': auteur, 'image':image})

def updateAuteur(request, id):
    auteur = models.Auteur.objects.get(pk=id)
    auteurform = AuteurForm(auteur.dic())
    return render(request, "ludotheque/auteurs/updateAuteur.html/", {"form":auteurform, "id":id})

def updatetraitementAuteur(request, id):
    auteurform = AuteurForm(data=request.POST, files=request.FILES)
    saveid = id
    if auteurform.is_valid():
        auteur = auteurform.save(commit = False)
        auteur.id = saveid
        auteur.save()
        return render(request, "ludotheque/auteurs/afficheAuteur.html", {"auteur": auteur})
    else:
        return render(request, "ludotheque/auteurs/updateAuteur.html", {"form": auteurform})

def deleteAuteur(request, id):
    suppr = models.Auteur.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/ludotheque/indexAuteur")

def indexAuteur(request):
    liste = models.Auteur.objects.all()
    return render(request, "ludotheque/auteurs/indexAuteur.html", {"liste": liste})