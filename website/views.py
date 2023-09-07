from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm

def home(request):
    if request.method == 'POST':
        username = request.GET['username']
        password = request.GET['password']

        current_user = authenticate(username=username, password=password)
        if current_user is not None:
            login(request, current_user)
            messages.success(request, "You log in")
        else:
            messages.success(request, "Error occurred...")

        return redirect('home')

    else:
        return render(request, 'home.html', {})
    

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            current_user = authenticate(username=username, password=password)
            login(request, current_user)
            messages.success(request, "Registered success")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})

def login_user(request):
    return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You log out...")
    return redirect('home')