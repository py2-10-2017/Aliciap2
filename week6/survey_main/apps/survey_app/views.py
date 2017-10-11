# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.



def index(request):
    return render(request, 'survey_app/index.html')

def process(request):
    # if request.method == 'POST':
    request.session['name'] = request.POST['name']
    request.session['dojo_location'] = request.POST['dojo_location']
    request.session['favorite_language'] = request.POST['favorite_language']
    request.session['comment'] = request.POST['comment']

    return redirect('/result')

def result(request):
    if request.session.get('counter') == None:
        request.session['counter'] = 0
        request.session['counter'] += 1

    post_info = {
        'name':request.session['name'],
        'dojo_location':request.session['dojo_location'],
        'favorite_language':request.session['favorite_language'],
        'comment':request.session['comment']
    }
    return render(request, 'survey_app/results.html', post_info)
