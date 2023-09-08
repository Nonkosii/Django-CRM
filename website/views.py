from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import Record
from .forms import SignUpForm, AddRecordForm

def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        current_user = authenticate(username=username, password=password)
        if current_user is not None:
            login(request, current_user)
            messages.success(request, "You log in")
        else:
            messages.success(request, "Error occurred...")

        return redirect('home')

    else:
        return render(request, 'home.html', {'records':records})
    

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

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added...")
                return redirect('home')

        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated...")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, "Record deleted successfully")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in")
        return redirect('home')

def login_user(request):
    return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You log out...")
    return redirect('home')