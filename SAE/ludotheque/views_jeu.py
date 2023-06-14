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
    fichierform = JeuFichierForm(request.FILES)
    if fichierform.is_valid():
        fichierform.save()
        with open(f"/media/fichiers/{fichierform.fichier}", 'r') as f:
            jeu = json.load(f)
        jeu.split(',')
        titre = jeu[0]
        annee = jeu[1]
        editeur = jeu[2]
        auteur = jeu[3].split(' ')
        prenomauteur = auteur[0]
        nomauteur = auteur[1]
        categorie = jeu[4]
        idauteur = models.Auteur.objects.get(prenomAuteur=prenomauteur, nomAuteur=nomauteur).id
        idcat = models.Cat.objects.get(nomCat=categorie).id
        if idauteur:
            idjeu =int(models.Jeu.objects.last().id) + 1
            data = f'"{idjeu}","{titre}","{annee}","","{editeur}","{idauteur}","{idcat}"'
            with open(f"/var/lib/mysql-files/entree{idjeu}.json", 'w') as f:
                json.dump(data, f)
            models.Jeu.objects.raw(f"LOAD DATA INFILE '/var/lib/mysql-files/entree{idjeu}.json' INTO TABLE ludotheque_jeu FIELDS TERMINATED BY ',' ENCLOSED BY '\"'")
#        else:
    #else retour à la page d'ajout


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
    a = 0.0
    b = 0
    for l in liste:
        notes = models.Comm.objects.filter(jeuComm_id=l.id)
        if notes:
            for n in notes:
                a += float(n.noteComm)
                b += 1
            a /= b
            l.notemoyenne = a
    return render(request, "ludotheque/jeux/indexJeu.html", {"liste": liste,})