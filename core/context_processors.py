from .models import Logo

def logo_context(request):
    logo = Logo.objects.first()
    return {'logo': logo}