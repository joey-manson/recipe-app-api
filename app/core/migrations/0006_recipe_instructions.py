# Generated by Django 2.1.15 on 2021-12-02 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_recipe_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(blank=True),
        ),
    ]
