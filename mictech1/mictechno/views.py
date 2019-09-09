from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,'home.html')
def events(request):
    return render(request,'events.html')

def register(request):
    return render(request,'Registrations.html')

def contact(request):
    return render(request,'contact.html')
