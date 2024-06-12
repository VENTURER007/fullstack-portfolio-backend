# Generated by Django 5.0.6 on 2024-06-10 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_rename_techstack_techstacks_alter_socials_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('main_description', models.TextField()),
                ('sub_description', models.TextField()),
                ('styling_image', models.ImageField(upload_to='about/')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='herosection',
            name='background_image',
            field=models.ImageField(upload_to='profile_image/'),
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('github_url', models.URLField()),
                ('live_demo_url', models.URLField()),
                ('project_image', models.ImageField(upload_to='project_images/')),
                ('tech_stacks', models.ManyToManyField(to='portfolio_app.techstacks')),
            ],
        ),
    ]