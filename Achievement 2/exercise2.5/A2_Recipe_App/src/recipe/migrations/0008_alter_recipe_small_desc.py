# Generated by Django 4.2.3 on 2023-07-25 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0007_alter_recipe_small_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='small_desc',
            field=models.TextField(default='No Description has been added currently.', max_length=200),
        ),
    ]
