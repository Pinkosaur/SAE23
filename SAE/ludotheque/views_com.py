from django.shortcuts import render
from .forms import CommForm_depuisjeu, CommForm_depuisjoueur
from . import models
from django.http import HttpResponseRedirect

def ajoutComm_depuisjeu(request, id):
        form = CommForm_depuisjeu()
        return render(request, "ludotheque/commentaires/ajoutComm.html", {"form": form, "idjeu":id})

def ajoutComm_depuisjoueur(request, id):
        form = CommForm_depuisjoueur()
        return render(request, "ludotheque/commentaires/ajoutComm.html", {"form": form})
def traitementComm_depuisjoueur(request):
    commform = CommForm_depuisjoueur(request.POST)
    if commform.is_valid():
        comm = commform.save()
        return render(request, "ludotheque/commentaires/affichecomm.html", {"comm": comm})
    else:
        return render(request, "ludotheque/commentaires/ajoutcomm.html", {"comm": commform})

def traitementComm_depuisjeu(request, id):
    commform = CommForm_depuisjeu(request.POST)
    if commform.is_valid():
        comm = commform.save()
        return render(request, "ludotheque/commentaires/affichecomm.html", {"comm": comm})
    else:
        return render(request, "ludotheque/commentaires/ajoutcomm.html", {"comm": commform})

def afficheComm(request, id):
    comm = models.Comm.objects.get(pk=id)
    return render(request, 'ludotheque/commentaires/affichejcomm.html', {'comm': comm})

def updateComm_depuisjoueur(request, id):
    comm = models.Comm.objects.get(pk=id)
    commform = CommForm_depuisjoueur(comm.dic())
    return render(request, "ludotheque/commentaires/ajoutupdatecomm.html", {"form":commform, "id":id})

def updateComm_depuisjeu(request, id):
    comm = models.Comm.objects.get(pk=id)
    commform = CommForm_depuisjeu(comm.dic())
    return render(request, "ludotheque/commentaires/ajoutupdatecomm.html", {"form":commform, "id":id})

def updatetraitementComm_depuisjoueur(request, id):
    commform = CommForm_depuisjoueur(request.POST)
    saveid = id
    if commform.is_valid():
        comm = commform.save(commit = False)
        comm.id = saveid
        comm.save()
        return HttpResponseRedirect("/ludotheque/indexcomm/")
    else:
        return render(request, "ludotheque/commentaires/ajoutupdatecomm.html", {"form": commform})

def updatetraitementComm_depuisjeu(request, id):
    commform = CommForm_depuisjeu(request.POST)
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

def indexComm_jeu(request, id):
    liste = models.Comm.objects.all()
    return render(request, "ludotheque/commentaires/indexcomm.html", {"liste": liste})

def indexComm_joueur(request, id):
    liste = models.Comm.objects.all()
    return render(request, "ludotheque/commentaires/indexcomm.html", {"liste": liste})