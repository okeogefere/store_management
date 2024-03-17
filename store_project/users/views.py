from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from .models import User
# Create your views here.

def sign_in(request):
    if request.user.is_authenticated: #checks if user is authenticated and redirects back to home page
        messages.warning(request, 'You are logged in Already')
        return redirect('home')
    
    if request.method == 'POST': #checks if the request is a POST request
        email = request.POST.get('email')  #gets the user email from the login input fields
        password = request.POST.get('password')  #gets the user password from the login input fields

        try: # Use try and catch exceptions to check if the user has an account registered
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user is not None: # if the user exist
                login(request, user)
                messages.success(request, "You are logged in")
                return redirect('home')
            else: #if the user does not exist
                messages.warning(request, 'User does not Exist, Create an account')
        except:
            messages.warning(request, f"User with {email} does not exist")
    return render(request, 'users/sign-in.html')

def sign_out(request):
    logout(request)
    messages.success(request, f" You are logged out")

    return redirect('sign-in')