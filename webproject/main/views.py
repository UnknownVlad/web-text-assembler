from .forms import UserRegistrationForm

from .forms import UserLoginForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ChoiceForm
from .text import check_text



def index(request):
    return render(request, 'main/index.html')


@login_required
def home(request):
    result = ''
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            choice = form.cleaned_data['choice']
            choice_lang = form.cleaned_data['choice_lang']
            text = form.cleaned_data['text']
            result = ', '.join(check_text(choice, choice_lang, text))
    else:
        form = ChoiceForm()
    return render(request, 'main/home.html', {'form': form, 'result': result})



def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'main/registration.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home')
    else:
        form = UserLoginForm()
    return render(request, 'main/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')
