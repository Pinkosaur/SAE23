from django.shortcuts import render
from .forms import CommForm_depuisjeu, CommForm_depuisjoueur
from . import models
from django.http import HttpResponseRedirect

def ajoutComm_depuisjeu(request, id): #l'id est celui du jeu
        form = CommForm_depuisjeu()
        return render(request, "ludotheque/commentaires/ajoutComm_jeu.html", {"form": form, "idjeu":id})

def ajoutComm_depuisjoueur(request, id):
        form = CommForm_depuisjoueur()
        return render(request, "ludotheque/commentaires/ajoutComm_joueur.html", {"form": form, "idjoueur":id})
def traitementComm_depuisjoueur(request, id):
    joueur = models.Joueur.objects.get(pk=id)
    commform = CommForm_depuisjoueur(request.POST)
    if commform.is_valid():
        comm = commform.save(commit=False)
        comm.joueurComm = joueur
        comm.joueur_id = id
        comm.save()
        return render(request, "ludotheque/commentaires/afficheComm_joueur.html", {"comm": comm})
    else:
        return render(request, "ludotheque/commentaires/ajoutComm_joueur.html", {"comm": commform})

def traitementComm_depuisjeu(request, id): #l'id est celui du jeu
    jeu = models.Jeu.objects.get(pk=id)
    commform = CommForm_depuisjeu(request.POST)
    if commform.is_valid():
        comm = commform.save(commit=False)
        comm.jeuComm = jeu
        comm.jeu_id = id
        comm.save()
        return render(request, "ludotheque/commentaires/afficheComm_jeu.html", {"comm": comm})
    else:
        return render(request, "ludotheque/commentaires/ajoutComm_jeu.html", {"comm": commform})

def afficheComm_jeu(request, id):
    comm = models.Comm.objects.get(pk=id)
    return render(request, 'ludotheque/commentaires/afficheComm_jeu.html', {'comm': comm})

def afficheComm_joueur(request, id):
    comm = models.Comm.objects.get(pk=id)
    return render(request, 'ludotheque/commentaires/afficheComm_joueur.html', {'comm': comm})

def updateComm_depuisjoueur(request, id):
    comm = models.Comm.objects.get(pk=id)
    commform = CommForm_depuisjoueur(comm.dic())
    return render(request, "ludotheque/commentaires/updateComm_joueur.html", {"form":commform, "id":id})

def updateComm_depuisjeu(request, id):
    comm = models.Comm.objects.get(pk=id)
    commform = CommForm_depuisjeu(comm.dic())
    return render(request, "ludotheque/commentaires/updateComm_jeu.html", {"form":commform, "id":id})

def updatetraitementComm_depuisjoueur(request, id):
    c = models.Comm.objects.get(pk=id)
    commform = CommForm_depuisjoueur(request.POST)
    saveid = id
    if commform.is_valid():
        comm = commform.save(commit=False)
        comm.id = saveid
        comm.joueurComm_id = c.joueurComm_id
        comm.save()
        return HttpResponseRedirect(f"/ludotheque/indexComm_joueur/{c.joueurComm_id}/")
    else:
        return render(request, "ludotheque/commentaires/updateComm_joueur.html", {"form": commform})

def updatetraitementComm_depuisjeu(request, id):
    c = models.Comm.objects.get(pk=id)
    commform = CommForm_depuisjeu(request.POST)
    saveid = id
    if commform.is_valid():
        comm = commform.save(commit = False)
        comm.id = saveid
        comm.jeuComm_id = c.jeuComm_id
        comm.save()
        return HttpResponseRedirect(f"/ludotheque/indexComm_jeu/{c.jeuComm_id}/")
    else:
        return render(request, "ludotheque/commentaires/updateComm_jeu.html", {"form": commform})

def deleteComm(request, id):
    suppr = models.Comm.objects.get(pk=id)
    suppr.delete()
    return render(request, "ludotheque/commentaires/deleted.html")

def indexComm_jeu(request, id): #id du jeu
    list = models.Comm.objects.filter(jeuComm=id).order_by('-noteComm')
    return render(request, "ludotheque/commentaires/indexComm_jeu.html", {"liste": list, "idjeu":id})

def indexComm_joueur(request, id):
    liste = models.Comm.objects.filter(joueurComm=id)
    return render(request, "ludotheque/commentaires/indexComm_joueur.html", {"liste": liste, "idjoueur":id})