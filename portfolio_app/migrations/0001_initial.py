# Generated by Django 5.0.6 on 2024-06-09 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeroSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('subheading', models.CharField(max_length=200)),
                ('background_image', models.ImageField(upload_to='hero/')),
            ],
        ),
        migrations.CreateModel(
            name='NavBar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField()),
            ],
        ),
    ]
