from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password_one = request.POST['password_one']
        password_two = request.POST['password_two']

        if password_one == password_two:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, email=email, password=password_one, first_name=first_name, last_name=last_name)
                user.save();
                print('User created')
                return redirect('login')

        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')

        return redirect('/')

    else:
        return render(request, 'registration/register.html')


def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
