from django.db import models

# Create your models here.
class Cat(models.Model): #Catégorie de jeux
    nomCat = models.CharField(max_length=100)
    descriptifCat = models.TextField(null = False, blank = True)

class Jeu(models.Model):
    titreJeu = models.CharField(max_length=50)
    anneeJeu =
    photoJeu =
    editeurJeu = models.CharField(max_length=50)
    auteurJeu = # ID auteur
    categorieJeu = # ID cat jeu

class Auteur(models.Model):
    nomAuteur = models.CharField(max_length=25)
    prenomAuteur = models.CharField(max_length=25)
    ageAuteur =
    photoAuteur =

class Joueur(models.Model):
    nomJoueur = models.CharField(max_length=25)
    prenomJoueur = models.CharField(max_length=25)
    emailjoueur =
    mdpJoueur = models.CharField(max_length=30)
    typeJoueur = models.Choices(["Professionnel", "Particulier"])

class Comm(models.Model): #Commentaires sur les jeux
    jeuComm = models.CharField(max_length=50)
    joueurComm = models.CharField(max_length=25)
    noteComm = models.FloatField(blank=False)
    contenuComm = models.TextField(null = False, blank = False)
    dateComm = models.DateField(blank=False, null = False)

class Liste(models.Model): #liste personnelle pour chaque joueur contenant ses jeux
    joueurListe =
    jeuxListe =