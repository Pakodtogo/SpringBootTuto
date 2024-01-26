# gestion_abonnements/models.py
from django.db import models


class Exploitation(models.Model):
    numero_exploitation = models.CharField(primary_key=True,max_length=255)
    designation = models.CharField(max_length=255, blank=False, null=False)
    def __str__(self):
        return self.designation


class PointDeVente(models.Model):
    code_pdv = models.CharField(primary_key=True, max_length=255, )
    libelle = models.CharField(max_length=255, blank=False, null=False)
    exploitation = models.ForeignKey('Exploitation', on_delete=models.CASCADE)
    def __str__(self):
        return self.libelle


class Guichet(models.Model):
    numero_guichet = models.CharField(primary_key=True, max_length=255)
    pointDeVente = models.ForeignKey('PointDeVente', on_delete=models.CASCADE)
    def __str__(self):
        return self.numero_guichet


class Branchement(models.Model):
    id = models.AutoField(primary_key=True)
    type_branchement = models.CharField(max_length=100,blank=False, null=False)
    section = models.CharField(max_length=100, blank=False, null=False)
    lot = models.CharField(max_length=100, blank=False, null=False)
    parcelle = models.CharField(max_length=100, blank=False, null=False)
    rang = models.CharField(max_length=100, blank=False, null=False)
    exploitation = models.ForeignKey('Exploitation', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.section} {self.lot} {self.parcelle} {self.rang}"
    

class EtatAbonnement(models.Model):
    code_etat = models.CharField(primary_key=True, max_length=255)
    libele = models.CharField(max_length=255, blank=False, null=False)
    def __str__(self):
        return self.libele


class Compteur(models.Model):
    numero_compteur = models.CharField(primary_key=True, max_length=9)
    modele_compteur = models.CharField(max_length=255, blank=False, null=False)
    mode_facturation = models.CharField(max_length=255, blank=False, null=False)
    numero_carte = models.CharField(max_length=255, blank=False, null=False)
    def __str__(self):
        return self.numero_compteur


class Abonne(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100, blank=False, null=False)
    prenom = models.CharField(max_length=100, blank=False, null=False)
    numero_telephone = models.CharField(max_length=20, blank=False, null=False)
    adresse_mail = models.EmailField(blank=True, null=True)
    numero_cnib = models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return f"{self.numero_cnib} : {self.nom} {self.prenom}"


class Tarif(models.Model):
    code_tarif = models.CharField(primary_key=True, max_length=255)
    prime_fixe = models.IntegerField(blank=False, null=False)
    redevance = models.IntegerField(blank=False, null=False)
    amperage = models.IntegerField(blank=False, null=False)
    def __str__(self):
        return self.code_tarif


class TrancheTarif(models.Model):
    id = models.AutoField(primary_key=True)
    debut = models.IntegerField(blank=False, null=False)
    fin = models.IntegerField(blank=False, null=False)
    cout_ht = models.DecimalField(max_digits=10, decimal_places=2)
    tde_trch = models.IntegerField(blank=False, null=False)
    tsdaae_trch = models.IntegerField(blank=False, null=False)
    tva_trch = models.DecimalField(max_digits=4, decimal_places=2)
    
    tarif = models.ForeignKey('Tarif', on_delete=models.CASCADE)
    def __str__(self):
        return f'TrancheTarif:{vars(self)}'
    


class Abonnement(models.Model):
    id = models.AutoField(primary_key=True)
    numero_abonnement = models.CharField(max_length=50, blank=False, null=False)
    date_creation = models.DateField(auto_now_add=True)
    date_mise_en_service = models.DateField(null=True, blank=True)
    date_resiliation = models.DateField(null=True, blank=True)
    timbre = models.IntegerField()
    liasse = models.IntegerField()
    numero_police = models.CharField(max_length=255)
    frais_police = models.IntegerField()

    abonne = models.ForeignKey('Abonne', on_delete=models.CASCADE)
    branchement = models.ForeignKey('Branchement', on_delete=models.CASCADE)
    etat_abonnement = models.ForeignKey('EtatAbonnement', on_delete=models.CASCADE)
    compteur = models.OneToOneField('Compteur', null=True, blank=True, on_delete=models.SET_NULL)
    tarif = models.ForeignKey('Tarif', on_delete=models.CASCADE)
    guichet = models.ForeignKey('Guichet', on_delete=models.CASCADE)
    
    
        
    
    def __str__(self):
        return self.numero_abonnement


class Vente(models.Model):
    numero_ticket = models.CharField(primary_key=True, max_length=255)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    tqr = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    energie_paye = models.DecimalField(max_digits=10, decimal_places=2)
    tde = models.DecimalField(max_digits=10, decimal_places=2)
    tsdaae = models.DecimalField(max_digits=10, decimal_places=2)
    tva = models.DecimalField(max_digits=4, decimal_places=2)
    cout_energie = models.DecimalField(max_digits=10, decimal_places=2)
    code_token = models.CharField(max_length=255)

    abonnement = models.ForeignKey('Abonnement', on_delete=models.CASCADE)
    guichet = models.ForeignKey('Guichet', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Vente:{vars(self)}'
