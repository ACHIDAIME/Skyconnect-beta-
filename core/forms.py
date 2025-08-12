from django import forms
from .models import MessageContact

class MessageContactForm(forms.ModelForm):
    class Meta:
        model = MessageContact
        fields = ['nom', 'email', 'sujet', 'message']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemple.com'}),
            'sujet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sujet'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Votre message', 'rows': 4}),
        }
