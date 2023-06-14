from django.shortcuts import render
from .forms import CatForm
from . import models
from django.http import HttpResponseRedirect

def ajoutCat(request):
    form = CatForm()
    return render(request, "ludotheque/categories/ajoutCat.html", {"form": form})


def traitementCat(request):
    catform = CatForm(request.POST)
    if catform.is_valid():
        cat = catform.save()
        return render(request, "ludotheque/categories/afficheCat.html", {"cat": cat})
    else:
        return render(request, "ludotheque/categories/ajoutCat.html", {"cat": catform})

def afficheCat(request, id):
    cat = models.Cat.objects.get(pk=id)
    return render(request, 'ludotheque/categories/afficheCat.html', {'cat': cat})

def updateCat(request, id):
    cat = models.Cat.objects.get(pk=id)
    catform = CatForm(cat.dic())
    return render(request, "ludotheque/categories/ajoutupdateCat.html/", {"form":catform, "id":id})

def updatetraitementCat(request, id):
    catform = CatForm(request.POST)
    saveid = id
    if catform.is_valid():
        cat = catform.save(commit = False)
        cat.id = saveid
        cat.save()
        return HttpResponseRedirect("/ludotheque/indexCat/")
    else:
        return render(request, "ludotheque/categories/ajoutupdateCat.html", {"form": catform})

def deleteCat(request, id):
    suppr = models.Cat.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/ludotheque/indexCat")

def indexCat(request):
    liste = models.Cat.objects.all()
    return render(request, "ludotheque/categories/indexCat.html", {"liste": liste})

