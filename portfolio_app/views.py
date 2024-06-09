from rest_framework import generics
from .models import NavBar, HeroSection
from .serializers import NavBarSerializer, HeroSectionSerializer

class NavBarList(generics.ListCreateAPIView):
    queryset = NavBar.objects.all()
    serializer_class = NavBarSerializer

class HeroSectionDetail(generics.RetrieveUpdateAPIView):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer
