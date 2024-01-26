# gestion_abonnements/urls.py
from django.urls import path
from .views import (
    abonne_list, abonne_detail, abonne_create, abonne_edit,
    abonnement_list, abonnement_detail, abonnement_create, abonnement_edit,
    vente_list, vente_detail, vente_create, vente_edit, home
)

urlpatterns = [
    # URL pour Abonne
    path('', home, name='home'), 
    path('abonnes/', abonne_list, name='abonne_list'),
    path('abonnes/<int:pk>/', abonne_detail, name='abonne_detail'),
    path('abonnes/create/', abonne_create, name='abonne_create'),
    path('abonnes/<int:pk>/edit/', abonne_edit, name='abonne_edit'),

    # URL pour Abonnement
    path('abonnements/', abonnement_list, name='abonnement_list'),
    path('abonnements/<int:pk>/', abonnement_detail, name='abonnement_detail'),
    path('abonnements/create/', abonnement_create, name='abonnement_create'),
    path('abonnements/<int:pk>/edit/', abonnement_edit, name='abonnement_edit'),

    # URL pour Vente
    path('ventes/', vente_list, name='vente_list'),
    path('ventes/<int:pk>/', vente_detail, name='vente_detail'),
    path('ventes/create/', vente_create, name='vente_create'),
    path('ventes/<int:pk>/edit/', vente_edit, name='vente_edit'),
]
