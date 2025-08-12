from django.db import models

# Create your models here.
# core/models.py

from django.db import models

class Service(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    icone = models.CharField(
        max_length=50,
        help_text="Nom de l’icône Bootstrap ex: 'bi-wifi'",
        default='bi-wifi'
    )
    prix = models.CharField(max_length=50, default='À définir')
    badge = models.CharField(max_length=30, blank=True, help_text="Ex: Populaire, Service+, 24/7")
    badge_color = models.CharField(max_length=30, blank=True, help_text="Ex: badge-promo")
    ordre = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nom

class MessageContact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=150)
    message = models.TextField()
    date_envoye = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.sujet}"

class ZoneCouverture(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # Tu peux ajouter d'autres champs si besoin

    def __str__(self):
        return self.nom

class Slider(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='sliders/')
    is_active = models.BooleanField(default=True)
    ordre = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titre
    
class Actualite(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/')
    date_pub = models.DateField(auto_now_add=True)
    lien = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titre