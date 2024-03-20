from django.shortcuts import render, redirect
from backend.models import *

# Create your views here.
def acceuil(request):
    return render(request, 'acceuil.html')

def produits(request):
    produits = Produit.objects.all()
    return render(request, 'produits.html', {"produits": produits})

def dashboard(request):
    ventes = Vente.objects.all()
    return render(request, 'dashboard.html', {"ventes": ventes})

def services(request):
    return render(request, 'services.html')

def ajouterProduit(request):
    if request.method == 'GET':
        return render(request, "ajouterProduit.html")
    else:
        nom = request.POST ["nom"]
        prix = request.POST ["prix"]
        categorie = request.POST ["categorie"]
        qte = request.POST ["qte"]
        p1 = Produit.objects.create(nom = nom, prix = prix, categorie = categorie, qte = qte)
        return redirect("frontend:produits")
    
def acheter(request, produit_id):
    produit=Produit.objects.get(pk=produit_id)
    produits = Produit.objects.all()
    if request.method == 'GET':
        return render(request, 'acheter.html', {"produit": produit})
    else :
        quantite = request.POST ["quantite"]
        vente = Vente.objects.create(produit = produit, quantite = quantite, date = date.today())
        return redirect("frontend:dashboard")
    
def supprimer(request, produit_id):
    if request.method == 'GET':
        produits=Produit.objects.get(pk=produit_id)
        produits.delete()
        return redirect("frontend:produits")
    
def modifier(request, produit_id):
    produit=Produit.objects.get(pk=produit_id)
    if request.method == 'GET':
        produits=Produit.objects.get(pk=produit.id)
        return render(request, "modifier.html", {'produits':produits})
    else:
        nom = request.POST ["nom"]
        prix = request.POST ["prix"]
        categorie = request.POST ["categorie"]
        qte = request.POST ["qte"]
        p1 = Produit.objects.update(nom = nom, prix = prix, categorie = categorie, qte = qte)
        return redirect("frontend:produits")

def mobile(request):
    if request.method == 'GET':
        return render(request, "services.html")
    else:
        numero = request.POST ["numero"]
        n1 = Numero.objects.create(numero = numero)
        return redirect("frontend:produits")