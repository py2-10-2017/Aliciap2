# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Reviews, Authors, Books
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
        'recent': Reviews.objects.recent_and_not()[0],
        'more': Reviews.objects.recent_and_not()[1]
    }
    return render(request, 'bookreviews/reviews.html', context)

def add(request):
    context = {
        'Authors': Authors.objects.all()
    }
    return render(request, 'bookreviews/newreview.html', context)

def show(request, book_id):
    context = {
        'book': Books.objects.get(id=book_id)
    }
    return render(request, 'bookreviews/book.html', context)

def create(request):
    errs = Reviews.objects.validate_review(request.POST)
    if errs:
        for e in errs:
            messages.error(request, e)
    else:
        book_id = Reviews.objects.create_review(request.POST, request.session['user_id']).book.id
    return redirect('/{}'.format(book_id))

def create_additional(request, book_id):
    the_book = Books.objects.get(id=book_id)
    new_book_data = {
        'title': the_book.title,
        'author': the_book.author.id,
        'rating': request.POST['rating'],
        'review': request.POST['review'],
        'new_author': ''
    }
    errs = reviews.objects.validate_review(new_book_data)
    if errs:
        for e in errs:
            messages.error(request, e)
    else:
        reviews.objects.create_review(new_book_data, request.session['user_id'])
    return redirect('/{}' .format(book_id))
