# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Friend, Note

def check_logged_in(request):
    #make sure user is logged in
    if not "id" in request.session.keys():
        print "no user here"
        return redirect('/')

# Create your views here.
def index(request):

    return render(request, "users/index.html")

def login_view(request):
    return render(request, 'users/login.html')

def register_view(request):
    return render(request, 'users/registration.html')

def login(request):
    errors_or_user = Friend.objects.validate_login(request.POST)
    if errors_or_user[0]:
        for fail in errors_or_user[0]:
            messages.error(request, fail)
        return redirect('/login_view')

    print errors_or_user[1]
    request.session['id'] = errors_or_user[1].id
    return redirect('/success')

def register(request):
    errors_or_user = Friend.objects.validate_registration(request.POST)

    if errors_or_user[0]:
        for fail in errors_or_user[0]:
            messages.error(request, fail)
        return redirect('/register_view')

    request.session['id'] = errors_or_user[1].id    
    return redirect('/success')

def logout(request):
    del request.session['id']
    return redirect('/')

# REQUIRES LOGIN
def success(request):

    check_logged_in(request)

    context = {
        "user": Friend.objects.get(id=request.session['id']),
        "notes": Note.objects.all()
    }
    return render(request, "users/success.html", context)

def create(request):
    check_logged_in(request)

    Note.objects.create(
        message = request.POST['note'],
        author_id = request.session['id']
    )
    return redirect('/success')
