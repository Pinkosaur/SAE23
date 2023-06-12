from django.db import models
import django.utils.timezone

# Create your models here.
class Cat(models.Model): #Catégorie de jeux
    nomCat = models.CharField(max_length=100)
    descriptifCat = models.TextField(null = False, blank = True)
    def __str__(self):
        chaine = f"{self.nomCat}"
        return chaine
    def dic(self):
        return {"nomCat": self.nomCat, "descriptifCat": self.descriptifCat}

class Jeu(models.Model):
    titreJeu = models.CharField(max_length=50)
    anneeJeu = models.IntegerField()
    photoJeu = models.ImageField(blank=True, upload_to='images') #Peut être à compléter avec (upload_to="...")
    editeurJeu = models.CharField(max_length=50)
    auteurJeu = models.ForeignKey("Auteur", on_delete=models.CASCADE, default=None)
    categorieJeu = models.ForeignKey("Cat", on_delete=models.CASCADE, default=None)
    def __str__(self):
        chaine = f"{self.titreJeu}"
        return chaine
    def dic(self):
        return {"titreJeu": self.titreJeu, "anneeJeu": self.anneeJeu, "photoJeu": self.photoJeu, "editeurJeu": self.editeurJeu,
        "auteurJeu":self.auteurJeu, "categorieJeu": self.categorieJeu        }

class Auteur(models.Model):
    nomAuteur = models.CharField(max_length=25)
    prenomAuteur = models.CharField(max_length=25)
    ageAuteur = models.IntegerField(blank=True, null=True)
    photoAuteur = models.ImageField(blank=True, null=True)  #Peut être à compléter avec (upload_to="...")
    def __str__(self):
        chaine = f"{self.prenomAuteur} {self.nomAuteur}"
        return chaine
    def dic(self):
        return {"nomAuteur": self.nomAuteur, "prenomAuteur": self.prenomAuteur, "ageAuteur": self.ageAuteur, "photoAuteur": self.photoAuteur,
                }


TYPE = (
        ("Particulier", "Particulier"),
        ("Professionnel", "Professionnel")
        )

class Joueur(models.Model):
    nomJoueur = models.CharField(max_length=25)
    prenomJoueur = models.CharField(max_length=25)
    emailJoueur = models.EmailField(blank=False, null=False, default="test@test.test")
    mdpJoueur = models.CharField(max_length=30)
    typeJoueur = models.CharField(max_length=30, choices=TYPE, default="Particulier")
    def __str__(self):
        chaine = f"{self.prenomJoueur} {self.nomJoueur}, {self.typeJoueur}"
        return chaine
    def dic(self):
        return {"nomJoueur": self.nomJoueur, "prenomJoueur": self.prenomJoueur, "emailJoueur": self.emailJoueur,
                "mdpJoueur": self.mdpJoueur,
                }



class Comm(models.Model): #Commentaires sur les jeux
    jeuComm = models.ForeignKey("jeu", on_delete=models.CASCADE)  #Jeu commenté
    joueurComm = models.ForeignKey("joueur", on_delete=models.CASCADE)
    noteComm = models.FloatField(blank=False, max_length=2)  # Note attribuée
    contenuComm = models.TextField(null = False, blank = False)
    dateComm = models.DateField(default = django.utils.timezone.now())
    def dic(self):
        return {"jeuComm": self.jeuComm, "joueurComm": self.joueurComm, "noteComm": self.noteComm,
                "contenuComm": self.contenuComm, "dateComm": self.dateComm
                }


class Liste(models.Model):
    joueurListe = models.ForeignKey("joueur", on_delete=models.CASCADE)
    jeuListe = models.ForeignKey("jeu", on_delete=models.CASCADE)
    def dic(self):
        return {"joueurListe":self.joueurListe, "jeuListe":self.jeuListe}
    def __str__(self):
        chaine = f"{self.jeuListe}"
        return chaine