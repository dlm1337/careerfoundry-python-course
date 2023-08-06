# Generated by Django 4.2.3 on 2023-07-27 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipe', '0001_initial'),
        ('recipeingredient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeIngredientIntermediary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
                ('recipe_ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeingredient.recipeingredient')),
            ],
        ),
    ]
