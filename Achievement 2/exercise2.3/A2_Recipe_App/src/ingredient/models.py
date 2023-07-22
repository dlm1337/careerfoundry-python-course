from django.db import models


# Create your models here.
class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=False)
    def __str__(self):
        return str(self.name)
