from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HeroSerializer, LoginSerializer
from .models import Hero, Login


# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all().order_by('username')
    serializer_class = LoginSerializer

