from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    lastname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
