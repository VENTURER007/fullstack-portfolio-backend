# Generated by Django 5.0.6 on 2024-06-10 09:55

import portfolio_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0006_alter_aboutme_styling_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='styling_image',
            field=models.FileField(upload_to='assets/about_me/', validators=[portfolio_app.models.validate_image_extension]),
        ),
    ]
