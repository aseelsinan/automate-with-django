from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import RegisterationForm


def home(request):
    return render(request,'home.html')




def register_view(request):  # noqa: F811
    if request.method == 'POST':
        form = RegisterationForm(request.POST)  # 2. استخدامه هنا
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')            
            return redirect('home') 
        else:
            messages.error(request, 'Failed to create account. Please check the errors below.') 
    else:
        messages.error(request, 'r')
        form = RegisterationForm()  # 3. واستخدامه هنا أيضاً
        
    return render(request, 'register.html', {'form': form})




def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('login')