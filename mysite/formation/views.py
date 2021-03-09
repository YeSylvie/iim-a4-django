from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request): 
    return render(request, 'formation/index.html')

def about(request):
    return render(request, 'formation/about.html')

def contact(request):
    return render(request, 'formation/contact.html')
