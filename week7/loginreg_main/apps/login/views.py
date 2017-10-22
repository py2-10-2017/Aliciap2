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
    errors = []

    if errors:
        for fail in errors:
            messages.error(request, fail)
    
    return redirect('/register_view')
   
    return redirect('/success')  
    #if no errors return to the success method that goes to the success template page
   


def success(request):
    context = {
        'user': Friend.object.get(id=request.session['id'])
    }
    return render(request, 'login/success.html', context)

