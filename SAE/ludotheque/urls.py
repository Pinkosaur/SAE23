from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index),

    path('ajoutJeu/', views.ajoutJeu),
    path('traitementJeu', views.traitementJeu),
    path('afficheJeu/<int:id>/', views.afficheJeu),
    path('updateJeu/<int:id>/', views.updateJeu),
    path('updatetraitementJeu/<int:id>/', views.updatetraitementJeu),
    path('deleteJeu/<int:id>/', views.deleteJeu),
    path('indexJeu/', views.indexJeu),

    path('ajoutCat/', views.ajoutCat),
    path('traitementCat', views.traitementCat),
    path('afficheCat/<int:id>/', views.afficheCat),
    path('updateCat/<int:id>/', views.updateCat),
    path('updatetraitementCat/<int:id>/', views.updatetraitementCat),
    path('deleteCat/<int:id>/', views.deleteCat),
    path('indexCat/', views.indexCat),

    path('ajoutAuteur/', views.ajoutAuteur),
    path('traitementAuteur', views.traitementAuteur),
    path('afficheAuteur/<int:id>/', views.afficheAuteur),
    path('updateAuteur/<int:id>/', views.updateAuteur),
    path('updatetraitementAuteur/<int:id>/', views.updatetraitementAuteur),
    path('deleteAuteur/<int:id>/', views.deleteAuteur),
    path('indexAuteur/', views.indexAuteur),

    path('ajoutJoueur/', views.ajoutJoueur),
    path('traitementJoueur', views.traitementJoueur),
    path('afficheJoueur/<int:id>/', views.afficheJoueur),
    path('updateJoueur/<int:id>/', views.updateJoueur),
    path('updatetraitementJoueur/<int:id>/', views.updatetraitementJoueur),
    path('deleteJoueur/<int:id>/', views.deleteJoueur),
    path('indexJoueur/', views.indexJoueur),

    path('ajoutComm/', views.ajoutComm),
    path('traitementComm', views.traitementComm),
    path('afficheComm/<int:id>/', views.afficheComm),
    path('updateComm/<int:id>/', views.updateComm),
    path('updatetraitementComm/<int:id>/', views.updatetraitementComm),
    path('surprise/', views.troll),
    path('gigapute/', views.gigapute),
    path('deleteComm/<int:id>/', views.deleteComm),
    path('indexComm/', views.indexComm),

    # Liste
    ]
