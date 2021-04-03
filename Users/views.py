# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


# Create your views here.


def register(request):
    form = UserCreationForm()
    return render(request, 'Users/register.html', {'form': form})
