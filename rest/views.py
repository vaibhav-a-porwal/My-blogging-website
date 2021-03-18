from django.http import HttpResponse
from django.shortcuts import render

def show_about(request):
    return render(request, 'rest/about.html')

def show_contact(request):
    return render(request, 'rest/contact.html')