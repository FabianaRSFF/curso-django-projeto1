# Generated by Django 4.0.2 on 2022-08-11 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(),
        ),
    ]