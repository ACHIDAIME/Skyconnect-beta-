from django.contrib import admin

# Register your models here.
from .models import Service, MessageContact, ZoneCouverture,Slider,Actualite,Logo,Commune,ActualiteImage

admin.site.register(Service)
admin.site.register(MessageContact)
admin.site.register(ZoneCouverture)
admin.site.register(Commune)
admin.site.register(Slider)
admin.site.register(Logo)

class ActualiteImageInline(admin.TabularInline):
    model = ActualiteImage
    extra = 3  # nombre de formulaires vides affichés par défaut
    fields = ['image', 'alt']
    # Tu peux aussi ajouter 'image' dans readonly_fields si besoin

@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):
    inlines = [ActualiteImageInline]
    list_display = ('titre', 'date_pub')
    search_fields = ('titre',)