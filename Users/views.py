# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            str1 = 'Account created for ' + str({username}) + '!'
            messages.success(request, str1)
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'Users/register.html', {'form': form})
