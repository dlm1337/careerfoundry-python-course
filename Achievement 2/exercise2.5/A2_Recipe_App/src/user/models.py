from django.db import models


# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    pic = models.ImageField(upload_to="user", default="no_picture.jpg")

    def __str__(self):
        return str(self.username)
