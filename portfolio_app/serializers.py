from rest_framework import serializers
from .models import HeroSection, Socials, TechStacks, AboutMe, Projects, Contact

class SocialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Socials
        fields = '__all__'

class TechStacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechStacks
        fields = '__all__'

class HeroSectionSerializer(serializers.ModelSerializer):
    socials = SocialsSerializer(many=True, read_only=True)
    tech_stack = TechStacksSerializer(many=True, read_only=True)

    class Meta:
        model = HeroSection
        fields = '__all__'

class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):
    tech_stacks = TechStacksSerializer(many=True, read_only=True)

    class Meta:
        model = Projects
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'