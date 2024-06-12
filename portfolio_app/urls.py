from django.urls import path
from .views import SocialsList, TechStacksList, HeroSectionDetail, AboutMeDetail, ProjectsDetail, ContactDetail

urlpatterns = [
    path('socials/', SocialsList.as_view(), name='socials-list'),
    path('techstacks/', TechStacksList.as_view(), name='techstacks-list'),
    path('hero/', HeroSectionDetail.as_view(), name='hero-detail'),
    path('aboutme/', AboutMeDetail.as_view(), name='about-detail'),
    path('projects/', ProjectsDetail.as_view(), name='projects-detail'),
    path('contact/', ContactDetail.as_view(), name='contact-list-create'),
]
