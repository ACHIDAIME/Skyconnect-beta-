from django.shortcuts import render
from .forms import MessageContactForm
from django.contrib import messages
from .models import Service,Slider,Actualite, ZoneCouverture,Commune
from django.core.mail import send_mail

# Create your views here.
def accueil(request):
    sliders = Slider.objects.filter(is_active=True).order_by('ordre')
    return render(request, 'core/accueil.html', {
        'sliders': sliders,
    })

# core/views.py
# core/views.py
def zone_couverture(request):
    zones = ZoneCouverture.objects.prefetch_related('communes').all()
    return render(request, 'core/zone_couverture.html', {'zones': zones})

def qui_sommes_nous(request):
    return render(request, 'core/qui_sommes_nous.html')

def offres(request):
    services = Service.objects.all().order_by('ordre')
    return render(request, 'core/offres.html', {'services': services})

def blog(request):
    actualites = Actualite.objects.prefetch_related('images').order_by('-date_pub')
    return render(request, 'core/blog.html', {'actualites': actualites})

def contact(request):
    form = MessageContactForm()
    success = False

    if request.method == 'POST':
        form = MessageContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            messages.success(request, " ✅ Votre message a bien été envoyé. Merci !")
            form = MessageContactForm()  # Réinitialiser le formulaire

    return render(request, 'core/contact.html', {'form': form, 'success': success})

def blog(request):
    actualites = Actualite.objects.all().order_by('-date_pub')
    return render(request, 'core/blog.html', {'actualites': actualites})

def contact(request):
    if request.method == 'POST':
        form = MessageContactForm(request.POST)
        if form.is_valid():
            message = form.save()
            # Envoi d’un email à l’admin
            send_mail(
                subject=f"Nouveau message de contact : {message.sujet}",
                message=f"Nom : {message.nom}\nEmail : {message.email}\nMessage :\n{message.message}",
                from_email=None,
                recipient_list=['noc@skyconnect-sa.com'],  # Mets ici l’email à notifier
                fail_silently=False,
            )
            messages.success(request, "Votre message a bien été envoyé !")
            return redirect('contact')
    else:
        form = MessageContactForm()
    return render(request, 'core/contact.html', {'form': form})

def mentions_legales(request):
    return render(request, 'core/mentions_legales.html')

