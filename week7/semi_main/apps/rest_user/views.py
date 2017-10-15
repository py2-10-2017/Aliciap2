# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'rest_user/index.html')


def new(request):
    return render(request, 'rest_user/new.html')
