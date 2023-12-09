from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from app.forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.cache import never_cache

@never_cache
def login_view(request):
    if not request.user.is_authenticated:    
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in Successfully !!")
                    return redirect(reverse('dashboard'))
        else:
            form = AuthenticationForm()
        return render(request, 'app/login.html', {'form':form})
    else:
        return redirect(reverse('dashboard'))

@never_cache
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            messages.success(request, 'Account Created Successfully !!')
            return redirect(reverse('login'))
    else:
        form = SignUpForm()
    return render(request, 'app/signup.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect(reverse('login'))


@login_required
@never_cache
def dashboard(request):
    username = request.user.username
    first_name = request.user.first_name
    last_name = request.user.last_name
    email = request.user.email
    profile_pic = request.user.profile_picture

    return render(request, 'app/dashboard.html', {'username': username, 'first_name': first_name,'last_name': last_name,'email': email,'profile_picture': profile_pic,})

