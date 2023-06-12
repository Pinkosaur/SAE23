from django.shortcuts import render
from .forms import JeuForm
from . import models
from django.http import HttpResponseRedirect
def ajoutJeu(request):
    form = JeuForm()
    return render(request, "ludotheque/jeux/ajoutJeu.html", {"form": form})

def traitementJeu(request):
    jeuform = JeuForm(data=request.POST, files=request.FILES)
    if jeuform.is_valid():
        jeu = jeuform.save()
        image = jeu.photoJeu
        return render(request, "ludotheque/jeux/afficheJeu.html", {"jeu": jeu, 'image':image})
    else:
        return render(request, "ludotheque/jeux/ajoutJeu.html", {"form": jeuform})

def afficheJeu(request, id):
    jeu = models.Jeu.objects.get(pk=id)
    image = jeu.photoJeu
    return render(request, 'ludotheque/jeux/afficheJeu.html', {'jeu': jeu, 'image':image})

def updateJeu(request, id):
    jeu = models.Jeu.objects.get(pk=id)
    jeuform = JeuForm(jeu.dic())
    return render(request, "ludotheque/jeux/updateJeu.html/", {"form":jeuform, "id":id})

def updatetraitementJeu(request, id):
    jeuform = JeuForm(data=request.POST, files=request.FILES)
    saveid = id
    if jeuform.is_valid():
        jeu = jeuform.save(commit = False)
        jeu.id = saveid
        jeu.save()
        image = jeu.photoJeu
        return render(request, "ludotheque/jeux/afficheJeu.html", {"jeu": jeu, 'image':image})
    else:
        return render(request, "ludotheque/jeux/updateJeu.html", {"form": jeuform})

def deleteJeu(request, id):
    suppr = models.Jeu.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/ludotheque/indexJeu")

def indexJeu(request):
    liste = models.Jeu.objects.all()
    return render(request, "ludotheque/jeux/indexJeu.html", {"liste": liste})