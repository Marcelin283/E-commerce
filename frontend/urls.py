from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "frontend"
urlpatterns = [
    path('acceuil', views.acceuil, name="acceuil"),
    path('produits', views.produits, name="produits"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('services', views.services, name="services"),
    path('ajouterProduit', views.ajouterProduit, name="ajouterProduit"),
    path('acheter/<int:produit_id>', views.acheter, name='acheter'),
    path('supprimer/<int:produit_id>',views.supprimer, name='supprimer'),
    path('modifier/<int:produit_id>', views.modifier, name='modifier'),
    path('mobile', views.mobile, name="mobile")
]
