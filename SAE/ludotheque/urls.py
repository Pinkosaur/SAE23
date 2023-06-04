from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index),

    path('ajoutJeu/', views.ajoutJeu),
    path('traitementJeu/', views.traitementJeu),
    path('afficheJeu/', views.afficheJeu),
    path('updateJeu/', views.updateJeu),
    path('updatetraitementJeu/', views.updatetraitementJeu),
    path('deleteJeu/', views.deleteJeu),
    path('indexJeu/', views.indexJeu),

    path('ajoutCat/', views.ajoutCat),
    path('traitementCat/', views.traitementCat),
    path('afficheCat/', views.afficheCat),
    path('updateCat/', views.updateCat),
    path('updatetraitementCat/', views.updatetraitementCat),
    path('deleteCat/', views.deleteCat),
    path('indexCat/', views.indexCat),

    path('ajoutAuteur/', views.ajoutAuteur),
    path('traitementAuteur/', views.traitementAuteur),
    path('afficheAuteur/', views.afficheAuteur),
    path('updateAuteur/', views.updateAuteur),
    path('updatetraitementAuteur/', views.updatetraitementAuteur),
    path('deleteAuteur/', views.deleteAuteur),
    path('indexAuteur/', views.indexAuteur),

    path('ajoutJoueur/', views.ajoutJoueur),
    path('traitementJoueur/', views.traitementJoueur),
    path('afficheJoueur/', views.afficheJoueur),
    path('updateJoueur/', views.updateJoueur),
    path('updatetraitementJoueur/', views.updatetraitementJoueur),
    path('deleteJoueur/', views.deleteJoueur),
    path('indexJoueur/', views.indexJoueur),

    path('ajoutComm/', views.ajoutComm),
    path('traitementComm/', views.traitementComm),
    path('afficheComm/', views.afficheComm),
    path('updateComm/', views.updateComm),
    path('updatetraitementComm/', views.updatetraitementComm),
    path('deleteComm/', views.deleteComm),
    path('indexComm/', views.indexComm),

    # Liste
    ]
