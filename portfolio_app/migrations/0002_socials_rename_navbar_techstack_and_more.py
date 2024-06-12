# Generated by Django 5.0.6 on 2024-06-09 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Socials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('logo_url', models.URLField()),
            ],
        ),
        migrations.RenameModel(
            old_name='NavBar',
            new_name='TechStack',
        ),
        migrations.RenameField(
            model_name='herosection',
            old_name='heading',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='herosection',
            old_name='subheading',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='techstack',
            old_name='link',
            new_name='logo_url',
        ),
        migrations.RenameField(
            model_name='techstack',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='herosection',
            name='tech_stack',
            field=models.ManyToManyField(blank=True, to='portfolio_app.techstack'),
        ),
        migrations.AddField(
            model_name='herosection',
            name='socials',
            field=models.ManyToManyField(blank=True, to='portfolio_app.socials'),
        ),
    ]