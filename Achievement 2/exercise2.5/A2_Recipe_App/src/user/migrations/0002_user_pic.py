# Generated by Django 4.2.3 on 2023-07-25 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pic',
            field=models.ImageField(default='no_picture.jpg', upload_to='user'),
        ),
    ]
