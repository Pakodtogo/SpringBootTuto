# gestion_abonnements/views.py
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
    return render(request, 'abonnement_detail.html', {'abonnement': abonnement})

def abonnement_create(request):
    if request.method == 'POST':
        form = AbonnementForm(request.POST)
        branchement_temp = form.fields['branchement']
        
        abonnemnent_save = Abonnement ()
        # abonnemnent_save.abonne = form.fields['abonne']
        # abonnemnent_save.branchement = form.fields['branchement']
        # abonnemnent_save.etat_abonnement = form.fields['etat_abonnement']
        abonnemnent_save.compteur = form.fields['compteur']
        abonnemnent_save.tarif = form.fields['tarif']
        abonnemnent_save.guichet = form.fields['guichet']
        
        abonnemnent_save.numero_abonnement = f"{branchement_temp.section} {branchement_temp.lot} {branchement_temp.parcelle} {branchement_temp.rang}"
        
        abonnemnent_save.timbre = 500
        abonnemnent_save.liasse = 1500
        abonnemnent_save.frais_police = 2000
        abonnemnent_save.numero_police = ''.join([str(int(char)) for char in abonnemnent_save.numero_abonnement.replace(' ', '')])
        
        abonnemnent_save.save()
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
    return render(request, 'vente_list.html', {'ventes': ventes})

def vente_detail(request, pk):
    vente = get_object_or_404(Vente, pk=pk)
    return render(request, 'vente_detail.html', {'vente': vente})

def vente_create(request):
    if request.method == 'POST':
        form = VenteForm(request.POST)
        if form.is_valid():
            vente = form.save()
            return redirect('vente_detail', pk=vente.pk)
    else:
        form = VenteForm()
    return render(request, 'vente_form.html', {'form': form})

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