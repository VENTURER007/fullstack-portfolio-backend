from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


#Hero Section models

class Socials(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    logo_url = models.URLField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Socials"

class TechStacks(models.Model):
    name = models.CharField(max_length=100)
    logo_url = models.URLField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Tech Stack"
        verbose_name_plural = "Tech Stacks"

class HeroSection(models.Model):
    role = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    background_image = models.ImageField(upload_to='assets/profile_image/')
    socials = models.ManyToManyField(Socials, blank=True)
    tech_stack = models.ManyToManyField(TechStacks, blank=True)

    def __str__(self):
        return "Hero Section Contents"

#About me section

# Custom validator to check if the file is an image
def validate_image_extension(value):
    valid_extensions = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp', 'svg']  # Add more extensions if needed
    ext = value.name.split('.')[-1].lower()
    if ext not in valid_extensions:
        raise ValidationError(
            _('Unsupported file extension. Only JPEG, PNG, GIF, BMP, WEBP, and SVG images are allowed.')
        )

class AboutMe(models.Model):
    title = models.CharField(max_length=100)
    main_description = models.TextField()
    sub_description = models.TextField()
    styling_image = models.FileField(upload_to='assets/about_me/', validators=[validate_image_extension])

    def __str__(self):
        return "About Me"
    
    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

#Project section model

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech_stacks = models.ManyToManyField(TechStacks)
    github_url = models.URLField(blank=True)
    live_demo_url = models.URLField(blank=True)
    project_image = models.ImageField(upload_to='project_images/')
    blog_url = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

#contact section model

class Contact(models.Model):
    title = models.TextField()
    email = models.EmailField()
    location = models.CharField(max_length=100)
 

    def __str__(self):
        return "Contact Details"
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact"