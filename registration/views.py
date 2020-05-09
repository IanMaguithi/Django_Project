from django.shortcuts import render, redirect
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
                print('Username already taken')

            elif User.objects.filter(email=email).exists():
                print('Email already exists')

            else:
                user = User.objects.create_user(username=username, email=email, password=password_one, first_name=first_name, last_name=last_name)
                user.save();
                print('User created')

        else:
            print('Passwords do not match')

        return redirect('/')

    else:
        return render(request, 'registration/register.html')
