from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HeroSerializer, LoginSerializer
from .models import Hero, Login
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all().order_by('username')
    serializer_class = LoginSerializer


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        # return render(request, 'dappx/login.html', {})
        return HttpResponse("Login details valid")
