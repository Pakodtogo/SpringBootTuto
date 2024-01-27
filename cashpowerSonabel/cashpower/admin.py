from django.contrib import admin
from django.utils.translation import gettext as _
from .models import Abonnement, Exploitation, PointDeVente, Guichet, Branchement, EtatAbonnement, Compteur, Abonne, Tarif, TrancheTarif, Vente

# Register your models here.
class AdminAbonne(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom', 'numero_telephone', 'adresse_mail', 'numero_cnib')

class AdminAbonnement(admin.ModelAdmin):
    list_display = ('id', 'numero_abonnement', 'date_creation', 'date_mise_en_service', 'date_resiliation', 'timbre', 'liasse', 'numero_police', 'frais_police',)

class AdminBranchement(admin.ModelAdmin):
    list_display = ('id', 'type_branchement', 'section', 'lot', 'parcelle', 'rang', 'exploitation')
    
class AdminCompteure(admin.ModelAdmin):
    list_display = ('numero_compteur', 'modele_compteur', 'mode_facturation', 'numero_carte')
    class Media:
        css = {
            'all': ('css/custom_admin_styles.css',),
        }

class AdminEtatAbonnement(admin.ModelAdmin):
    list_display = ('code_etat', 'libele')
    
class AdminExploitation(admin.ModelAdmin):
    list_display = ('numero_exploitation', 'designation')
    
class AdminPointDeVente(admin.ModelAdmin):
    list_display = ('code_pdv', 'libelle', 'exploitation')
 
class AdminGuichet(admin.ModelAdmin):
    list_display = ('numero_guichet', 'pointDeVente')

class AdminTarif(admin.ModelAdmin):
    list_display = ('code_tarif', 'prime_fixe', 'redevance', 'amperage')
     
class AdminTrancheTarif(admin.ModelAdmin):
    list_display = ('id', 'debut', 'fin', 'cout_ht', 'tde_trch', 'tsdaae_trch', 'tva_trch', 'tarif')
   
class AdminVente(admin.ModelAdmin):
    list_display = ('numero_ticket', 'montant', 'tqr', 'date', 'energie_paye', 'tde', 'tsdaae', 'tva', 'cout_energie', 'code_token', 'abonnement', 'guichet')
       
admin.site.register(Branchement, AdminBranchement)
admin.site.register(Exploitation, AdminExploitation)
admin.site.register(PointDeVente, AdminPointDeVente)
admin.site.register(Guichet, AdminGuichet)
admin.site.register(EtatAbonnement, AdminEtatAbonnement)
admin.site.register(Compteur, AdminCompteure)
admin.site.register(Abonne, AdminAbonne)
admin.site.register(Tarif, AdminTarif)
admin.site.register(TrancheTarif, AdminTrancheTarif)
admin.site.register(Abonnement, AdminAbonnement)
admin.site.register(Vente, AdminVente)

# Configuration du titre, de l'en-tête et du titre de l'index
admin.site.site_title = _("CASHPOWER SYSTEM")
admin.site.site_header = _("CASHPOWER SYSTEM")
admin.site.index_title = _("CASHPOWER SYSTEM")

