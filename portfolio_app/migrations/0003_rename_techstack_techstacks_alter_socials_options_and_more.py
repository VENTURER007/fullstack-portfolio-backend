# Generated by Django 5.0.6 on 2024-06-09 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_socials_rename_navbar_techstack_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TechStack',
            new_name='TechStacks',
        ),
        migrations.AlterModelOptions(
            name='socials',
            options={'verbose_name': 'Social', 'verbose_name_plural': 'Socials'},
        ),
        migrations.AlterModelOptions(
            name='techstacks',
            options={'verbose_name': 'Tech Stack', 'verbose_name_plural': 'Tech Stacks'},
        ),
    ]
