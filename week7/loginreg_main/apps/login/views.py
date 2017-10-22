# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User


def index(request):
    return render(request, 'login/index.html')

def login_view(request):
    return render(request, 'login/login.html')

def register_view(request):
    return render(request, 'login/registration.html')

def register(request):

    User.objects.validate_registration(request.POST)

    if errors:
        for fail in errors:
            messages.error(request, fail)
    
    return redirect('/register_view')
   

def success(request):
    context = {
        'user': Friend.object.get(id=request.session['id'])
    }
    return render(request, 'login/success.html', context)

