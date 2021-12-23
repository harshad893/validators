from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def contact(request):
    c=ContactForm()
    d={'c':c}
    if request.method=='POST':
        FD=ContactForm(request.POST)
        if FD.is_valid():
            return HttpResponse(str(FD.cleaned_data))
    return render(request,'contact.html',d)