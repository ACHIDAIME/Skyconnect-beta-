from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('offres/', views.offres, name='offres'),
    path('contact/', views.contact, name='contact'),
    path('qui-sommes-nous/', views.qui_sommes_nous, name='qui_sommes_nous'),
    path('zone-couverture/', views.zone_couverture, name='zone_couverture'),
    path('services/', views.blog, name='blog'),
    path('mentions-legales/', views.mentions_legales, name='mentions_legales'),
]
