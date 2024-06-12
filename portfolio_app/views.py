from rest_framework import generics
from .models import Socials, TechStacks, HeroSection, AboutMe, Projects, Contact
from .serializers import SocialsSerializer, TechStacksSerializer, HeroSectionSerializer, AboutMeSerializer, ProjectsSerializer, ContactSerializer

class SocialsList(generics.ListAPIView):
    queryset = Socials.objects.all()
    serializer_class = SocialsSerializer
    http_method_names = ['get']


class TechStacksList(generics.ListAPIView):
    queryset = TechStacks.objects.all()
    serializer_class = TechStacksSerializer
    http_method_names = ['get']



class HeroSectionDetail(generics.RetrieveAPIView):
    queryset = HeroSection.objects.all()
    serializer_class = HeroSectionSerializer
    http_method_names = ['get']

    def get_object(self):
        return HeroSection.objects.first()

class AboutMeDetail(generics.RetrieveAPIView):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer
    http_method_names = ['get']

    def get_object(self):
        return AboutMe.objects.first()

class ProjectsDetail(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    http_method_names = ['get']


class ContactDetail(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ['get']

    def get_object(self):
        return Contact.objects.first()
