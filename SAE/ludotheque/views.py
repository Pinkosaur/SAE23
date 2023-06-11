from django.shortcuts import render
# from .forms import CatForm, JeuForm, AuteurForm, JoueurForm, CommForm#, ListeForm
from . import models
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, "ludotheque/index.html")

"""

# JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU JEU

def ajoutJeu(request):
    form = JeuForm()
    return render(request, "ludotheque/jeux/ajoutJeu.html", {"form": form})

def traitementJeu(request):
    jeuform = JeuForm(request.POST)
    if jeuform.is_valid():
        jeu = jeuform.save()
        return render(request, "ludotheque/jeux/afficheJeu.html", {"jeu": jeu})
    else:
        return render(request, "ludotheque/jeux/ajoutJeu.html", {"form": jeuform})

def afficheJeu(request, id):
    jeu = models.Jeu.objects.get(pk=id)
    return render(request, 'ludotheque/jeux/afficheJeu.html', {'jeu': jeu})

def updateJeu(request, id):
    jeu = models.Jeu.objects.get(pk=id)
    jeuform = JeuForm(jeu.dic())
    return render(request, "ludotheque/jeux/updateJeu.html/", {"form":jeuform, "id":id})

def updatetraitementJeu(request, id):
    jeuform = JeuForm(request.POST)
    saveid = id
    if jeuform.is_valid():
        jeu = jeuform.save(commit = False)
        jeu.id = saveid
        jeu.save()
        return HttpResponseRedirect("/ludotheque/indexJeu/")
    else:
        return render(request, "ludotheque/jeux/updateJeu.html", {"form": jeuform})

def deleteJeu(request, id):
    suppr = models.Jeu.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/ludotheque/jeux/indexJeu")

def indexJeu(request):
    liste = models.Jeu.objects.all()
    return render(request, "ludotheque/jeux/indexJeu.html", {"liste": liste})






# CATEGORIE CATEGORIE CATEGORIE CATEGORIE CATEGORIE CATEGORIE CATEGORIE CATEGORIE CATEGORIE CATEGORIE CATEGORIE

def ajoutCat(request):
    if request.method == "POST":
        form = CatForm(request)
        if form.is_valid():
            cat = form.save()
            return render(request, "ludotheque/categories/afficheCat.html", {"cat": cat})
        else:
            return render(request, "ludotheque/categories/ajoutCat.html", {"form": form})
    else:
        form = CatForm()
        return render(request, "ludotheque/categories/ajoutCat.html", {"form": form})


def traitementCat(request):
    catform = CatForm(request.POST)
    if catform.is_valid():
        cat = catform.save()
        return render(request, "ludotheque/categories/affichecat.html", {"cat": cat})
    else:
        return render(request, "ludotheque/categories/ajoutcat.html", {"cat": catform})

def afficheCat(request, id):
    cat = models.Cat.objects.get(pk=id)
    return render(request, 'ludotheque/categories/affichecat.html', {'cat': cat})

def updateCat(request, id):
    cat = models.Cat.objects.get(pk=id)
    catform = CatForm(cat.dic())
    return render(request, "ludotheque/categories/ajoutupdatecat.html/", {"form":catform, "id":id})

def updatetraitementCat(request, id):
    catform = CatForm(request.POST)
    saveid = id
    if catform.is_valid():
        cat = catform.save(commit = False)
        cat.id = saveid
        cat.save()
        return HttpResponseRedirect("/ludotheque/indexCat/")
    else:
        return render(request, "ludotheque/categories/ajoutupdatecat.html", {"form": catform})

def deleteCat(request, id):
    suppr = models.Cat.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/ludotheque/indexCat")

def indexCat(request):
    liste = models.Cat.objects.all()
    return render(request, "ludotheque/categories/indexcat.html", {"liste": liste})





# AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR AUTEUR

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




# JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR JOUEUR

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
    return render(request, 'ludotheque/joueurs/afficheJoueur.html', {'joueur': joueur})

def updateJoueur(request, id):
    joueur = models.Joueur.objects.get(pk=id)
    joueurform = JoueurForm(joueur.dic())
    return render(request, "ludotheque/joueurs/ajoutupdateJoueur.html/", {"form":joueurform, "id":id})

def updatetraitementJoueur(request, id):
    joueurform = JoueurForm(request.POST)
    saveid = id
    if joueurform.is_valid():
        joueur = joueurform.save(commit = False)
        joueur.id = saveid
        joueur.save()
        return HttpResponseRedirect("/ludotheque/indexJoueur/")
    else:
        return render(request, "ludotheque/joueurs/ajoutupdateJoueur.html", {"form": joueurform})

def deleteJoueur(request, id):
    suppr = models.Joueur.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/ludotheque/indexJoueur")

def indexJoueur(request):
    liste = models.Joueur.objects.all()
    return render(request, "ludotheque/joueurs/indexJoueur.html", {"liste": liste})




# COMMENTAIRE COMMENTAIRE COMMENTAIRE COMMENTAIRE COMMENTAIRE COMMENTAIRE COMMENTAIRE COMMENTAIRE COMMENTAIRE COMMENTAIRE

def ajoutComm(request):
    if request.method == "POST":
        form = CommForm(request)
        if form.is_valid():
            comm = form.save()
            return render(request, "ludotheque/commentaires/afficheComm.html", {"comm": comm})
        else:
            return render(request, "ludotheque/commentaires/ajoutComm.html", {"form": form})
    else:
        form = CommForm()
        return render(request, "ludotheque/commentaires/ajoutComm.html", {"form": form})
def traitementComm(request):
    commform = CommForm(request.POST)
    if commform.is_valid():
        comm = commform.save()
        return render(request, "ludotheque/commentaires/affichecomm.html", {"comm": comm})
    else:
        return render(request, "ludotheque/commentaires/ajoutcomm.html", {"comm": commform})

def afficheComm(request, id):
    comm = models.Comm.objects.get(pk=id)
    return render(request, 'ludotheque/commentaires/affichejcomm.html', {'comm': comm})

def updateComm(request, id):
    comm = models.Comm.objects.get(pk=id)
    commform = CommForm(comm.dic())
    return render(request, "ludotheque/commentaires/ajoutupdatecomm.html", {"form":commform, "id":id})

def updatetraitementComm(request, id):
    commform = CommForm(request.POST)
    saveid = id
    if commform.is_valid():
        comm = commform.save(commit = False)
        comm.id = saveid
        comm.save()
        return HttpResponseRedirect("/ludotheque/indexcomm/")
    else:
        return render(request, "ludotheque/commentaires/ajoutupdatecomm.html", {"form": commform})

def deleteComm(request, id):
    suppr = models.Comm.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/ludotheque/indexcomm")

def indexComm(request):
    liste = models.Comm.objects.all()
    return render(request, "ludotheque/commentaires/indexcomm.html", {"liste": liste})



"""

# LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE LISTE