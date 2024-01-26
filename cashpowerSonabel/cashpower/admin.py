from django.contrib import admin
from .models import Abonnement, Exploitation, PointDeVente, Guichet, Branchement, EtatAbonnement, Compteur, Abonne, Tarif, TrancheTarif, Vente

# Register your models here.
admin.site.register(Branchement)
admin.site.register(Exploitation)
admin.site.register(PointDeVente)
admin.site.register(Guichet)
admin.site.register(EtatAbonnement)
admin.site.register(Compteur)
admin.site.register(Abonne)
admin.site.register(Tarif)
admin.site.register(TrancheTarif)
admin.site.register(Abonnement)
admin.site.register(Vente)