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





# AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR

def ajoutauteur(request):
    if request.method == "POST":
        form = AuteurForm(request)
        if form.is_valid():
            auteur = form.save()
            return render(request, "ludotheque/afficheauteur.html", {"auteur": auteur})
        else:
            return render(request, "ludotheque/ajoutauteur.html", {"form": form})
    else:
        form = AuteurForm()
        return render(request, "ludotheque/ajoutauteur.html", {"form": form})

def traitementauteur(request):
    auteurform = AuteurForm(request.POST)
    if auteurform.is_valid():
        auteur = auteurform.save()
        return render(request, "ludotheque/afficheauteur.html", {"auteur": auteur})
    else:
        return render(request, "ludotheque/ajoutauteur.html", {"form": auteurform})

def afficheauteur(request, id):
    auteur = models.Auteur.objects.get(pk=id)
    return render(request, 'ludotheque/afficheauteur.html', {'auteur': auteur})

def updateauteur(request, id):
    auteur = models.Auteur.objects.get(pk=id)
    auteurform = AuteurForm(auteur.dic())
    return render(request, "ludotheque/ajoutupdateauteur.html/", {"form":auteurform, "id":id})

def updatetraitementauteur(request, id):
    auteurform = AuteurForm(request.POST)
    saveid = id
    if auteurform.is_valid():
        auteur = auteurform.save(commit = False)
        auteur.id = saveid
        auteur.save()
        return HttpResponseRedirect("/ludotheque/indexauteur/")
    else:
        return render(request, "ludotheque/ajoutupdateauteur.html", {"form": auteurform})

def deleteauteur(request, id):
    suppr = models.Auteur.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/ludotheque/indexauteur")

def indexauteur(request):
    liste = models.Auteur.objects.all()
    return render(request, "ludotheque/indexauteur.html", {"liste": liste})




# JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR

def traitementjoueur(request):
    joueurform = JoueurForm(request.POST)
    if joueurform.is_valid():
        joueur = joueurform.save()
        return render(request, "ludotheque/affichejoueur.html", {"joueur": joueur})
    else:
        return render(request, "ludotheque/ajoutjoueur.html", {"joueur": joueurform})

def affichejoueur(request, id):
    joueur = models.Joueur.objects.get(pk=id)
    return render(request, 'ludotheque/affichejjoueur.html', {'joueur': joueur})

def updatejoueur(request, id):
    joueur = models.Joueur.objects.get(pk=id)
    joueurform = JoueurForm(joueur.dic())
    return render(request, "ludotheque/ajoutupdatejoueur.html/", {"form":joueurform, "id":id})

def updatetraitementjoueur(request, id):
    joueurform = JoueurForm(request.POST)
    saveid = id
    if joueurform.is_valid():
        joueur = joueurform.save(commit = False)
        joueur.id = saveid
        joueur.save()
        return HttpResponseRedirect("/ludotheque/indexjoueur/")
    else:
        return render(request, "ludotheque/ajoutupdatejoueur.html", {"form": joueurform})

def deletejoueur(request, id):
    suppr = models.Joueur.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/ludotheque/indexjoueur")

def indexjoueur(request):
    liste = models.Joueur.objects.all()
    return render(request, "ludotheque/indexjoueur.html", {"liste": liste})




# COMMENTAIRE COMMENTAIRE COMMENTAIRE COMMENTAIRE COMMENTAIRE COMMENTAIRE COMMENTAIRE COMMENTAIRE COMMENTAIRE COMMENTAIRE
def traitementcomm(request):
    commform = CommForm(request.POST)
    if commform.is_valid():
        comm = commform.save()
        return render(request, "ludotheque/affichecomm.html", {"comm": comm})
    else:
        return render(request, "ludotheque/ajoutcomm.html", {"comm": commform})

def affichecomm(request, id):
    comm = models.Comm.objects.get(pk=id)
    return render(request, 'ludotheque/affichejcomm.html', {'comm': comm})

def updatecomm(request, id):
    comm = models.Comm.objects.get(pk=id)
    commform = CommForm(comm.dic())
    return render(request, "ludotheque/ajoutupdatecomm.html/", {"form":commform, "id":id})

def updatetraitementcomm(request, id):
    commform = CommForm(request.POST)
    saveid = id
    if commform.is_valid():
        comm = commform.save(commit = False)
        comm.id = saveid
        comm.save()
        return HttpResponseRedirect("/ludotheque/indexcomm/")
    else:
        return render(request, "ludotheque/ajoutupdatecomm.html", {"form": commform})

def deletecomm(request, id):
    suppr = models.Comm.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/ludotheque/indexcomm")

def indexcomm(request):
    liste = models.Comm.objects.all()
    return render(request, "ludotheque/indexcomm.html", {"liste": liste})





# LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE