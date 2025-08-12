from django.contrib import admin

# Register your models here.
from .models import Service, MessageContact, ZoneCouverture,Slider,Actualite,Logo

admin.site.register(Service)
admin.site.register(MessageContact)
admin.site.register(ZoneCouverture)
admin.site.register(Slider)
admin.site.register(Actualite)
admin.site.register(Logo)
