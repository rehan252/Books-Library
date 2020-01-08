from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse

from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('accounts:user_login')
    else:
        user_form = RegistrationForm()
    return render(request, 'accounts/register.html', {'user_form': user_form})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate user from Database
        user = authenticate(username=username, password=password)

        # if user is authenticated
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('BookLibrary:home'))
            else:
                return HttpResponse("Account is Inactive")

        else:
            return HttpResponse("Invalid login details")

    else:
        return render(request, 'accounts/login.html', {})


@login_required()
def user_logout(request):
    logout(request)
    return redirect(reverse('accounts:user_login'))
