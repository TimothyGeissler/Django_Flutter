from rest_framework import serializers
from .models import Hero, Login


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')


class LoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Login
        fields = ('username', 'password')