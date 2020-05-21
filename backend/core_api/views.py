from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HeroSerializer, UserSerializer
from .models import Hero, Users
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm


# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('username')
    serializer_class = UserSerializer


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponse("Correct login details")
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        # return render(request, 'dappx/login.html', {})
        return HttpResponse("Return to login")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponse("Signup successful: " + username + ", " + raw_password)
        else:
            print(form.errors)
            return HttpResponse("Signup unsuccessful: " + form.errors)
    else:
        form = UserCreationForm()
        return HttpResponse("POST required for /user_register")
    #return render(request, 'signup.html', {'form': form})

