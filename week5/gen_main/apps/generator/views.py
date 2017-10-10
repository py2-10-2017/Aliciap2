# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def index(request):
    try:
        request.session['attempts']
    except KeyError:
        request.session['attempts'] = 0

    return render(request, "generator/index.html")

def generate(request):
    request.session['attempts'] += 1
    request.session['random_word'] = get_random_string(length=14)
    return redirect('/')

def reset(request):
    del request.session['attempts']
    del request.session['random_word']
    return redirect('/')