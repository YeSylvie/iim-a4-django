from django.forms import ModelForm
from django.utils import timezone
from .models import Contact, UploadCvFile

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['lastname', 'firstname', 'email', 'message']

class UploadCvFileForm(ModelForm):
    class Meta:
        model = UploadCvFile
        fields = ['cv_name', 'cv_file']