from django.db import models

# Create your models here.
class Cat(models.Model): #Catégorie de jeux
    nomCat = models.CharField(max_length=100)
    descriptifCat = models.TextField(null = False, blank = True)

class Jeu(models.Model):
    titreJeu = models.CharField(max_length=50)
    anneeJeu = models.IntegerField()
    photoJeu = models.ImageField(blank=True) #Peut être à compléter avec (upload_to="...")
    editeurJeu = models.CharField(max_length=50)
#    auteurJeu = # ID auteur
#    categorieJeu = # ID cat jeu
    def dic(self):
        return {"titreJeu": self.titreJeu, "anneeJeu": self.anneeJeu, "photoJeu": self.photoJeu, "editeurJeu": self.editeurJeu,
                }

class Auteur(models.Model):
    nomAuteur = models.CharField(max_length=25)
    prenomAuteur = models.CharField(max_length=25)
    ageAuteur = models.IntegerField(blank=True, null=True)
    photoAuteur = models.ImageField(blank=True, null=True)  #Peut être à compléter avec (upload_to="...")

class Joueur(models.Model):
    nomJoueur = models.CharField(max_length=25)
    prenomJoueur = models.CharField(max_length=25)
    emailJoueur = models.EmailField(blank=False, null=False)
    mdpJoueur = models.CharField(max_length=30)
"""    PARTICULIER = "0"
    PROFESSIONNEL = "1"
    TYPE = [
        (PARTICULIER, "Particulier"),
        (PROFESSIONNEL, "Professionnel"),
    ]
    typeJoueur = models.CharField(
        choices = TYPE,
        default=PARTICULIER,
    )"""

"""class Comm(models.Model): #Commentaires sur les jeux
    jeuComm = models.CharField(max_length=50)  #Jeu commenté
    emailJoueurComm = models.CharField(choices=Joueur.emailJoueur)  # Joueur qui commente / à modifier, pour associer à l'ID et pas au nom
#    idJoueurComm =  Joueur.objects.raw("SELECT id FROM Joueur WHERE Joueur.nomJoueur=Comm.nomJoueurComm")  #à voir/corriger
    noteComm = models.FloatField(blank=False)  # Note attribuée
    contenuComm = models.TextField(null = False, blank = False)
    dateComm = models.DateField(blank=False, null = False) # à changer --> date auto
"""
#class Liste(models.Model): #liste personnelle pour chaque joueur contenant ses jeux
#    joueurListe = models."???"
#    jeuxListe = models."???"

class Troll(models.Model):
    nombre = models.IntegerField(blank=False, null=False)