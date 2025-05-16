from django.db import models

# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    image = models.ImageField(upload_to="imagini_jucatori")

    def __str__(self):
        return self.name