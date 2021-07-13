from django.shortcuts import render
from .forms import *
from django.contrib import messages

# Create your views here.


def home(request):
    form = RegForm()
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            success = 1
            wifi = wifipassword.objects.all().first()
            messages.success(request, 'Registration Successfull')
    return render(request, 'home.html', locals())
