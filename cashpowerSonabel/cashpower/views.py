# gestion_abonnements/views.py
import random
from django.shortcuts import render, get_object_or_404, redirect
from .models import Abonne, Abonnement, Vente, Branchement
from .forms import AbonneForm, AbonnementForm, VenteForm

def home(request):
    return render (request, 'index.html')
def abonne_list(request):
    
    abonnes = Abonne.objects.all()
    return render(request, 'abonne_list.html', {'abonnes': abonnes})

def abonne_detail(request, pk):
    abonne = get_object_or_404(Abonne, pk=pk)
    return render(request, 'abonne_detail.html', {'abonne': abonne})

def abonne_create(request):
    if request.method == 'POST':
        form = AbonneForm(request.POST)
        if form.is_valid():
            abonne = form.save()
            return redirect('abonne_detail', pk=abonne.pk)
    else:
        form = AbonneForm()
    return render(request, 'abonne_form.html', {'form': form})

def abonne_edit(request, pk):
    abonne = get_object_or_404(Abonne, pk=pk)
    if request.method == 'POST':
        form = AbonneForm(request.POST, instance=abonne)
        if form.is_valid():
            abonne = form.save()
            return redirect('abonne_detail', pk=abonne.pk)
    else:
        form = AbonneForm(instance=abonne)
    return render(request, 'abonne_form.html', {'form': form})






def abonnement_list(request):
    abonnements = Abonnement.objects.all()
    return render(request, 'abonnements/index.html', {'abonnements': abonnements})

def abonnement_detail(request, pk):
    abonnement = get_object_or_404(Abonnement, pk=pk)
    return render(request, 'abonnements/detail.html', {'abonnement': abonnement})

def abonnement_create(request):
    if request.method == 'POST':
        form = AbonnementForm(request.POST)
        if form.is_valid():
            abonnement = form.save(commit=False)
            
            branchement_temp = abonnement.branchement
            abonnement.numero_abonnement = f"{branchement_temp.section} {branchement_temp.lot} {branchement_temp.parcelle} {branchement_temp.rang}"
            abonnement.timbre = 500
            abonnement.liasse = 1500
            abonnement.frais_police = 2000
            abonnement.numero_police = ''.join([str(int(char)) for char in abonnement.numero_abonnement.replace(' ', '')])
            
            abonnement.save()

            return redirect('abonnement_list')        
    else:
        form = AbonnementForm()
    return render(request, 'abonnements/create.html', {'form': form})


def abonnement_edit(request, pk):
    abonnement = get_object_or_404(Abonnement, pk=pk)
    if request.method == 'POST':
        form = AbonnementForm(request.POST, instance=abonnement)
        if form.is_valid():
            abonnement = form.save()
            return redirect('abonnement_detail', pk=abonnement.pk)
    else:
        form = AbonnementForm(instance=abonnement)
    return render(request, 'abonnement_form.html', {'form': form})





def vente_list(request):
    ventes = Vente.objects.all()
    return render(request, 'ventes/index.html', {'ventes': ventes})

def vente_detail(request, pk):
    vente = get_object_or_404(Vente, pk=pk)
    return render(request, 'vente_detail.html', {'vente': vente})

def vente_create(request):
    
    def calcul_TQR(M):
        if M < 100:
            TQR = 0
        elif 100 <= M <= 1000:
            TQR = 20
        elif 1000 < M <= 5000:
            TQR = 30
        elif 5000 < M <= 10000:
            TQR = 50
        elif 10000 < M <= 50000:
            TQR = 100
        else:
            n = M // 50000
            TQR = 50 * (n + 2)
        return TQR
    

    if request.method == 'POST':
        form = VenteForm(request.POST)
        if form.is_valid():
            vente = form.save(commit=False)
            vente.tqr = calcul_TQR(vente.montant)
            p = vente.abonnement.tarif.prime_fixe
            r = vente.abonnement.tarif.redevance
            mat = vente.montant - p - r - vente.tqr
            eht = mat/108
            vente.tde = 2 * eht
            vente.tsdaae = 3*eht
            vente.tva = 18 * eht / 100
            vente.energie_paye = eht - vente.tde - vente.tsdaae - vente.tva
            vente.cout_energie = vente.energie_paye * 108
            groups_of_digits = [str(random.randint(0, 9999)).zfill(4) for _ in range(5)]
            vente.code_token = ' '.join(groups_of_digits)
            vente.numero_ticket = groups_of_digits
            
            vente.save()

            return redirect('vente_list') 
            
    else:
        form = VenteForm()
    return render(request, 'ventes/create.html', {'form': form})

def vente_edit(request, pk):
    vente = get_object_or_404(Vente, pk=pk)
    if request.method == 'POST':
        form = VenteForm(request.POST, instance=vente)
        if form.is_valid():
            vente = form.save()
            return redirect('vente_detail', pk=vente.pk)
    else:
        form = VenteForm(instance=vente)
    return render(request, 'vente_form.html', {'form': form})