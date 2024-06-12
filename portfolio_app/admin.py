from django.contrib import admin
from .models import  HeroSection, TechStacks, Socials, Projects, AboutMe, Contact

# Register your models here.

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    pass 

@admin.register(TechStacks)
class TechStackAdmin(admin.ModelAdmin):
    pass

@admin.register(Socials)
class SocialsAdmin(admin.ModelAdmin):
    pass

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    pass

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
