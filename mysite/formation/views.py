from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Contact, UploadCvFile
from .forms import ContactForm, UploadCvFileForm

# Create your views here.
def home(request): 
    return render(request, 'formation/index.html')

def apply(request):
    cvs = UploadCvFile.objects.filter(uploaded_date__lte=timezone.now()).order_by('uploaded_date')
    return render(request, 'formation/apply.html', {'cvs': cvs})

def contact(request):
    messages = Contact.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'formation/contact.html', {'messages': messages})

def dashboard(request):
    return render(request, 'formation/dashboard.html')

def new_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = timezone.now()
            post.save()
        else:
            return HttpResponse(status=500) 
    else:
        form = ContactForm()
    return redirect('/contact')

def new_cv(request):
    if request.method == "POST":
        form = UploadCvFileForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.uploaded_date = timezone.now()
            post.save()
        else:
            return HttpResponse(status=500) 
    else:
        form = UploadCvFileForm()
    return redirect('/apply')
