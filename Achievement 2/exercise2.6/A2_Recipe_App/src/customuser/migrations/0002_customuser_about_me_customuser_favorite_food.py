# Generated by Django 4.2.3 on 2023-07-28 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='about_me',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='favorite_food',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
