from django.shortcuts import render
from .forms import JeuForm, JeuFichierForm
from . import models
from django.http import HttpResponseRedirect
import json

def ajoutJeu(request):
    form = JeuForm()
    return render(request, "ludotheque/jeux/ajoutJeu.html", {"form": form})

def traitementJeu(request):
    jeuform = JeuForm(data=request.POST, files=request.FILES)
    if jeuform.is_valid():
        jeu = jeuform.save()
        return render(request, "ludotheque/jeux/afficheJeu.html", {"jeu": jeu})
    else:
        return render(request, "ludotheque/jeux/ajoutJeu.html", {"form": jeuform})

def ajoutJeu_fiche(request):
    form = JeuFichierForm()
    return render(request, "ludotheque/jeux/ajoutJeu_fiche.html", {"form": form})


def traitementFichier(request):
    fichierform = JeuFichierForm(data=request.POST, files=request.FILES)
    if fichierform.is_valid():
        fichierform.save()
        fich = models.JeuFichier.objects.last().fichier
        with open(f"media/{fich}", 'r') as f:
            jeu = json.load(f)
        jeu = jeu.split(' ') # 0:titre, 1:année, 2:editeur, 3:categorie, 4:prenom, 5:nom
        if models.Auteur.objects.filter(prenomAuteur=jeu[4], nomAuteur=jeu[5]).exists():
            auteur = models.Auteur.objects.get(prenomAuteur=jeu[4], nomAuteur=jeu[5])
        else:
            auteur = models.Auteur.objects.create(prenomAuteur=jeu[4], nomAuteur=jeu[5], ageAuteur=None,
                                                  photoAuteur="images/default.png")
        nouveaujeu = models.Jeu.objects.create(titreJeu=jeu[0], anneeJeu=jeu[1], editeurJeu=jeu[2], categorieJeu=models.Cat.objects.get(nomCat=jeu[3]), auteurJeu=auteur)
        return HttpResponseRedirect("/ludotheque/indexJeu/")
    else:
        return render(request, "ludotheque/jeux/ajoutJeu_fiche.html", {"form":fichierform})


def aideFichier(request):
    return render(request, 'ludotheque/jeux/aideFichier.html')
def afficheJeu(request, id):
    jeu = models.Jeu.objects.get(pk=id)
    return render(request, 'ludotheque/jeux/afficheJeu.html', {'jeu': jeu})

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
        return render(request, "ludotheque/jeux/afficheJeu.html", {"jeu": jeu})
    else:
        return render(request, "ludotheque/jeux/updateJeu.html", {"form": jeuform})

def deleteJeu(request, id):
    suppr = models.Jeu.objects.get(pk=id)
    suppr.delete()
    return HttpResponseRedirect("/ludotheque/indexJeu/")

def indexJeu(request):
    liste = models.Jeu.objects.all()
    sommeglobal = 0.0
    sommepart = 0.0
    sommepro = 0.0
    nbnotesglobal = 0
    nbnotespart = 0
    nbnotespro = 0
    for l in liste:
        notes = models.Comm.objects.filter(jeuComm_id=l.id)


        if notes:
            for n in notes:
                if models.Joueur.objects.get(pk=n.joueurComm_id).typeJoueur == "Particulier":
                    sommepart += float(n.noteComm)
                    nbnotespart += 1
                else:
                    sommepro += float(n.noteComm)
                    nbnotespro += 1
                sommeglobal += float(n.noteComm)
                nbnotesglobal += 1
            sommeglobal /= nbnotesglobal
            if nbnotespart != 0:
                sommepart /= nbnotespart
                l.notepart = sommepart
            if nbnotespro != 0:
                sommepro /= nbnotespro
                l.notepro = sommepro
            l.notemoyenne = sommeglobal
        notepro = models.Comm.objects.filter(jeuComm_id=l.id, )
    return render(request, "ludotheque/jeux/indexJeu.html", {"liste": liste,})
