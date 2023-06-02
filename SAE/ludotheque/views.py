from django.shortcuts import render
from .forms import CatForm, JeuForm, AuteurForm, JoueurForm, CommForm, ListeForm
from . import models
from django.http import HttpResponseRedirect

# Create your views here.



# JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU

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




# CATEGORIE CATEGORIE CATEGORIE CATEGORIE CATEGORIE CATEGORIE CATEGORIE CATEGORIE CATEGORIE CATEGORIE CATEGORIE

def traitementcat(request):
    catform = CatForm(request.POST)
    if catform.is_valid():
        cat = catform.save()
        return render(request, "ludotheque/affichecat.html", {"cat": cat})
    else:
        return render(request, "ludotheque/ajoutcat.html", {"cat": catform})

def affichecat(request, id):
    cat = models.Cat.objects.get(pk=id)
    return render(request, 'ludotheque/affichejcat.html', {'cat': cat})

def updatecat(request, id):
    cat = models.Cat.objects.get(pk=id)
    catform = CatForm(cat.dic())
    return render(request, "ludotheque/ajoutupdatecat.html/", {"form":catform, "id":id})

def updatetraitementcat(request, id):
    catform = CatForm(request.POST)
    saveid = id
    if catform.is_valid():
        cat = catform.save(commit = False)
        cat.id = saveid
        cat.save()
        return HttpResponseRedirect("/ludotheque/indexcat/")
    else:
        return render(request, "ludotheque/ajoutupdatecat.html", {"form": catform})

def deletecat(request, id):
    suppr = models.Cat.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/ludotheque/indexcat")

def indexcat(request):
    liste = models.Cat.objects.all()
    return render(request, "ludotheque/indexcat.html", {"liste": liste})