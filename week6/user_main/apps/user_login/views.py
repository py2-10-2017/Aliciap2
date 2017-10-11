# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, redirect

def index(request):
    return render(request, "user_login/index.html")