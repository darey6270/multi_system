from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .forms import UserRegisterForm, UserForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from app_user.models import UserProfile

User = get_user_model()


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                u = User.objects.get(username=username)
                if request.user.is_superuser:
                    return render(request, 'multi_levelsystem/index.html',
                                  {'form': form})
                elif u.userprofile.status:
                    logout(request)
                    messages.error(request, 'this Ip has be blocked')
                    return render(request, 'app_user/sign-in.html',
                                  {'form': form})
                else:
                    return HttpResponseRedirect(reverse('app_user:user_login'))
        else:
            messages.error(request, 'username or password not correct')
            return render(request, 'app_user/sign-in.html',
                          {'form': form})


    else:
        form = AuthenticationForm()
    return render(request, 'app_user/sign-in.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('multi_levelsystem:index'))


def register(request):
    if request.method == "POST":
        user_register = UserRegisterForm(data=request.POST)
        user_form = UserForm(data=request.POST)
        if user_register.is_valid() and user_form.is_valid():
            user = user_form.save()
            user.save()
            messages.success(request, 'Account created successfully')
            return HttpResponseRedirect(reverse('app_user:user_login'))
    else:
        user_register = UserRegisterForm()
        user_form = UserForm()
    return render(request, 'app_user/registration.html',
                  {'user_form': user_form, 'reg_form': user_register})
