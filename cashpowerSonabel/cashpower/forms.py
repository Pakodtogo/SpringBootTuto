# gestion_abonnements/forms.py
from django import forms
from .models import Exploitation, PointDeVente, Guichet, Branchement, EtatAbonnement, Compteur, Abonne, Tarif, TrancheTarif, Abonnement, Vente

class ExploitationForm(forms.ModelForm):
    class Meta:
        model = Exploitation
        fields = ['numero_exploitation', 'designation']
        labels = {
            'numero_exploitation': 'Numéro d\'exploitation',
            'designation': 'Désignation',
        }
        widgets = {
            'numero_exploitaton': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PointDeVenteForm(forms.ModelForm):
    class Meta:
        model = PointDeVente
        fields = ['code_pdv', 'libelle', 'exploitation']
        labels = {
            'code_pdv': 'Code du point de vente',
            'libelle': 'Libellé',
            'exploitation': 'Exploitation',
        }
        widgets = {
            'code_pdv': forms.TextInput(attrs={'class': 'form-control'}),
            'libelle': forms.TextInput(attrs={'class': 'form-control'}),
            'exploitation': forms.Select(attrs={'class': 'form-control'}),
        }

class GuichetForm(forms.ModelForm):
    class Meta:
        model = Guichet
        fields = ['pointDeVente','numero_guichet']
        labels = {
            'pointDeVente': 'Point de vente',
            'numero_guichet': 'Numéro de guichet',
        }
        widgets = {
            'pointDeVente': forms.Select(attrs={'class':'form-control'}),
            'numero_guichet': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BranchementForm(forms.ModelForm):
    class Meta:
        model = Branchement
        fields = ['type_branchement', 'exploitation', 'section', 'lot', 'parcelle', 'rang']
        labels = {
            'type_branchement': 'Type de branchement',
            'exploitation': 'Exploitation',
            'section': 'Section',
            'lot': 'Lot',
            'parcelle': 'Parcelle',
            'rang': 'Rang',
        }
        widgets = {
            'type_branchement': forms.TextInput(attrs={'class': 'form-control'}),
            'exploitation': forms.Select(attrs={'class': 'form-control'}),
            'section': forms.TextInput(attrs={'class': 'form-control'}),
            'lot': forms.TextInput(attrs={'class': 'form-control'}),
            'parcelle': forms.TextInput(attrs={'class': 'form-control'}),
            'rang': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EtatAbonnementForm(forms.ModelForm):
    class Meta:
        model = EtatAbonnement
        fields = ['code_etat', 'libele']
        labels = {
            'code_etat': 'Code d\'état',
            'libele': 'Libellé',
        }
        widgets = {
            'code_etat': forms.TextInput(attrs={'class': 'form-control'}),
            'libele': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CompteurForm(forms.ModelForm):
    class Meta:
        model = Compteur
        fields = ['numero_compteur', 'modele_compteur', 'mode_facturation', 'numero_carte']
        labels = {
            'numero_compteur': 'Numéro de compteur',
            'modele_compteur': 'Modèle de compteur',
            'mode_facturation': 'Mode de facturation',
            'numero_carte': 'Numéro de carte',
        }
        widgets = {
            'numero_compteur': forms.TextInput(attrs={'class': 'form-control'}),
            'modele_compteur': forms.TextInput(attrs={'class': 'form-control'}),
            'mode_facturation': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_carte': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AbonneForm(forms.ModelForm):
    class Meta:
        model = Abonne
        fields = ['nom', 'prenom', 'numero_telephone', 'adresse_mail', 'numero_cnib']
        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'numero_telephone': 'Numéro de téléphone',
            'adresse_mail': 'Adresse e-mail',
            'numero_cnib': 'Numéro de CNIB',
        }
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse_mail': forms.EmailInput(attrs={'class': 'form-control'}),
            'numero_cnib': forms.TextInput(attrs={'class': 'form-control'}),
        }
        

class TarifForm(forms.ModelForm):
    class Meta:
        model = Tarif
        fields = ['code_tarif', 'prime_fixe', 'redevance', 'amperage']
        labels = {
            'code_tarif': 'Code du tarif',
            'prime_fixe': 'Prime fixe',
            'redevance': 'Redevance',
            'amperage': 'Amperage',
        }
        widgets = {
            'code_tarif': forms.TextInput(attrs={'class': 'form-control'}),
            'prime_fixe': forms.NumberInput(attrs={'class': 'form-control'}),
            'redevance': forms.NumberInput(attrs={'class': 'form-control'}),
            'amperage': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class TrancheTarifForm(forms.ModelForm):
    class Meta:
        model = TrancheTarif
        fields = ['debut', 'fin', 'cout_ht', 'tde_trch', 'tsdaae_trch', 'tva_trch', 'tarif']
        labels = {
            'debut': 'Début',
            'fin': 'Fin',
            'cout_ht': 'Coût HT',
            'tde_trch': 'TDE Tranche',
            'tsdaae_trch': 'TSDAAE Tranche',
            'tva_trch': 'TVA Tranche',
            'tarif': 'Tarif',
        }
        widgets = {
            'debut': forms.NumberInput(attrs={'class': 'form-control'}),
            'fin': forms.NumberInput(attrs={'class': 'form-control'}),
            'cout_ht': forms.NumberInput(attrs={'class': 'form-control'}),
            'tde_trch': forms.NumberInput(attrs={'class': 'form-control'}),
            'tsdaae_trch': forms.NumberInput(attrs={'class': 'form-control'}),
            'tva_trch': forms.NumberInput(attrs={'class': 'form-control'}),
            'tarif': forms.Select(attrs={'class': 'form-control'}),
        }

class AbonnementForm(forms.ModelForm):
    class Meta:
        model = Abonnement
        exclude = ['numero_abonnement', 'numero_police', 'timbre', 'liasse', 'frais_police']

        labels = {
            'abonne': 'Abonné',
            'branchement': 'Branchement',
            'etat_abonnement': 'État d\'abonnement',
            'compteur': 'Compteur',
            'tarif': 'Tarif',
            'guichet': 'N° Guichet',
        }

        widgets = {
            'date_creation': forms.HiddenInput(),
            'date_mise_en_service': forms.HiddenInput(),
            'date_resiliation': forms.HiddenInput(),
            'abonne': forms.Select(attrs={'class': 'form-control form-select', 'placeholder': 'Abonné'}),
            'branchement': forms.Select(attrs={'class': 'form-control form-select'}),
            'etat_abonnement': forms.Select(attrs={'class': 'form-control form-select'}),
            'compteur': forms.Select(attrs={'class': 'form-control form-select'}),
            'tarif': forms.Select(attrs={'class': 'form-control form-select form-select'}),
            'guichet': forms.Select(attrs={'class': 'form-control form-select'}),
            'timbre': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'liasse': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'numero_police': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'frais_police': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
        }


class VenteForm(forms.ModelForm):
    class Meta:
        model = Vente
        fields = ['montant', 'abonnement', 'guichet']
        labels = {
            'montant': 'Montant',
            'abonnement': 'Abonnement',
            'guichet': 'N° Guichet',
        }
        widgets = {

            'montant': forms.NumberInput(attrs={'class': 'form-control'}),
            'abonnement': forms.Select(attrs={'class': 'form-control'}),
            'guichet': forms.Select(attrs={'class': 'form-control'}),
        }

