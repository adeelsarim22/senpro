# Generated by Django 4.1.2 on 2022-10-04 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0001_initial"),
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="custom_recipes",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="customer", to="recipe.recipe"
            ),
        ),
        migrations.AlterField(
            model_name="nutritionist",
            name="recipes",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="nutritionist", to="recipe.recipe"
            ),
        ),
    ]
