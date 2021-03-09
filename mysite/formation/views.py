from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Contact
# from .forms import ContactForm

# Create your views here.
def home(request): 
    return render(request, 'formation/index.html')

def about(request):
    return render(request, 'formation/about.html')

def contact(request):
    messages = Contact.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'formation/contact.html', {'messages': messages})

# def new_contact(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.pcreated_date = timezone.now()
#             post.save()
#     else:
#         form = ContactForm()
#     return render(request, 'formation/contact.html', {'form': form})
