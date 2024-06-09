from rest_framework import serializers
from .models import NavBar, HeroSection

class NavBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavBar
        fields = '__all__'

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'
