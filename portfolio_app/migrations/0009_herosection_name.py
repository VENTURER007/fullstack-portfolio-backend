# Generated by Django 5.0.6 on 2024-06-24 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0008_projects_blog_url_alter_projects_github_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='herosection',
            name='name',
            field=models.CharField(default='ASWIN A K', max_length=100),
        ),
    ]