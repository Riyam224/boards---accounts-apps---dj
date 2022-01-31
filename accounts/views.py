from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# ! login
from django.contrib.auth import login as auth_login
# Create your views here.
from .form import SignupForm

# TODO sign up


def signup(request):

    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return redirect('index')
        else:
            form = SignupForm()
        return render(request, 'signup.html', {'form': form})
