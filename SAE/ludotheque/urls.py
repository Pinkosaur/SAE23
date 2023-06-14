from django.urls import path
from . import views, views_cat, views_com, views_jeu, views_jou, views_lis, views_aut


urlpatterns = [
    path('', views.index),

    path('ajoutJeu/', views_jeu.ajoutJeu),
    path('traitementJeu', views_jeu.traitementJeu),
    path('afficheJeu/<int:id>/', views_jeu.afficheJeu),
    path('updateJeu/<int:id>/', views_jeu.updateJeu),
    path('updatetraitementJeu/<int:id>/', views_jeu.updatetraitementJeu),
    path('deleteJeu/<int:id>/', views_jeu.deleteJeu),
    path('indexJeu/', views_jeu.indexJeu),
    path('ajoutJeu_fiche/', views_jeu.ajoutJeu_fiche),
    path('traitementFichier/', views_jeu.traitementFichier),
    path('aideFichier/', views_jeu.aideFichier),

    path('ajoutCat/', views_cat.ajoutCat),
    path('traitementCat', views_cat.traitementCat),
    path('afficheCat/<int:id>/', views_cat.afficheCat),
    path('updateCat/<int:id>/', views_cat.updateCat),
    path('updatetraitementCat/<int:id>/', views_cat.updatetraitementCat),
    path('deleteCat/<int:id>/', views_cat.deleteCat),
    path('indexCat/', views_cat.indexCat),

    path('ajoutAuteur/', views_aut.ajoutAuteur),
    path('traitementAuteur/', views_aut.traitementAuteur),
    path('afficheAuteur/<int:id>/', views_aut.afficheAuteur),
    path('updateAuteur/<int:id>/', views_aut.updateAuteur),
    path('updatetraitementAuteur/<int:id>/', views_aut.updatetraitementAuteur),
    path('deleteAuteur/<int:id>/', views_aut.deleteAuteur),
    path('indexAuteur/', views_aut.indexAuteur),

    path('ajoutJoueur/', views_jou.ajoutJoueur),
    path('traitementJoueur/', views_jou.traitementJoueur),
    path('afficheJoueur/<int:id>/', views_jou.afficheJoueur),
    path('updateJoueur/<int:id>/', views_jou.updateJoueur),
    path('updatetraitementJoueur/<int:id>/', views_jou.updatetraitementJoueur),
    path('deleteJoueur/<int:id>/', views_jou.deleteJoueur),
    path('indexJoueur/', views_jou.indexJoueur),

    path('ajoutComm_joueur/<int:id>/', views_com.ajoutComm_depuisjoueur),
    path('ajoutComm_jeu/<int:id>/', views_com.ajoutComm_depuisjeu),
    path('traitementComm_joueur/<int:id>/', views_com.traitementComm_depuisjoueur),
    path('traitementComm_jeu/<int:id>/', views_com.traitementComm_depuisjeu),
    path('afficheComm/<int:id>/', views_com.afficheComm),
    path('updateComm_joueur/<int:id>/', views_com.updateComm_depuisjoueur),
    path('updateComm_jeu/<int:id>/', views_com.updateComm_depuisjeu),
    path('updatetraitementComm_joueur/<int:id>/', views_com.updatetraitementComm_depuisjoueur),
    path('updatetraitementComm_jeu/<int:id>/', views_com.updatetraitementComm_depuisjeu),
    path('deleteComm/<int:id>/', views_com.deleteComm),
    path('indexComm_jeu/<int:id>/', views_com.indexComm_jeu),
    path('indexComm_joueur/<int:id>/', views_com.indexComm_joueur),

    # Liste
    path("ajoutListe/<int:id>/", views_lis.ajoutListe),
    path('traitementListe/<int:id>/', views_lis.traitementListe),
    path("afficheListe/<int:id>/", views_lis.afficheListe),
    path("updateListe/<int:id>/", views_lis.updateListe),
    path('updatetraitementListe/<int:id>/', views_lis.updatetraitementListe),
    path('deleteListe/<int:id>/', views_lis.deleteListe),
    path("indexListe/<int:id>/", views_lis.indexListe),
    ]
