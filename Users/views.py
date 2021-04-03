# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            str1 = 'Account created for ' + {username} + '!'
            messages.success(request, str1)
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'Users/register.html', {'form': form})
