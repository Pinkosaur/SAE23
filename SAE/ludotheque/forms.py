from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class JeuForm(ModelForm):
    class Meta:
        model = models.Jeu
        fields = ("titreJeu", "anneeJeu", "photoJeu", "editeurJeu", "auteurJeu", "categorieJeu"
                  )
        labels = {
            'titreJeu': _('Titre du jeu'),
            'anneeJeu': _('Année de parution'),
            'photoJeu': _('Photo de la boîte'),
            'editeurJeu': _('Éditeur'),
            'auteurJeu': _('Auteur'),
            'categorieJeu': _('Catégorie')
        }

class CatForm(ModelForm):
    class Meta:
        model = models.Cat
        fields = ("nomCat", "descriptifCat")
        labels = {
            'nomCat': _('Nom de la catégorie'),
            'descriptifCat': _('Description'),
        }

class AuteurForm(ModelForm):
    class Meta:
        model = models.Auteur
        fields = ("nomAuteur", "prenomAuteur", "ageAuteur", "photoAuteur")
        labels = {
            'nomAuteur': _('Nom'),
            'prenomAuteur': _('Prénom'),
            'ageAuteur': _('Age'),
            'photoAuteur': _('Photo'),
        }

class JoueurForm(ModelForm):
    class Meta:
        model = models.Joueur
        fields = ("nomJoueur", "prenomJoueur", "emailJoueur", "mdpJoueur", "typeJoueur"
                  )
        labels = {
            'nomJoueur': _('Nom'),
            'prenomJoueur': _('Prénom'),
            'emailJoueur': _('Email'),
            'mdpJoueur': _('Mot de passe'),
            'typeJoueur': _('Type de joueur'),
        }

class CommForm_depuisjoueur(ModelForm):
    class Meta:
        model = models.Comm
        fields = ("jeuComm", "noteComm", "contenuComm")
        labels = {
            'jeuComm': _('Titre du jeu'),
            'noteComm': _('Note'),
            'contenuComm': _('Commentaire'),
        }

class CommForm_depuisjeu(ModelForm):
    class Meta:
        model = models.Comm
        fields = ("joueurComm", "noteComm", "contenuComm")
        labels = {
            'joueurComm': _('Joueur commentant ce jeu'),
            'noteComm': _('Note'),
            'contenuComm': _('Commentaire'),
        }

class ListeForm(ModelForm):
    class Meta:
        model = models.Liste
        fields = ('jeuListe',)
        labels = {'jeuListe': _('Choisir un jeu')}