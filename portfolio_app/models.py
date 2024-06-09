from django.db import models

class NavBar(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.title

class HeroSection(models.Model):
    heading = models.CharField(max_length=200)
    subheading = models.CharField(max_length=200)
    background_image = models.ImageField(upload_to='hero/')

    def __str__(self):
        return self.heading
