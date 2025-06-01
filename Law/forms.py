from django import forms
from django.core.validators import RegexValidator
from .models import Contact


class ContactForm(forms.ModelForm):
    phone = forms.CharField(
        max_length=15,
        required=False,
        validators=[RegexValidator(regex=r'^\d{8,15}$', message="Veuillez entrer un numéro de téléphone valide.")],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'})
    )

    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'phone', 'profession', 'description']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom complet'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'profession': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Profession'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 4}),
        }