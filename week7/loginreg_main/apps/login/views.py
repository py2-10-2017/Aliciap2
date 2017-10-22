# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages


def index(request):
    return render(request, 'login/index.html')

def login_view(request):
    return render(request, 'login/login.html')

def register_view(request):
    return render(request, 'login/registration.html')

def register(request):
    if len(request.POST['first_name']) < 1:
        messages.error(request, "Field is required.")
    if request.POST['first_name'] == 'Alicia':
        messages.error(request, 'Pandas are so cute!')
    
    return redirect('/')
   


def success(request):
    context = {
        'user': Friend.object.get(id=request.session['id'])
    }
    return render(request, 'login/success.html', context)

