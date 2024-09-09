from email import message
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def Signup_View(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todoapp:todo_list')

    form = UserCreationForm()
    return render(request,'accounts/signup.html', {'form':form})
  
def Login_View(request):
    if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('todoapp:todo_list')
        else:
            messages.error(request, 'نام کاربری یا گذرواژه اشتباه است')

    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def Logout_View(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')