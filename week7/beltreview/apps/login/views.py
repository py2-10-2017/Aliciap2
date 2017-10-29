from __future__ import unicode_literals
from .models import Users
from ..bookreviews.models import Books
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def register(request):
    result = Users.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully registered!")
    return redirect('/reviewshome')

def login(request):
    result = Users.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully logged in!")
    return redirect ('/reviewshome')

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context = {
        'User': Users.objects.get(id=request.session['user_id'])
    }
    return render(request, 'login/success.html', context)

def show(request, user_id):
    users = Users.objects.get(id=user_id)
    unique_ids = Users.Reviews_left.all().values('Books').distinct()
    unique_books = []
    for Books in unique_ids:
        unique_books.append(books.objects.get(id=book['Book']))
    context = {
        'User': Users,
        'unique_book_reviews': unique_books
    }
    return render(request, 'login/user.html', context)
