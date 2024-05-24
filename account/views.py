
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .form import UserForm, LoginForm

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('APP1:cours')
        else:
            messages.info(request, 'Identifiant ou mot de passe incorrect')

    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = UserForm()


    return render(request, 'register.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('APP1:acceuil')




