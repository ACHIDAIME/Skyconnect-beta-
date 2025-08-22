import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skyconnect.settings")
django.setup()

from django.contrib.auth.models import User

# Change ici le nom, email et mot de passe
username = "Mirabeau"
email = "mirabeautoureend@gmail.com"
password = "0001"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser créé !")
else:
    print("Superuser existe déjà.")
