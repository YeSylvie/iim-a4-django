from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    lastname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

class UploadCvFile(models.Model):
    cv_name = models.CharField(max_length=255, blank=True)
    cv_file = models.FileField(upload_to='documents/cv/')
    uploaded_date = models.DateTimeField(default=timezone.now)