from django.urls import path
from .views import NavBarList, HeroSectionDetail

urlpatterns = [
    path('navbar/', NavBarList.as_view(), name='navbar-list'),
    path('hero/<int:pk>/', HeroSectionDetail.as_view(), name='hero-detail'),
]
