from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            return render(request, 'accounts/register_done.html',
                           {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/register.html',
                        {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data # cd --> {'username': 'value1', 'password': 'value2'}
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Logged in successfully')
                else:
                    return HttpResponse('Disabled Account')
            else:
                return HttpResponse('Invalid Login')

    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required()
def dashboard(request):
    return render(request, 'accounts/dashboard.html', {'section': 'dashboard'})
