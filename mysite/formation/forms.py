from django import forms
from django.utils import timezone
from .models import Contact

# class ContactForm(forms.ModelForm):
#     lastname = forms.CharField(label='Votre nom', max_length=200)
#     firstname = forms.CharField(label='Votre prénom', max_length=200)
#     email = forms.EmailField(label='Votre mail')
#     message = forms.CharField(label='Votre message', widget=forms.Textarea)
#     created_date = forms.DateTimeField(timezone.now)